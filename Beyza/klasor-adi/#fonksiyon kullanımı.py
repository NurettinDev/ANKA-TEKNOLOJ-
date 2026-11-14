#fonksiyon kullanımı
def my_function(x,/):#sadece argüman için
    print(x)
my_function(7)


def your_function(*,x):#anahtar argüman ile çalışır
    print(x)
your_function(x=3)

def her_function(x,y,/,*,a,b):
    print(x+y+a+b)
her_function(7,4,a=5,b=2)
