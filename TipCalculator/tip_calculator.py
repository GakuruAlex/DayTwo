def tip_calculator(bill: float, tip: int, num_people: int)-> float:
    """_summary_

    Args:
        bill (float): _Total bill to be paid_
        tip (int): _tip to give_
        num_people (int): _Number of people splitting bill_

    Returns:
        float: _Amount each person will pay_
    """
    return round((bill * (1 + tip / 100)) / num_people, 2)

def main() -> None:
    print("Welcome to tip calculator")
    bill = input("Enter bill to pay: ")
    tip = input("How much do you wish to tip (10%, 12%, 15%) ?")
    people = input("How many people are splitting the bill ?")
    
    tip = int(tip)
    bill = float(bill)
    people = int(people)
    
    share = tip_calculator(bill=bill, tip=tip, num_people=people)
    
    print(f"Bill for each person is: {share}")
    
if __name__ == "__main__":
    main()