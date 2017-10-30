def usd_to_egp(usd):
    amount = usd * 17.62
    print('That is about', amount, 'EGP')


if __name__ == "__main__":
    while True:
        usd = input("USD: ")
        if usd.isdigit():
            usd_to_egp(usd)
        else:
            print("Invalid input")
