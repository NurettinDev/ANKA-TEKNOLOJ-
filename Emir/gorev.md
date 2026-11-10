# Kodun/Algoritmanın anlatımı
Bu aslında bilgisayar bilimlerindeki klasik knapsack problemidir. Bu problemi çözmenin birkaç yolu vardır örneğin akla ilk gelen tüm kombinasyonları denemek olabilir
fakat bu yöntem(bazen budama yöntemi de denir.) $O(2^n)$ karmaşıklığına sahiptir. Bu bilgisayar biliminde girişlerin ne kadar işlem aşamasından geçtiğini göstermek için kullanılan bir semboldür. $O(2^n)$ karmaşıklığa sahip bir algoritma $n$ girdi aldığında $2^n$ tane işlem gerçekleştirir. Bundan çok daha hızlı olan diğer bir algoritma dynamic programming yöntemini kullanan knapsack algoritmasıdır ve bu yöntem: $C$ kapasite, $N$ ise nesne sayısı olarak gösterirsek $O(C*N)$ karmaşıklığına sahip olur. Bu eksponansiyel karmaşıklıktan pseudo-polinomal karmaşıklığa geçiş demektir ve çok daha hızlıdır. Görevde verilen telemetri paketleri bu problem ile rahatça modellenilebilir ve istenen program oluşturulabilir. 

Knapsack probleminde matematiksel formülasyon şu şekilde olur:
Öncelikle maksimize edilmek istenen belirli bir fonksiyon değeri olur bu bizim durumumuzda iletilecek paketlerin toplam önceliğidir buna objective function denir.
$x_{i}$ 0 veya 1 değeri alan ve i'ninci nesnenin iletilip iletilmeyeceğini söyler eğer iletilecekse 1 olur ve toplama eklenir eğer iletilmeyecekse öncelik ne olursa olsun 0 ile çarpıldığından dolayı toplama katkıda bulunmaz. 

$$
Z = \sum_{i=1}^{n} x_{i}P_{i}
$$

Bunun yanı sıra bir de sınırlandırmamız vardır bu da kapasitenin aşılmaması için gereklidir

$$
C \ge \sum_{i=1}^{n} x_{i}P_{i}
$$

Görevde belirtildiği üzere başka koşullarımız da vardır ancak bir knapsack problemi genel olarak bu temel bilgilerle modellenmektedir kodun içerisinde bu durumlar da hesaba katılacak çeşitli şekillerde modellenecek ve istenen program gerçeklenecektir. 

Algoritma önce filtreleme yapar eğer belirli bir paket tek başına azami kapasiteyi aşıyorsa o zaman direkt olarak reddedilir(örneğin kapasite 9KB iken belirli bir P1 paketi 11KB ise doğrudan reddedilir.) eğer paket doğrulanmamış ise yine doğrudan reddedilir ve ilgili reddedilmiş paketleri taşıyan listelere paket eklenir ve iletilme potansiyeli olan ana paketler listesinden atılır. Daha sonra bu ana paketler listesi(kısacası ana paket listesi olarak APL diyelim), içerisinde Dynamic Programming algoritması kullanılır. Bu algoritmanın anlatımı oldukça uzundur ve Bilgisayar Mühendisliği/Computer Science bölümünde Data Structures and Algorithms dersinde işlenmektedir(algoritmanın anlatılması özellikle istenirse uzunca anlatabilirim) fakat kısaca özetlemek gerekirse DP matrix adı verilen önce 2 boyutlu bir tablo oluşturulur:

<img width="550" height="388" alt="image" src="https://github.com/user-attachments/assets/236e8890-10d1-46f8-a98d-f7716d195ab7" />

Buradaki matriste satırlar nesne(item)'ları gösterir, sütunlar ise $C$'den 1'e kadar tüm mümkün kapasite durumlarını modeller. Her bir kutu temelde ilgili sütundaki kadar bir boş kapasitemiz var iken o satırdaki nesne ile o nesneyi koyduğumuzda kalan kapasiteye en son neyin eklendiği bilgisi üzerinden bir toplama yapıp en çok puan alan yani bizim durumumuzda en çok önceliği olan durumu bulup kutunun içine onu yazar.
Örneğin 2. paketin büyüklüğü 5KB ise ancak biz 6KB kapasitelik bir sütundaysak 1 KB'lık kapasiteye bu 2. paketin hiç hesaba katılmadığı zamandaki(ki bu en çok 1. satır olabilmektedir) elde edilen toplam öncelik değeri ile bir toplama yapılır ancak eğer ki bu kapasite sütunundaki yani 6KB sütununda başka bir üstteki yani 2. itemın hesaba katılmadığı fakat 6KB'lık kapasiteye doldurulabilmiş daha büyük bir öncelik var ise bu kutunun içine o puan yazılır. Bu şekilde tablo tamamen doldurulur. Daha sonrasında elde edilen tabloya veya DP matrisine backtracking adı verilen yani geriye doğru izleme adı verilen başka bir algoritma kullanılır bu algoritma son satır ve son sütundan başlayarak(bunun nedeni son sütun son satırın en yüksek öncelik puanına sahip olmasıdır ve zaten istediğimiz şey de maksimum öncelik kombinasyonunu veren listeyi bulmaktır) satır sayısını azaltarak hangi satırda bir değişiklik olduğunu hesaba katmaya çalışır örneğin eğer son sütundaki kapasite değerimiz 9KB ise ve 4. item'dan 3. item'a geçerken ilgili öncelik puanı değişiyorsa bunun anlamı 4. item'a geçildiğinde kapasiteye bunun bir etkisinin olduğu anlamına gelir bu da 4. item'ın aslında seçildiğini gösterir. Daha sonrasında geri izlemeye 3. itemdan devam edilir ve 3. item ya da daha altı dahil mi bu aranmaya başlanır, sütun ise $C$ kapasite boyutundan 4. item'ın boyutu çıkarıldığında kalan boyutta ne olup bittiğini anlamak için C-4. item'ın kapasitesi = kalan kapasite olacak şekilde sütun değiştirilir bu sayede kalan kapasiteye 3. veya daha küçük indeksli elemanlardan birisinin yine en baştakindeki gibi üst üste puanları aynı sütunda eşit olup olmadığına bakılarak etkiler gözlemlenir ve etkisi olan paketler bir bir 0. indekse kadar gidilerek eklenir. İşte bu şekilde seçilen paketler tablodan çıkarılır. Bu algoritma bahsedilen tüm kombinasyonları bulmayı içeren algoritmalardan çok daha hızlıdır ve daha az bellek kullanır.
Son kısımda toplanılan bilgiler yazılır. Ayrıca aynı önceliğe sahip kombinasyonlarda özellikle ilk önce gelen paketin gönderilmesi durumu da kodda mevcuttur, bilinçli olarak en küçük indeksliler önce konan paket olarak ayarlanmıştır ve daha büyük indeksli paketin sonradan geldiği varsayılmıştır. DP matrisinde en alttan(yani en büyük satır numarasından) üste doğru gidildiği için ve üst üste iki eşit olan kombinasyon seçilmediği için önceliği farklı olan ancak eğer ki aynıysa da ilk önce gelenin seçilmesi söz konusudur. Algoritma buna göre kodda implemente edilmiştir. Satır satır açıklama istenirse yapılabilir.  



