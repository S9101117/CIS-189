from decimal import *

def calculate_price( price, cash_coupon, percent_coupon):
    temp_total = price

    tempTotal = price - cash_coupon #Subtracting Cash Coupon

    tempTotal = tempTotal - (tempTotal*(percent_coupon/100))#Subtracting Percent Coupon

    tax = tempTotal*0.06 #Calculating tax

    if tempTotal <= 10:
        tempTotal = tempTotal + 5.95
    elif tempTotal >= 10 and tempTotal <= 30:
        tempTotal = tempTotal + 7.95
    elif tempTotal >= 30 and tempTotal <= 50:
        tempTotal = tempTotal + 11.95
    elif tempTotal >= 50:
        tempTotal = tempTotal + 50

    tempTotal = tempTotal + tax

    return float('%.2f'%tempTotal)


def main():
    result = calculate_price(80,10,20)
    print(result)

if __name__=="__main__":
    main()
