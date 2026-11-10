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

Buradaki matriste satırlar nesne(item)'ları gösterir ve 

