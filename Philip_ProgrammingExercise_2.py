# This email program creates a list of 30 words and phrases that were
# commonly used in spam messages in emails. It will perform a scan
# to see the word / phrase score of the email sent to see if it is
# considered a scam or not.

# A list of words / phrases that are considered spam material.
spam_keywords = [
    "free", "home address", "won", "prize", "million dollars",
    "not a scam", "credit card", "social security number",
    "congratulations", "act now", "offer", "click here",
    "urgent", "not a spam", "million people", "cheap",
    "loan", "download now", "exclusive", "gift",
    "limited time", "no cost", "verify now", "money",
    "once in a lifetime", "call now", "apply now",
    "click below", "membership", "account suspension"
]

# The score that adds up for each spam material found
# to change the results when finished.
def get_spam_rating(score: int) -> str:
    if score == 0:
        return "All clean, no spam detected!"
    elif score <= 2:
        return "Low likelihood of spam detected!"
    elif score <= 5:
        return "Medium likelihood of spam detected!"
    elif score <= 9:
        return "High likelihood of spam detected!"
    else:
        return "The message is entirely all spam based on our detection!"

# This code scans the message to find pieces of spam material.
# Each spam word / phrase gets one point on the score, it will
# show the results depending on if the message is less of spam or
# mostly spam.
def scan_message(message: str) -> tuple[int, list[str]]:
    lower_msg = message.lower()
    score = 0
    match =[]

    for keyword in spam_keywords:
        count = lower_msg.count(keyword.lower())
        if count > 0:
            score += count
            match.append(f'- "{keyword}" (x{count})')

    return score, match

# After scanning, this code will show the results of the written email.
def display_results(score: int, match: list[str], rating: str) -> None:
    print(" ")
    print("-----------------------------------------------------------------")
    print("Your message has been checked by the system.")
    print("We will now print out the results of your spam score.")
    print("-----------------------------------------------------------------")
    print(f"You were given the spam score of {score} point(s).")
    print(f"For its likelihood: {rating}")

    if match:
        print(" ")
        print("Here are some words / phrases that have been")
        print("detected by our system:")
        for item in match:
            print(f"{item}")
    else:
        print("Your message is fully clean from spam!")


# Main Program Function:
# This code will tell the user to make their own email message
# while also scanning for spam words / phrases.
def main ():
    print("-----------------------------------------------------------------")
    print("This is an spam mail checker.")
    print("This will show the likelihood on how much spam is in the message.")
    print("Please write your fake email message below.")
    print("-----------------------------------------------------------------")

    message = input()

    if not message:
        print("-----------------------------------------------------------------")
        print("Nothing was written in your email message.")
        print("Please try again so we can detect any spam.")
        print("-----------------------------------------------------------------")
        return

    score, match = scan_message(message)
    rating = get_spam_rating(score)
    display_results (score, match, rating)

main()