def cardnum(n):
    return "*" * (len(str(n))-4)+str(n)[-4:]
num=int(input("enter a number"))
print(cardnum(num))
# or using this method
card_num=int(input("enter a number:"))
card_num[12:]
print('*' * 12 + card_num)