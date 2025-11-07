# Pano İçerik Düzenleyicisi #
*	Yazarlar: Noelia ve Abdel.

Bu eklenti, panoya metin eklemek için kullanılır ve bu, metin bölümlerini yapıştırmaya hazır bir şekilde birleştirmek istediğinizde yararlı olabilir.
Pano içeriği ayrıca temizlenebilir ve göz atma modunda gösterilebilir.

## Klavye komutları ##
*	NVDA+windows+c: Seçilen metni, MathML nesnelerini temsil eden Unicode braille karakterlerini veya inceleme imleciyle işaretlenmiş dizeyi panoya ekler.
*	NVDA+Windows+X: Pano içeriğini temizler.
*	 Atanmamış: Panoya kopyalar (veya panodan keser), önceden onay istenme olasılığı ile.
*	 Atanmamış: Pano metnini tarama modunda HTML olarak gösterir. Pano boşsa ya da Windows Gezgini'nden kopyalanan dosyalar veya klasörler gibi tarama modunda görüntülenemeyen içeriklere sahipse bunu sesli olarak bildirir.
*	 Atanmamış: Metinsel pano içeriğini tarama kipi modunda düz metin olarak gösterir. Panonun boş olup olmadığını veya örneğin dosyalar ya da klasörler Windows Gezgini'nden kopyalanmışsa göz atılabilir bir iletide gösterilemeyen içeriğe sahip olup olmadığını bildirir.


## Pano İçerik Düzenleyicisi Ayarları ##

Bu panele NVDA menüsü tercihler alt menüsünden Ayarlar iletişim kutusuna girerek erişilebilir.

Aşağıdaki kontrolleri içerir:

* Panoya eklenen içerikler arasında ayraç olarak kullanılacak metni yazın: Eklenen metnin tamamı yapıştırıldıktan sonra metin bölümlerini bulmak için kullanılabilecek bir ayırıcı ayarlamayı sağlar.
* Metni panodaki verilerden önce ekle: Eklenen metnin sona mı yoksa başa mı ekleneceğini seçmek de mümkündür.
* Önceden onay gerektiren eylemleri seçin: Mevcut her eylem için hemen mi yoksa onaydan sonra mı gerçekleştirileceğini seçebilirsiniz. Kullanılabilir eylemler şunlardır: metin ekle, panoyu temizle, kopyalamayı taklit et ve kesmeyi taklit et.
* Şu durumlarda seçili eylemleri gerçekleştirmeden önce onay iste: Yalnızca panoda metin varsa veya pano boş değilse (örneğin metin değil de bir dosya kopyaladıysanız) onayın her zaman istenip istenmeyeceğini seçebilirsiniz.
* Pano metnini tarama modunda HTML olarak gösterecek şekilde biçimlendirin: HTML biçimlendirme dili öğreniyorsanız, HTML kodunuzun NVDA tarafından bir tarayıcıda nasıl oluşturulacağı hakkında bir fikir sahibi olmak için HTML veya bir web tarayıcısında gösterildiği gibi HTML'de Önceden Biçimlendirilmiş metin'i seçebilirsiniz. Önceden biçimlendirilmiş ve geleneksel HTML arasındaki fark, ilk seçeneğin ardışık boşlukları ve satır sonlarını koruması, ikincisinin ise bunları sıkıştırmasıdır. Örneğin, h1, h2, li, pre vb. gibi bazı HTML etiketleri yazın, metni seçip panoya kopyalayın ve metni göz atılabilir bir mesajda göstermek için clipContentsDesigner eklentisini kullanın.
* Pano metnini Tarama kipi modunda gösterirken maksimum karakter sayısı: Pano büyük metin dizeleri içeriyorsa, bu sınırı artırmanın sorunlara yol açabileceğini lütfen unutmayın. Varsayılan sınır 100000 karakterdir.
* Varsayılanları geri yükle.

Notlar:

*	Eğer NVDA'nın bir mesaj kutusu hala açıksa bir işlem için onay istenmeyecektir. Bu gibi durumlarda, işlemler derhal gerçekleştirilecektir.
* Kopyalayı taklit et ve kesme komutlarını taklit et, bu özellikler etkinleştirildiğinde, eklentinin kontrol+c ve control+x kontrolünü ele alacağı anlamına gelir. Bu, bu tuş vuruşlarına karşılık gelen eylemleri gerçekleştirmeden önce bir onay istenip verilmeyeceğini seçecektir.

## 46.0.0 için Değişiklikler
* NVDA, göz atılabilir iletilerdeki HTML'yi sterilize edecektir.
* Göz atılabilir mesajları kapatmak için Escape tuşuna ek olarak bir düğme eklendi.


## 40.0.0 için Değişiklikler
* İbranice klavye için destek eklendi.

## 22.0.0 için Değişiklikler
* Eklenti ayarları panelinde varsayılanları geri yüklemek için bir düğme eklendi.
* Eklenti güvenli modda çalıştırılamaz.

## 17.0 için Değişiklikler
* NVDA 2023.1 ile uyumlu.

## 16.0 için Değişiklikler
* NVDA 2022.1 veya sonraki bir sürümü gerektirir.

## 15.0 için Değişiklikler
* Panoya metin ekleme komutu, girdi hareketleri iletişim kutusuna tekrar eklendi.
* Mohammadhosein Ghezelsofla sayesinde Farsça klavyeyle kopyalama ve kesme hareketleri düzeltildi.

