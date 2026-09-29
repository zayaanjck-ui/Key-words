bill=(int(input("How much was the bill? ")))
paying=(int(input("How much did you pay? ")))
def calc(bill,paying):
    change=(paying-bill)
    return change

answer=calc(paying,bill)
print(answer)
