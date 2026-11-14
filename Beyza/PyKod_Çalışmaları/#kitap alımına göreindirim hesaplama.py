#kitap alımına göreindirim hesaplama
quantity=int(input("Enter the number of books you want to order:"))
book_price=105

total_price=quantity*book_price

if(quantity>=50):
    discount_rate=0.25
elif(quantity>=25):
    discount_rate=0.15
elif(quantity>=10):
    discount_rate=0.10
else:
    discount_rate=0.00
discount_amount=total_price*discount_rate

final_price=total_price-discount_amount
print(f"Total price (before discount):{total_price:.1f} TL")
print(f"Discount amount:{discount_amount:.1f} TL")
print(f"Final price to pay:{final_price:.1f} TL")
