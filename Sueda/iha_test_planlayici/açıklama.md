
                                               ALGORİTMANIN İŞLEYİŞİ
- Sisteme eklenen her testin ID'sindeki boşluklar temizlenir ve teste eklenme sırasını tutan bir sıra numarası verilir.
- Aynı ID'ye sahip bir test tekrar eklenirse ilk kayda dokunulmaz ve ikinci gelen kayıt doğrudan reddedilen listesine atılır.
- Tekrar etmeyen testler dogrula() metoduyla kontrol edilir.Hazır olmayan, önceliği 1-5 dışında kalan veya süresi pozitif olmayan testler elenir.
- Geçerli testler önce öncelik puanına göre ama öncelikleri eşitse sisteme eklenme sırasına göre sıralanır.
- Sıralanan testlerden kalan süreye sığanlar planlanan listesine alınıp süreleri bütçeden düşülür.Sığmayanlar da bekleyen listesine alınır ama döngü sonraki kısa testler için devam eder.
- İşlem sonunda her test yalnızca tek bir grupta (planlanan,bekleyen,reddedilen) yer alır ve sonuçlar nedenleriyle birlikte ekrana yazdırılır.