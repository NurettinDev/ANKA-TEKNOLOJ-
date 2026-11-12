def isUpperHigher(r, c, S, matrix):
  if r == 1:
      return -1
  if matrix[r-2][c-1] >= S:
      return 1
  else:
      return 0

class TelemetryPacket:
    #Raw paketlerin nesneye dönüştürülmesi 
    def __init__(self, packet_id: str, priority: int, size: int, is_verified: int):
        self.packet_id = packet_id
        self.priority = priority
        self.size = size
        self.is_verified = bool(is_verified)


class TelemetryScheduler:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.all_packages = []
        self.valid_packages = []
        self.unverified_ones = []
        self.too_big_ones = []

    def load_packages(self, raw_data: list):
        for item in raw_data:
            packet = TelemetryPacket(
                packet_id=item[0],
                priority=item[1],
                size=item[2],
                is_verified=item[3]
            )
            self.all_packages.append(packet)
    def filter_packages(self):
        #Ön Filtreleme doğrulanmamış ve kapasiteyi aşan paketleri ayırır ve reddeder)
        self.valid_packages = []
        self.unverified_ones = []
        self.too_big_ones = []

        for pkt in self.all_packages:
            if not pkt.is_verified:
                self.unverified_ones.append(pkt.packet_id)
            elif pkt.size > self.max_capacity:
                self.too_big_ones.append(pkt.packet_id)
            else:
                self.valid_packages.append(pkt)

    def optimize_and_schedule(self):
        # 1. Filtrelemeyi Çalıştır
        self.filter_packages()

        packages = self.valid_packages
        item_amount = len(packages)
        max_capacity = self.max_capacity
        self.matrix = [[0 for col in range(max_capacity)] for row in range(item_amount)]
        matrix = self.matrix
        for r in range(1, item_amount+1):
            for c in range(1, max_capacity+1):
                curr_pck = packages[r-1]
                temp_size1 = curr_pck.size
                temp_priority1 = curr_pck.priority
                size_dif = c - temp_size1

                if (size_dif) == 0:
                    if isUpperHigher(r, c, temp_priority1, matrix) == 1:
                        matrix[r-1][c-1] = matrix[r-2][c-1]
                    elif isUpperHigher(r, c, temp_priority1, matrix) == 0:
                        matrix[r-1][c-1] = temp_priority1
                    else:
                        matrix[r-1][c-1] = temp_priority1
                    continue
                elif (size_dif) > 0:
                    S=0
                    if r!=1:
                        S = temp_priority1 + matrix[r-2][ size_dif-1]
                    else:
                        matrix[r-1][c-1] = temp_priority1

                    if isUpperHigher(r, c, S, matrix) == 1:
                        matrix[r-1][c-1] = matrix[r-2][c-1]
                    elif isUpperHigher(r, c, S, matrix) == 0:
                        matrix[r-1][c-1] = S
                    continue    
                else:
                    if r == 1:
                        matrix[r-1][c-1] = 0
                    else:
                        matrix[r-1][c-1] = matrix[r-2][c-1]
                    continue
    def backtrack(self):
        used_size = 0
        packages = self.valid_packages
        item_amount = len(packages)
        unselected_items = []
        selected_items = []
        #Backtracking(geri izleme ve paketleri ortaya çıkarma)
        c = self.max_capacity
        matrix = self.matrix
        for r in range(item_amount, 0, -1):
            curr_pck = packages[r-1]
            if r==1:
                selected_items.append(curr_pck.packet_id)
                used_size += curr_pck.size
                continue
            if matrix[r-1][c-1] == matrix[r-2][c-1]:
                unselected_items.append(curr_pck.packet_id)
                continue
            else:
                selected_items.append(curr_pck.packet_id)
                used_size += curr_pck.size
                c = self.max_capacity-curr_pck.size
        print(f"Gönderilenler: {selected_items} | Bekleyenler: {unselected_items} | Reddedilenler: Büyük olduğu için {self.too_big_ones}, Doğrulanmadığı için {self.unverified_ones} | Gönderilen Boyut: {used_size} KB | Kalan: {self.max_capacity-used_size} KB")

if __name__ == "__main__":
    raw_packages = [
        ["P1", 5, 6, 1],
        ["P2", 4, 5, 1],
        ["P3", 3, 3, 1],
        ["P4", 2, 2, 0]
    ]

    # Karar motorunu başlat (Kapasite = 9)
    scheduler = TelemetryScheduler(max_capacity=9)
    
    # Verileri yükle ve algoritmayı çalıştır
    scheduler.load_packages(raw_packages)
    scheduler.optimize_and_schedule()
    scheduler.backtrack()
