def usd_to_egp(usd):
    amount = usd * 17.65
    print('That is about', amount, 'EGP')

while True:
    usd_to_egp(int(input("USD: ")))