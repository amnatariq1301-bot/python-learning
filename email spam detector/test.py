spam_dict = {"lottery":5, "urgent":4, "free":3, "crypto":5, "winner":4}
def check_spam():
    spam_score = 0
    email_text = input("enter the email_text here")
    email = email_text.lower().split()
    for word in email:
        if word == spam_dict:
            spam_score += spam_dict[word]

    print(f"Total spam score: {spam_score}")
    if spam_score > 5:
        print("ALERT! this is a spam email")
    else:
        print("Safe email")

check_spam()