## 14.0 için Değişiklikler
* NVDA 2021.1 ile uyumlu.

## 13.0 için Değişiklikler
* Ayarlar panelinin görsel düzenindeki bir sorun düzeltildi, teşekkürler Cyrille Bougot.
* Dokümantasyon (yardım dosyaları) geliştirildi.
* Eklenti için kullanılabilen tüm komutlara girdi hareketleri atamak için bir Pano İçerik Düzenleyicisi kategorisi eklendi.
* Tarayıcılarda odak modu etkinken Kopyalamayı taklit et kullanıldığında yaşanan hatalar düzeltildi.
* Pano metin içeriklerini ham metin veya HTML şeklinde biçimlendirilmiş olarak göstermek için farklı hareketler atayabilirsiniz. Ayarlar panelinde pano metnini gösterecek biçim, HTML biçimi için mevcut iki seçeneği seçmek üzere düzenlendi.

## 12.0 için Değişiklikler
* LibreOffice Writer gibi uygulamalarda Kopyalamayı taklit et kullanırken oluşan hatalar düzeltildi.

## 11.0 için Değişiklikler
* Artık NVDA'nın standart komutlarını (NVDA+f9 ve NVDA+f10) kullanarak inceleme imleciyle işaretlenmiş metni eklemek mümkündür. Yeni NVDA+shift+f9 komutuyla daha iyi bir entegrasyon için NVDA+windows+f9 artık kullanılmamaktadır.
* NVDA 2019.3 veya sonraki bir sürümü gerektirir.

## 10.0 için Değişiklikler
* Başlık latin olmayan karakterler içerdiğinde pano metnini göstermek için kullanılan iletişim kutusundaki bir hata düzeltildi.
* Arapça klavye düzeniyle Kesmeyi taklit et ve Kopyalamayı taklit et özelliklerini kullanırken oluşan bir hata düzeltildi. Bu, Abdel tarafından düzeltildi, eklenti yazar olarak eklendi.

## 9.0 için Değişiklikler

* Pano metnini tarama kipi modunda gösterme özelliği eklendi.
* Dosyalar veya klasörler kopyalanmışsa, pano boş değilse onayın gerekli olup olmayacağını seçmek için bir seçenek eklendi.
* NVDA 2018.4 veya sonraki bir sürümü gerektirir.

## 8.0 için Değişiklikler ##

* Eklenti ayarları, NVDA Ayarları iletişim kutusunun ilgili kategorisinde gösterilir.
* NVDA 2018.2 veya sonraki bir sürümü gerektirir.

## 7.0 için Değişiklikler

* Kurulum sırasında yapılandırma iletişim kutusunda hayır'ı seçerseniz, Kesmeyi taklit et ve Kopyalamayı taklit et özeliklerine ilişkin komutlar kaldırılır, böylece kontrol+c ve kontrol+x için normal davranışı geri yükleyebilirsiniz.

## 6.0 için Değişiklikler

*	 Onaydan sonra mevcut eylemlerin gerçekleştirilip gerçekleştirilmeyeceğini seçmek için seçenekler eklendi.
*	Girdi hareketleri iletişim kutusundan atanabilen Kopyalamayı taklit et ve Kesmeyi taklit et komutları eklendi.
*	 Yükleme sırasında Kopyalamayı taklit et ve Kesmeyi taklit et işlevlerini yapılandırmak için bir iletişim kutusu eklendi. Bu, kopyalamak ve kesmek için control+c ve control+x komutlarının eklenmesine ve bu tuş vuruşlarına basıldığında pano içeriğini değiştirmek isteyip istemediğinizin sorulmasına olanak tanır.
*	Belgeler script_add (Windows+NVDA+c) için düzeltildi.

## 5.0 için Değişiklikler ##

*	Diyaloğun görsel sunumu, NVDA'da gösterilen diyalogların görünümüne bağlı kalarak geliştirildi.
*	NVDA 2016.4 veya sonraki bir sürümü gerektirir.

## 4.0 için Değişiklikler ##
*	Eklenti ayarları NVDA konfigürasyonundan yönetilir, böylece farklı ayraçları kaydetmek için standart profiller kullanılabilir ve yeniden kurulum sırasında içe aktarma için ayarların kopyalanması gerekmez.
*	Artık, Pano İçerik düzenleyicisi ayarları iletişim kutusundaki metni pano verilerinden önce ekle onay kutusunu kullanarak, eklenecek metnin başa mı yoksa sona mı ekleneceğini seçmek mümkündür.

## 3.0 için Değişiklikler ##
*	MathPlayer kuruluysa, MathML nesnelerinin Braille gösterimi panoya eklenebilir.
*	Ayraç ayarlanmazsa, eklenen metin bölümleri arasına yalnızca tek bir satır yerleştirilir.
*	Pano İçerik Düzenleyicisi ayarları iletişim kutusunu açmak için bir kısayol atanabilir.
*	Eklentiyi yeniden yüklerken içe aktarılmak üzere ayırıcının kopyalanıp kopyalanmayacağını seçmek için ayarlar iletişim kutusuna bir onay kutusu eklendi.

## 2.0 için Değişiklikler ##
*	Hintçe karakterler, eklenen içerikler arasında ayraç olarak kullanılabilir.

## 1.0 için Değişiklikler ##
*	İlk sürüm.
