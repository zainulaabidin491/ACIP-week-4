class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.number_of_bids = 0
        self.highest_bid = 0

class Auction:
    def __init__(self):
        self.items = {}

    def add_item(self):
        item_number = int(input("Enter item number: "))
        description = input("Enter item description: ")
        reserve_price = float(input("Enter reserve price: "))
        self.items[item_number] = AuctionItem(item_number, description, reserve_price)

    def view_item(self):
        item_number = int(input("Enter item number: "))
        if item_number in self.items:
            item = self.items[item_number]
            print(f"Item Number: {item.item_number}")
            print(f"Description: {item.description}")
            print(f"Current Highest Bid: {item.highest_bid}")
        else:
            print("Item not found.")

    def place_bid(self):
        buyer_number = int(input("Enter buyer number: "))
        item_number = int(input("Enter item number: "))
        bid = float(input("Enter bid: "))
        if item_number in self.items:
            item = self.items[item_number]
            if bid > item.highest_bid:
                item.highest_bid = bid
                item.number_of_bids += 1
                print("Bid placed successfully.")
            else:
                print("Bid must be higher than existing bids.")
        else:
            print("Item not found.")

    def end_auction(self):
        total_fee = 0
        sold_items = 0
        unsold_items = 0
        no_bids_items = 0
        for item in self.items.values():
            if item.highest_bid >= item.reserve_price:
                sold_items += 1
                total_fee += item.highest_bid * 0.1
                print(f"Item {item.item_number} sold for {item.highest_bid}.")
            elif item.number_of_bids > 0:
                unsold_items += 1
                print(f"Item {item.item_number} did not meet reserve price. Highest bid: {item.highest_bid}.")
            else:
                no_bids_items += 1
                print(f"Item {item.item_number} received no bids.")
        print(f"Total fee: {total_fee}")
        print(f"Number of items sold: {sold_items}")
        print(f"Number of items that did not meet reserve price: {unsold_items}")
        print(f"Number of items with no bids: {no_bids_items}")

def main():
    auction = Auction()
    while True:
        print("\n1. Auction set up")
        print("2. Buyer bids")
        print("3. End auction")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            auction.add_item()
        elif choice == 2:
            auction.view_item()
            auction.place_bid()
        elif choice == 3:
            auction.end_auction()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()