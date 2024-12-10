def wait():
    print("Waiting...")

def abortOffer():
    print("Aborting Offer...")

def collectItems():
    print("Collecting Items...")

def buy():
    print("Buying...")

def sell():
    print("Selling...")

status = "Sell"
def main():
    if status == "Wait":
        wait()
    elif status == "Abort Offer":
        abortOffer()
    elif status == "Collect Items":
        collectItems()
    elif status == "Buy":
        buy()
    elif status == "Sell":
        sell()
main()