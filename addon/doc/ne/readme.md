# क्लिप सामाग्री नमुनाकार #
*   लेखकहरू: नोलिया रुइज्
*   [स्थीर संस्करण][1] को अनुबहन
*   [विकास संस्करण][2] को अनुबहन

क्लिपपाटीमा पाठहरुलाई थप गर्न यो उप-कर्मीको   प्रयोग गरिन्छ जसमा सबै
पाठहरुलाई एक आपसमा जोडेर टाँस्न सकिन्छ । यस्ता सामाग्रीलाई मेटाउन पनि
सकिन्छ ।

## कुञ्जीपाटी आदेश ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   नेत्रवाणी+windows+x: क्लिपमा रहेका सामाग्रिलाई मेटाउ ।
*   नेत्रवाणी+windows+f9: समिक्षा क्रसरको हालको स्थानलाई क्लिपपाटिमा थप
    गरिने पाठको सुरु विन्दुको रुपमा कायम गर । यदि तपाइले नेत्रवाणी+F9 दबाउनु
    भयो भने, त्यो पाठ  क्लिपपाटिमा थपिने छैन । 

टिप्पणी: उपरोक्त आदेशहरूलाई नेत्रवाणी मेनु, प्राथमिकताहरू उप-मेनु,लगानी
सङ्केत पातोमा  रहेको पाठ समिक्षा वर्गीकरणमा गएर परिवर्तन गर्न सकिन्छ ।

## प्राथमिकता मेनु ##
*   Clip Contents Designer settings: Allows to set a separator which can be
    used to find the text segments once the entire appended text is
    pasted. You can also choose if the separator should be copied to your
    personal NVDA's configuration folder, so that it can be imported when
    reinstalling the add-on.

Note: The above command can be changed from NVDA menu, Preferences submenu,
Input gestures dialog, Configuration category.

## Changes for 3.0 ##
*   Braille representation of MathML objects can be appended to the
    clipboard if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    appended text segments.
*   A shortcut can be assigned to open the Clip Contents Designer settings
    dialog.
*   Added a check box in the settings dialog, for choosing if the separator
    should be copied to be imported when reinstalling the add-on.

## २.० संस्करणमा गरिएका परिवर्तनहरू ##
*   थप गरिएका पाठहरुको विचमा देवनागरि वर्णहरुलाई पनि प्रयोग गर्न सकिन्छ ।

## १.० मा गरिएका परिवर्तनहरू ##
*   सुरुको संस्करण

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
