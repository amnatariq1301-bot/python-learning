from datetime import date
import sys
import inflect

def main():
    birth_date_str = input("Enter your birthdate (YYYY-MM-DD) : ").strip()

    today = date.today()
    minutes = get_minutes(birth_date_str, today)
    words = convert_to_words(minutes)
    print(words)

def get_minutes(birth_date_str, today):
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    if birth_date > today:
        sys.exit("Birth date cannot be in future")
    days_difference = (today - birth_date).days
    minutes = days_difference * 60
    return minutes
def convert_to_words(minutes):
    """
    Converts an integer number of minutes into capitalized words 
    without any 'and' connectors.
    """
    p = inflect.engine()
    
    # Convert number to words (e.g., "five hundred and twenty-five thousand")
    words = p.number_to_words(minutes, wantlist=False)
    
    # Remove the word "and" per the prompt's instructions
    words = words.replace(" and ", " ")
    
    # Capitalize only the very first letter of the string and append " minutes"
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()