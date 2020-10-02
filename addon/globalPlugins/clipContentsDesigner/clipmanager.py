import os
import json
from typing import List, Dict
import functools
import api
import ui
import gui
from keyboardHandler import KeyboardInputGesture
import globalVars
from logHandler import log
import wx

CLIPS_FILE_PATH: str = os.path.join(globalVars.appArgs.configPath, "clips.json")


def recentClips(func):
	@functools.wraps(func)
	def innerFunc(*args, **kwargs):
		func(*args, **kwargs)
		try:
			clips = initClipSfile()
			clip = api.getClipData()
			log.info(clip)
			clips['recent'].insert(0, clip)
			writeClips(clips)
		except OSError:
			pass
	return innerFunc


def initClipSfile():
	clips: Dict[str, List] = {'recent': [], 'favourite': []}
	if not os.path.exists(CLIPS_FILE_PATH):
		with open(CLIPS_FILE_PATH, 'x') as f:
			json.dump(clips, f, indent=2, separators=(',', ':'))
		return clips
	else:
		with open(CLIPS_FILE_PATH, 'r') as f:
			clips = json.load(f)
		return clips


def writeClips(clips):
	with open(CLIPS_FILE_PATH, 'w') as f:
		json.dump(clips, f, indent=2, separators=(',', ':'))


