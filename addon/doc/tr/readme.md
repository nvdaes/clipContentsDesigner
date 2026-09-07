# Pano İçerik Düzenleyicisi #
*	Yazarlar: Noelia, Abdel.

Bu eklenti panoya metin eklemek için kullanılır; bu, metin bölümlerini yapıştırmaya hazır bir şekilde birleştirmek istediğinizde yararlı olabilir.
Pano içeriği de temizlenebilir ve Tarama Kipi gösterilebilir.

## Klavye komutları ##
*	NVDA+windows+c: Seçilen metni, MathML nesnelerini temsil eden Unicode braille karakterlerini veya inceleme imleciyle işaretlenen dizeyi panoya ekler.
*	NVDA+windows+x: Pano içeriğini temizler.
*	 Atanmamış: Daha önce onay istenme olasılığıyla birlikte panoya kopyalar (veya panodan keser).
*	 Atanmamış: Pano metnini Tarama Kipinde HTML olarak gösterir veya panonun boş olup olmadığını veya göz atılabilir bir mesajda sunulamayan içeriğe sahip olup olmadığını (örneğin, dosyalar veya klasörler Windows Gezgini'nden kopyalanmışsa) duyurur.
*	 Atanmamış: Tarama Kipinde panonun metinsel içeriğini düz metin olarak gösterir veya pano boşsa ya da göz atılabilir bir mesajda gösterilemeyen içeriğe sahipse (örneğin, Windows Gezgini'nden dosya veya klasör kopyalanıyorsa) bunu bildirir.


## Pano İçerik Düzenleyicisi ayarları ##

Bu panele NVDA menüsü, Tercihler alt menüsü, Ayarlar iletişim kutusundan erişilebilir.

Aşağıdaki kontrolleri içerir:

* Panoya eklenen içerikler arasında ayırıcı olarak kullanılacak dizeyi yazın: Eklenen metnin tamamı yapıştırıldıktan sonra metin bölümlerini bulmak için kullanılabilecek bir ayırıcı ayarlamanıza olanak tanır.
* Pano içeriğinden önce metin ekleme: Eklenen metnin sonuna mı yoksa başına mı ekleneceğini de seçebilirsiniz.
* Önceden onay gerektiren eylemleri seçin: Mevcut her eylem için, hemen mi yoksa onaylandıktan sonra mı gerçekleştirileceğini seçebilirsiniz. Kullanılabilir eylemler şunlardır: metin ekleme, panoyu temizleme, kopyalamayı taklit etme ve kesmeyi taklit etme.
* Şu durumlarda, seçilen eylemleri gerçekleştirmeden önce onay iste: Onayların her zaman, yalnızca panoda metin varsa veya pano boş değilse (örneğin, metni değil bir dosyayı kopyaladıysanız) istenip istenmeyeceğini seçebilirsiniz.
* Pano metnini Tarama Kipinde HTML olarak gösterecek şekilde biçimlendirin: HTML biçimlendirme dilini öğreniyorsanız, HTML kodunuzun bir tarayıcıda NVDA tarafından nasıl oluşturulacağı hakkında fikir sahibi olmak için HTML'de veya web tarayıcısında gösterildiği gibi önceden biçimlendirilmiş metni seçebilirsiniz. Önceden biçimlendirilmiş HTML ile geleneksel HTML arasındaki fark, ilk seçeneğin ardışık boşlukları ve satır sonlarını koruması, ikincisinin ise bunları sıkıştırmasıdır.  Örneğin, h1, h2, li, pre vb. gibi bazı HTML etiketleri yazın, metni seçip panoya kopyalayın ve metni göz atılabilir bir mesajda göstermek için Pano İçerik Düzenleyicisi eklentisini kullanın.
* Pano metnini Tarama Kipinde gösterirken maksimum karakter sayısı: Lütfen, panonun büyük metin dizeleri içermesi durumunda bu sınırı artırmanın sorunlara yol açabileceğini unutmayın. Varsayılan sınır 100000 karakterdir.
* Güncellerken yapılandırma iletişim kutusunu göster: Eklentiyi güncellerken kopyala ve kes öykünmesini yapılandırmak için bir iletişim kutusu görmek istemiyorsanız bu seçeneğin işaretini kaldırın.
* Varsayılanları geri yükle.

Notlar:

*	NVDA'nın mesaj kutusu hala açıkken onay istenmeyecektir. Bu durumda gerekli işlemler anında yapılacaktır.
* Kopyalamayı taklit et ve kesmeyi taklit et komutları, bu özellikler etkinleştirildiğinde eklentinin kontrol+c ve kontrol+x'in kontrolünü ele alacağı anlamına gelir. Bu, bu tuş vuruşlarına karşılık gelen eylemleri gerçekleştirmeden önce bir onay istenip istenmeyeceğinin seçilmesine olanak tanır.


## 49.0.0 için değişiklikler
* Eklenti güncellendiğinde bir yapılandırma iletişim kutusunun gösterilip gösterilmeyeceğine karar vermek için bir onay kutusu eklendi.


## 46.0.0 için değişiklikler
* NVDA, görüntülenebilir mesajlardaki HTML'yi temizleyecektir.
* Escape tuşuna ek olarak göz atılabilir mesajları kapatmak için bir düğme eklendi.


## 40.0.0 için değişiklikler
* İbranice klavye için destek eklendi.

## 22.0.0 için değişiklikler
* Eklenti ayarları paneline varsayılanları geri yüklemek için bir düğme eklendi.
* Eklenti güvenli modda çalıştırılamaz.

## 17.0 için değişiklikler
* NVDA 2023.1 ile uyumludur.

## 16.0 için değişiklikler
* NVDA 2022.1 veya sonrası sürümleri gerektirir.

## 15.0 için değişiklikler
* Panoya metin ekleme komutu yine girdi hareketleri iletişim kutusunda sunulur.
* Mohammadhosein Ghezelsofla sayesinde Farsça klavyeyle kopyalama ve kesme hareketleri düzeltildi.

## 14.0 için değişiklikler
* NVDA 2021.1 ile uyumludur.

## 13.0 için değişiklikler
* Cyrille Bougot sayesinde ayarlar panelinin görsel düzenindeki sorun düzeltildi.
* Belgeler iyileştirildi.
* Bu eklenti için, mevcut tüm komutlara hareket atayabilmek için Girdi Hareketleri iletişim kutusuna Pano İçerik Düzenleyicisi kategorisi eklendi.
* Odak kipi etkin olduğunda tarayıcılarda kopyalama Taklidi kullanılırken oluşan hatalar düzeltildi.
* Pano metin içeriğini ham metin olarak veya HTML olarak biçimlendirilmiş olarak göstermek için farklı hareketler atayabilirsiniz. Ayarlar panelinde pano metnini gösterme Biçimi, HTML biçimi için mevcut iki seçeneği belirleyecek şekilde buna göre değiştirildi.

## 12.0 için değişiklikler
* LibreOffice Writer gibi uygulamalarda kopyalama taklidi kullanılırken oluşan hatalar düzeltildi.

## 11.0 için değişiklikler
* Artık NVDA'nın standart komutlarını (NVDA+f9 ve NVDA+f10) kullanarak inceleme imleciyle işaretlenen metni eklemek mümkün. Yeni NVDA+shift+f9 komutuyla daha iyi entegrasyon sağlamak amacıyla NVDA+windows+f9 artık kullanılmamaktadır.
* NVDA 2019.3 veya sonrası sürümleri gerektirir.

## 10.0 için değişiklikler
* Başlığı Latin olmayan karakterler içerdiğinde pano metnini göstermek için kullanılan iletişim kutusundaki bir hata düzeltildi.
* Arapça klavye düzeniyle kesme ve kopyalama özelliklerini taklit ederken oluşan bir hata düzeltildi. Bu hata, eklenti yazarı olarak eklenen Abdel tarafından giderildi.

## 9.0 için değişiklikler

* Pano metnini Tarama Kipinde gösterme olanağı eklendi.
* Pano boş değilse, örneğin dosyalar veya klasörler kopyalanmışsa, onayların gerekip gerekmeyeceğini seçme seçeneği eklendi.
* NVDA 2018.4 veya sonrası sürümleri gerektirir.

## 8.0 için değişiklikler ##

* Eklenti ayarları, NVDA Ayarları iletişim kutusunun ilgili kategorisinde gösterilir.
* NVDA 2018.2 veya sonrası sürümleri gerektirir.

## 7.0 için değişiklikler

* Kurulum sırasında "Kopyala" ve "Kes" işlevlerini yapılandırmak için kullanılan iletişim kutusunda "Hayır" seçeneğini seçerseniz, bu özelliklere ait komutlar kaldırılır ve böylece Ctrl+C ve Ctrl+X için normal davranış geri yüklenir.

## 6.0 için değişiklikler

*	 Onaydan sonra mevcut eylemlerin gerçekleştirilip gerçekleştirilmeyeceğini seçmek için seçenekler eklendi.
*	GirDi hareketleri iletişim kutusundan atanabilen "Kopyala" ve "Kes" komutlarını taklit et özelliği eklendi.
*	 Kurulum sırasında Taklit kopyalama ve Taklit kesme işlevlerini yapılandırmak için bir iletişim kutusu eklendi. Bu, kopyalamak ve kesmek için control+c ve control+x komutlarını eklemenize ve bu tuş vuruşlarına bastığınızda pano içeriğini değiştirmek isteyip istemediğinizin sorulmasına olanak tanır.
*	Script_add (Windows+NVDA+c) için Belgeler düzeltildi.

## 5.0 için değişiklikler ##

*	Diyalogların görsel sunumu, NVDA'da gösterilen diyalogların görünümüne uygun olarak geliştirilmiştir.
*	NVDA 2016.4 veya sonrası sürümleri gerektirir.

## 4.0 için değişiklikler ##
*	Eklenti ayarları NVDA konfigürasyonundan yönetilir, böylece farklı ayırıcıları kaydetmek için standart profiller kullanılabilir ve yeniden kurulum sırasında içe aktarmak için ayarların kopyalanmasına gerek kalmaz.
*	Artık, Pano İçerik Düzenleyicisi ayarları iletişim kutusundaki Pano İçeriğinden önce metin ekle onay kutusunu kullanarak, eklenen metnin ekleneceği mi yoksa başına mı ekleneceğini seçmek mümkün.

## 3.0 için değişiklikler ##
*	MathPlayer kuruluysa, MathML nesnelerinin Braille gösterimi panoya eklenebilir.
*	Ayırıcı ayarlanmadıysa eklenen metin bölümleri arasına yalnızca tek bir satır yerleştirilecektir.
*	Pano İçerik Düzenleyicisi ayarları iletişim kutusunu açmak için bir kısayol atanabilir.
*	Eklentiyi yeniden yüklerken ayırıcının içe aktarılmak üzere kopyalanıp kopyalanmayacağını seçmek için ayarlar iletişim kutusuna bir onay kutusu eklendi.

## 2.0 için değişiklikler ##
*	Hintçe karakterler eklenen içerikler arasında ayırıcı olarak kullanılabilir.

## 1.0 için değişiklikler ##
*	İlk sürüm.
