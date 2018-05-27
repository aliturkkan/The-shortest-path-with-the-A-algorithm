# 1. AMAÇ

Bu web arayüzü ile *Ankara-Gaziantep* ve *Ankara-Mersin* şehirleri arasındaki en kısa mesafe bulunması amaçlanmaktadır. Bu amaç kapsamında yapay zekâ algoritmalarından olan A* algoritması kullanılacaktır. Algoritma hakkında bilgi, __A* Algoritması__ başlığı altında detaylı olarak anlatılacaktır. Günümüzde sıkça kullanılan google haritalar uygulaması üzerinden de veriler görselleştirilerek gerçek uzaklıklar ve rota hakkında doğrulama görselleştirilecektir. Görselleştirme işlemi ise python web kütüphanesi olan django ile yapılacaktır. 
Bu uygulama ile belirlenen şehirlere en kısa mesafeden nasıl gidileceği belirlenmiş olacaktır. Bu sayede şehirler arasında yolculuk yapacak olan insanlar bu uygulama ile daha kısa sürede istedikleri şehre gidebilecekler.

# 2. A* Algoritması

## 2.1.A* Algoritması Nedir?

A* algoritması, iki düğüm arasındaki en kısa yolu bulmak için kullanılan bir algoritmadır. Bu en kısa yolu bulurken üç değeri göz önünde bulundurmaktadır. Bunlar;

•	Bulunulan düğüm ile bitiş düğümü arasındaki kuş bakışı uzaklık,

•	Bulunulan düğüm ile gidilecek düğüm arasındaki gerçek uzaklık,

•	Bulunulan düğüme gelirken gidilen gerçek uzaklık.


Bu elde edilen üç değer ile A* algoritmasının bulduğu en kısa yol elde edilmiş olunur.

## 2.2. A* Algoritması Nasıl Çalışır?

A* algoritması hesaplanırken, başlangıç düğümü dahil tüm düğümlerin varış düğümüne olan kuş bakışı uzaklıkları hesaplanır. Bu uzaklıklara sezgisel uzaklık adı verilir. Daha sonra başlangıç düğümünden gidilebilecek düğümler ele alınır. Ele alınan bu düğümlerin varış düğümüne kuş bakışı uzaklığı ve başlangıç düğümüne olan gerçek uzaklığı toplanarak maliyetleri bulunur. Maliyeti en düşük olan yol bir sonraki düğüm olarak seçilir. Bu işleme varış düğümüne ulaşılana kadar devam edilir. 
Bir ayrıntı olarak hesaplanan maliyetlerde o düğüme gelene kadar harcanan gerçek yol değerleri mutlaka olmalıdır. Örneğin hesaplamanın 4. adımına ulaşan bir maliyet, ilk 3 adım için harcanan gerçek yol değerlerini içermelidir.

## 2.3. A* Algoritması Nerelerde Kullanılır?

A* algoritması genel olarak en kısa yolun bulunmasında kullanılır. Bu en kısa yol bulma işlemi bazen bir oyunda karakterin gideceği yeri hesaplarken, bazense bir cihaza bilmediği bir yol için en kısa zamanda hedefe nasıl ulaşması gerektiğini söyletmek için kullanılır. Örnek olarak Warcraft3 oyununda kullanıcı kontrolü dışındaki karakterler bu algoritma ile yolunu bulmaktadırlar.

## 2.4. A* Algoritması Avantajları

•	Diğer arama algoritmalarından farklı olarak sezgisel ve gerçek değerin karışımı bir maliyet hesapladığı için gerçeğe daha yakındır,

•	Düğüm genişletilerek alınan verim diğer arama algoritmalarına kıyasla en fazladır,

•	En optimal değeri verir,

•	Bulduğu ilk düğüm hedef düğümdür.


## 2.5. A* Algoritması Dezavantajları

•	Her adımın sabit bir maliyeti varsa çalışmaz,

•	Bazı problemlerde karmaşıklık ortaya çıkarabilir.




