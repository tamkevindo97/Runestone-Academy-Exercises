def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price == 0 and count == 0:
            print("Cannot divide by zero")
            moreItems = False
        else:
            if price > 0:
                count = count + 1
                total = total + price
                print('Subtotal: $', total)
                average = total / count
            elif price < 0:
                repeat_price = float(input('NEGATIVE NUMBER ERROR: Please re-enter the price of item or 0 to finish'))
                price = repeat_price
                if price == 0:
                    moreItems = False
                    print("Checkout finished.")
                elif price < 0:
                    moreItems = False
                    print("Negatives are not allowed. Checkout aborted.")
                else:
                    count = count + 1
                    total = total + price
                    average = total/count
                    print('Subtotal: $', total)
            else:
                moreItems = False
                print("Checkout finished")

    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