class ClipManagerDialog(wx.Dialog):
	_instance = None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		if ClipManagerDialog._instance is None:
			return super(ClipManagerDialog, cls).__new__(cls, *args, **kwargs)
		return ClipManagerDialog._instance

	def __del__(self):
		ClipManagerDialog._instance = None

	def __init__(self, *args, **kwds):
		if ClipManagerDialog._instance is not None:
			return
		ClipManagerDialog._instance = self

		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		# Translators: title of clipboard manager dialog
		self.SetTitle(_("clip manager"))

		mainSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.clipCategoryTree = wx.TreeCtrl(
			self, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.TR_DEFAULT_STYLE
			| wx.TR_EDIT_LABELS | wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT | wx.TR_SINGLE)
		mainSizer.Add(self.clipCategoryTree, 1, wx.ALL | wx.EXPAND, 0)

		self.clipList = wx.ListCtrl(
			self, wx.ID_ANY, style=wx.LC_EDIT_LABELS
			| wx.LC_HRULES | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_VRULES)
		self.clipList.SetFocus()
		self.clipList.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=-1)
		mainSizer.Add(self.clipList, 1, wx.EXPAND, 0)

		btnSizer = wx.StdDialogButtonSizer()
		mainSizer.Add(btnSizer, 0, wx.ALL, 4)
		# Translators: label of a button to close clipboard manager
		self.closeBtn = wx.Button(self, wx.ID_CLOSE, _("close"))
		btnSizer.AddButton(self.closeBtn)

		btnSizer.Realize()

		self.SetSizer(mainSizer)
		mainSizer.Fit(self)

		self.SetEscapeId(self.closeBtn.GetId())

		self.Layout()
		self.Centre()
		self.initTree()
		# binding tre events and list event to respective functions
		self.clipCategoryTree.Bind(wx.EVT_CONTEXT_MENU, self.onTreeContextMenu)
		self.clipCategoryTree.Bind(wx.EVT_TREE_KEY_DOWN, self.onTreeKeyPresses)
		self.Bind(
			wx.EVT_TREE_SEL_CHANGED,
			self.onTreeItemSelect, self.clipCategoryTree)
		self.clipCategoryTree.Bind(
			wx.EVT_TREE_END_LABEL_EDIT, self.onRenamedTreeItem)

		self.clipList.Bind(wx.EVT_CONTEXT_MENU, self.onListContextMenu)
		self.clipList.Bind(wx.EVT_KEY_UP, self.onListKeyUp)
		self.clipList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onActivatedListItem)
		self.clipList.Bind(
			wx.EVT_LIST_BEGIN_LABEL_EDIT,
			self.onListItemRenaming)
		self.clipList.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.onRenamedListItem)
		self.closeBtn.Bind(wx.EVT_BUTTON, self.close)
		self.clipList.SetFocus()
		item, cookie = self.clipCategoryTree.GetFirstChild(self.root)
		self.clipCategoryTree.SelectItem(item)

	def initTree(self):
		self.root = self.clipCategoryTree.AddRoot('root')
		self.TREE_ITEM_IDS = {}
		clips = initClipSfile()
		treeChildren = clips.keys()
		for child in treeChildren:
			treeId = self.clipCategoryTree.AppendItem(
				self.root, child, data=clips[child])
			self.TREE_ITEM_IDS[child] = treeId

	def onTreeContextMenu(self, evt):
		menus = wx.Menu()
		# Translators: label of menu item to create new category
		addCat = wx.MenuItem(menus, id=wx.ID_ANY, text=_("add category."))
		# Translators: label of a menu item to delete category
		delCat = wx.MenuItem(menus, id=wx.ID_ANY, text=_("delete category."))
		# Translators: label of a menu item to rename category
		renameCat = wx.MenuItem(menus, id=wx.ID_ANY, text=_("rename category."))
		menus.Append(addCat)
		menus.Append(delCat)
		menus.Append(renameCat)
		self.Bind(wx.EVT_MENU, self.addCategory, addCat)
		self.Bind(wx.EVT_MENU, self.renameTreeItem, renameCat)
		self.Bind(wx.EVT_MENU, self.deleteTreeItem, delCat)
		self.PopupMenu(menus, evt.GetPosition())
		evt.Skip()

	def onTreeKeyPresses(self, evt):
		keyCode = evt.GetKeyCode()
		if keyCode == wx.WXK_DELETE or keyCode == wx.WXK_NUMPAD_DELETE:
			self.deleteTreeItem(evt=None)
		elif keyCode == wx.WXK_F2:
			self.renameTreeItem(evt=None)
		evt.Skip()

	def onRenamedTreeItem(self, evt):
		if evt.Label in self.TREE_ITEM_IDS.keys():
			evt.Veto()
			gui.messageBox(
				# Translators: error message to be shown when can't rename the  category
				_("can't rename item. there is already an item with the same name."),
				# Translators: title of error dialog
				_("rename error!"))
			return False
		self.TREE_ITEM_IDS[evt.Label] = evt.Item

	def addCategory(self, evt):
		labelItem = self.editDialog(
			# Translators: title of a text entry dialog shown to create new category
			_("add category "),
			# Translators: label of an edit field shown to type new category name
			_("category name:"))
		if labelItem in self.TREE_ITEM_IDS.keys():
			gui.messageBox(
				# Translators: error message shown when can't add new category
				_("can't create category. there is already category with the same name."),
				# Translators: title of error dialog
				_("add error!"))
			return False
		addTreeId = self.clipCategoryTree.AppendItem(self.root, labelItem, data=[])
		self.TREE_ITEM_IDS[labelItem] = addTreeId

	def renameTreeItem(self, evt):
		selTreeItem = self.clipCategoryTree.FocusedItem
		self.clipCategoryTree.EditLabel(selTreeItem)

	def deleteTreeItem(self, evt):
		if self.TREE_ITEM_IDS[self.selCat] != []:
			self.TREE_ITEM_IDS.pop(self.selCat)
			self.clipCategoryTree.Delete(self.SelTreeItem)

	def onTreeItemSelect(self, evt):
		self.treeItemData = self.clipCategoryTree.GetItemData(evt.Item)
		self.selCat = self.clipCategoryTree.GetItemText(evt.Item)
		self.SelTreeItem = evt.Item
		self.clipList.DeleteAllItems()
		if self.treeItemData is None:
			return []
		for clip in self.treeItemData:
			self.clipList.Append([clip])
		item = self.clipList.GetTopItem()
		self.clipList.SetItemState(item, wx.LIST_STATE_FOCUSED, wx.LIST_STATE_FOCUSED)
		self.clipList.SetItemState(item, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

	def onListContextMenu(self, evt):
		menus = wx.Menu()
		addClip = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of menu item shown to create new clip
			text=_("add clip"))
		addFav = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of menu item to add selected clips to favourites
			text=_("add to favourite"))
		delClip = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of a menu item to delete selected clips
			text=_("delete clip"))
		cutClips = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of a menu item to cut clips
			text=_("cut clips CTRL + X"))
		copyClips = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of a menu item to copy clips
			text=_("copy clips CTRL + C"))
		pasteClips = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of a menu item paste clips
			text=_("Paste  clips CTRL + V"))
		selectAllClips = wx.MenuItem(
			menus, id=wx.ID_ANY,
			# Translators: label of a menu item to select all clips
			text=_("select all   clips CTRL + A"))
		menus.Append(addClip)
		menus.Append(delClip)
		menus.Append(addFav)
		menus.Append(cutClips)
		menus.Append(copyClips)
		menus.Append(pasteClips)
		menus.Append(selectAllClips)
		self.Bind(wx.EVT_MENU, self.addListItem, addClip)
		self.Bind(wx.EVT_MENU, self.deleteListItem, delClip)
		self.Bind(wx.EVT_MENU, self.addToFavourite, addFav)
		self.Bind(wx.EVT_MENU, self.cutListItem, cutClips)
		self.Bind(wx.EVT_MENU, self.copyListItem, copyClips)
		self.Bind(wx.EVT_MENU, self.pasteListItems, pasteClips)
		self.Bind(wx.EVT_MENU, self.selectAllListItem, selectAllClips)
		self.PopupMenu(menus, evt.GetPosition())

	def onListKeyUp(self, evt):
		keyCode = evt.GetKeyCode()
		if keyCode == wx.WXK_DELETE or keyCode == wx.WXK_NUMPAD_DELETE:
			self.deleteListItem(evt=None)
		elif keyCode == wx.WXK_F2:
			item = self.clipList.GetFirstSelected()
			self.clipList.EditLabel(item)
		elif keyCode == 65 and evt.ControlDown():
			self.selectAllListItem(evt=None)
		elif keyCode == 67 and evt.ControlDown():
			self.copyListItem(evt=None)
		elif keyCode == 88 and evt.ControlDown():
			self.cutListItem(evt=None)
		elif keyCode == 86 and evt.ControlDown():
			self.pasteListItems(evt=None)
		evt.Skip()

	def onListItemRenaming(self, evt):
		self.removeItem = evt.Index
		itemData = self.clipCategoryTree.GetItemData(
			self.clipCategoryTree.FocusedItem)
		itemData.pop(self.removeItem)

	def onRenamedListItem(self, evt):
		itemData = self.clipCategoryTree.GetItemData(
			self.clipCategoryTree.FocusedItem)
		labelItem = evt.Item.GetText()
		itemData.insert(self.removeItem, labelItem)

	def getClipListSelection(self) -> List:
		i = self.clipList.GetFirstSelected()
		clipsIndices = [i]
		while i >= 0:
			i = self.clipList.GetNextSelected(i)
			if i >= 0:
				clipsIndices.append(i)
		return clipsIndices

	def onActivatedListItem(self, evt):
		clipSelection = self.getClipListSelection()
		if clipSelection == [-1]:
			return False
		self.Hide()
		clip = self.clipList.GetItemText(self.clipList.FocusedItem)
		api.copyToClip(clip)
		paste = KeyboardInputGesture.fromName("control+v")
		paste.send()
		self.Close()
		evt.Skip()

	def addListItem(self, evt):
		itemLabel = self.editDialog(
			# Translators: title of edit dialog
			_("add a new clip"),
			# Translators: label of an edit field to type new clip text
			"clip: ")
		evt.Skip()
		currentIndex = self.clipList.FocusedItem
		if currentIndex < 0:
			currentIndex = 0
		self.clipList.InsertItem(currentIndex, itemLabel)
		self.treeItemData.insert(currentIndex, itemLabel)
		self.clipList.Refresh()

	def deleteListItem(self, evt):
		selClips = self.getClipListSelection()
		if self.treeItemData == [] or selClips == [-1]:
			gui.messageBox(
				# Translators: error message shown when no clips is selected
				_("no clip selected."),
				# Translators: title of error dialog
				_("delete error!"))
			return False
		selClips.reverse()
		for clip in selClips:
			self.clipList.DeleteItem(clip)
			self.treeItemData.pop(clip)
		ui.message(
			# Translators: message presented when clips are deleted
			_("clips deleted"))

	def cutListItem(self, evt):
		clipSelection = self.getClipListSelection()
		if clipSelection == [-1]:
			ui.message(
				# Translators: message presented when no clip selected to be copied
				_("no clip selected."))
			return False
		self.clipsToPaste = []
		clipSelection.reverse()
		for clip in clipSelection:
			self.clipsToPaste.append(self.treeItemData.pop(clip))
		ui.message(
			# Translators: message presented when clips are cut to clipboard
			_("cut clips to clipboard."))

	def copyListItem(self, evt):
		clipSelection = self.getClipListSelection()
		if clipSelection == [-1]:
			ui.message(
				# Translators: message presented when no clip is selected to be copied to clipboard
				_("no clip selected"))
			return False
		self.clipsToPaste = []
		clipSelection.reverse()
		for clip in clipSelection:
			self.clipsToPaste.append(self.treeItemData[clip])
		ui.message(
			# Translators: message presented when clips are copied to clipboard
			_("clips copied to clipboard"))

	def pasteListItems(self, evt):
		if not hasattr(self, 'clipsToPaste') or self.clipsToPaste == []:
			ui.message(
				# Translators: message presented when no clip is copied or cut
				_("no clip to paste."))
			return False
		for clip in self.clipsToPaste:
			self.treeItemData.append(clip)
			self.clipList.Append([clip])
		ui.message(
			# Translators: message presented when clip are pasted
			_("clip pasted."))

	def selectAllListItem(self, evt):
		item = self.clipList.GetTopItem()
		if self.clipList.ItemCount <= 0:
			ui.message(
				# Translators: message presented when no clips are available
				_("no clip available."))
			return False
		while item >= 0:
			item = self.clipList.GetNextItem(
				item, wx.LIST_NEXT_ALL,
				wx.LIST_STATE_DONTCARE)
			self.clipList.SetItemState(item, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		ui.message(
			# Translators: message presented when all clips are selected
			_("all clips selected."))

	def getTreeItems(self):
		treeItems: list = []
		rootItem = self.clipCategoryTree.GetRootItem()
		item, cookie = self.clipCategoryTree.GetFirstChild(rootItem)
		children = self.clipCategoryTree.GetChildrenCount(rootItem)
		i = 0

		while i < children:
			treeItems.append(self.clipCategoryTree.GetItemText(item))
			item = self.clipCategoryTree.GetNextSibling(item)
			i += 1
		return treeItems

	def editDialog(self, msg: str, title: str) -> str:
		with wx.TextEntryDialog(self, title, msg) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
		return d.Value

	def addToFavourite(self, evt):
		clips = self.getClipListSelection()
		favItemData = self.clipCategoryTree.GetItemData(
			self.TREE_ITEM_IDS['favourite'])
		for i in clips:
			favItemData.insert(0, self.treeItemData[i])

	def saveClips(self):
		self.clips = {}
		for treeLabel in self.TREE_ITEM_IDS.keys():
			self.clips[treeLabel] = self.clipCategoryTree.GetItemData(
				self.TREE_ITEM_IDS[treeLabel])
		writeClips(self.clips)

	def close(self, evt):
		self.saveClips()
		evt.Skip()
