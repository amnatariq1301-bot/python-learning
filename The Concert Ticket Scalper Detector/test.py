blacklist = {"ahmed", "ali", "asif"}
promo_codes = {
    "ROCK50" : 0.5,
    "DISCOUNT10" : 0.1,
    "VIP60" : 0.6
}

transactions = [
    "amna:2:ROCK50",
    "imran:7:DISCOUNT10",
    "akbar:1:INVALID USER",
    "ahmaed:1:VIP60",
    "atif:8:VIP60"
]

base_ticket_price = 100
total_revenue = 0.0
successful_buyers = []
used_promo_codes = set()

"""STARTING TRANSACTION ANALAYSIS"""

for transaction in transactions:
    name, ticket_count_str, promo = transaction.split(":")
    ticket_count = int(ticket_count_str)
    if name in blacklist:
        print(f"Transaction Blocked ! the {name} is on blacklist")
        continue
    if ticket_count > 5:
        print(f"Transaction Blocked!  {name} tried to buye {ticket_count} tickets. (Limit is 5)")
        continue
    try:
        discount = promo_codes[promo]
        price_per_ticket = base_ticket_price * (1-discount)
        current_total = price_per_ticket * ticket_count
        used_promo_codes.add(promo)
    except KeyError:
        print(f"NOTE: {name} used invalid promo code {promo} . Processing at full price")
        current_total = base_ticket_price * ticket_count
    total_revenue+=current_total
    successful_buyers.append(name)
    print(f"Processed {ticket_count} tickets for {name} . total cost {current_total}")

    """Final Summary"""
print(f"Total Revenue: {total_revenue}")
print(f"Successfull buyers: {successful_buyers}")
print(f"Unique promo codes used: {used_promo_codes}")