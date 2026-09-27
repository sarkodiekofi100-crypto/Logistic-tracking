from datetime import datetime

# Store all goods in a dictionary
goods = {}


def add_goods():
    tracking_id = input("Enter tracking ID: ")
    item = input("Enter item/goods name: ")
    sender = input("Enter sender name: ")
    receiver = input("Enter receiver name: ")
    destination = input("Enter destination: ")

    goods[tracking_id] = {
        "item": item,
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "location": "Warehouse",
        "status": "Processing",
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\nGoods successfully added!")
    print("Tracking ID:", tracking_id)


def track_goods():
    tracking_id = input("Enter tracking ID: ")

    if tracking_id in goods:
        item = goods[tracking_id]

        print("\n----- GOODS INFORMATION -----")
        print("Tracking ID:", tracking_id)
        print("Goods:", item["item"])
        print("Sender:", item["sender"])
        print("Receiver:", item["receiver"])
        print("Destination:", item["destination"])
        print("Current Location:", item["location"])
        print("Status:", item["status"])
        print("Last Update:", item["last_update"])
    else:
        print("\nTracking ID not found.")


def update_goods():
    tracking_id = input("Enter tracking ID: ")

    if tracking_id not in goods:
        print("\nTracking ID not found.")
        return

    print("\n1. Processing")
    print("2. In Transit")
    print("3. Arrived at Destination")
    print("4. Out for Delivery")
    print("5. Delivered")

    choice = input("Select new status: ")

    statuses = {
        "1": "Processing",
        "2": "In Transit",
        "3": "Arrived at Destination",
        "4": "Out for Delivery",
        "5": "Delivered"
    }

    if choice in statuses:
        goods[tracking_id]["status"] = statuses[choice]

        new_location = input("Enter current location: ")
        goods[tracking_id]["location"] = new_location

        goods[tracking_id]["last_update"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print("\nGoods information updated successfully!")
    else:
        print("\nInvalid choice.")


def show_all_goods():
    if not goods:
        print("\nNo goods have been registered.")
        return

    print("\n========== ALL GOODS ==========")

    for tracking_id, item in goods.items():
        print("\nTracking ID:", tracking_id)
        print("Goods:", item["item"])
        print("Receiver:", item["receiver"])
        print("Destination:", item["destination"])
        print("Location:", item["location"])
        print("Status:", item["status"])
        print("------------------------------")


def main():
    while True:
        print("\n================================")
        print("       GOODS TRACKING SYSTEM")
        print("================================")
        print("1. Add Goods")
        print("2. Track Goods")
        print("3. Update Goods")
        print("4. View All Goods")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_goods()

        elif choice == "2":
            track_goods()

        elif choice == "3":
            update_goods()

        elif choice == "4":
            show_all_goods()

        elif choice == "5":
            print("\nThank you for using the Goods Tracking System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()