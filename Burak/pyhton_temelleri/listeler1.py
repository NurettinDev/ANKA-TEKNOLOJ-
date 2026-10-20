
"""
ogrenci_listesi={100:
                 {"Name":"Ajdar",
                  "Telfon No":123123
                  }}
"""
list = {}
i=0
while(i<3):
    i+=1 
    number =input("Öğrenci Numaranızı Giriniz : ")
    name= input("Adınızı Giriniz : ")
    phone=input("Telefon Numaranızı Giriniz : ")

    list.update({number:
        {"Name":name,
        "Telefon No":phone,

    }   }   )

    print(list)

