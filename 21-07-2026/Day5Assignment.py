mileage=45
base_price=100

amount=int(input("Enter the amount available: "))
distance=int(input("Enter the distance from source to dstination(in kms): "))
distance_up_and_down=distance+distance
amount_required=(distance_up_and_down/mileage)*base_price

print("Amount required to required to fuel up: ", amount_required)
if amount_required <=amount:
    print("You can travel having ",amount-amount_required, "rs. remaining")
else:
    print("Amount required is higher")
