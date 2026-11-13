class TestSenaryosu:
    def __init__(self, test_id, oncelik, sure, hazir):
        # aklıma gelmemişti-> aynı kimlik boşluklu veya boşluksuz yazıldığında bunun aynı kimliği kastettiği anlaşılmalı
        if type(test_id) is str:
            self.test_id = test_id.strip()
        else:
            self.test_id = test_id

        self.oncelik = oncelik
        self.sure = sure
        self.hazir = hazir
        self.sira_no = 0
        self.durum = None
        self.neden = ""

    def dogrula(self):
        # testin kendi verilerinin kurallara uyup uymadığının kontrolü
        if type(self.test_id) is not str or self.test_id == "":
            return False, "Gecersiz veya bos test kimligi"

        if type(self.hazir) is not bool:
            return False, "Hazirlik durumu True veya False olmali"

        if not self.hazir:
            return False, "Test hazir degil"

        if type(self.oncelik) is not int or not (1 <= self.oncelik <= 5):
            return False, f"Oncelik 1-5 arasinda tam sayi olmali (Girilen: {self.oncelik})"

        if type(self.sure) is not int or self.sure <= 0:
            return False, f"Sure pozitif tam sayi olmali (Girilen: {self.sure})"

        return True, "Gecerli ve hazir"