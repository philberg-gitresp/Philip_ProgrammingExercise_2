# Philip_ProgrammingExercise_2
In this program, the user gets to create a fake email message as the program scans the email for any spam material (Ranging from 30 Words / Phrases). Once it finishes scanning, it will display the results of if the email has a high spam score or a low spam score. It will also display the words that may have caused the score to increase.

## Function: get_spam_rating
The score that adds up for each spam material found to change the results when finished.

Parameters:
score: int (The spam score that will add up for each spam material detected.)

Variables:
None

Logic:
1. Each time a piece of spam material is detected, it adds up to the score.
2. Every time it adds up, the score will change the outcome if more or less spam material was found and added to its system.
3. After scanning, it will display the results on if the message was filled with spam or not.

Returns:
	str
If 0, “All clean, no spam detected!”
If 1 - 2, “All clean, no spam detected!”
If 0, “All clean, no spam detected!”
If 0, “All clean, no spam detected!”
## Function: scan_message
Scans the message for spam words / keyphrases to show the results.

Parameters:
message: str (The fake email message given to be scanned for spam material.)

Variables:
lower.msg (Includes the lowercase version of the letters so that the system could detect it.)
score (The score for the spam given its presence in the message.)
match (This makes sure that the words / keyphrases match what was on the list.)
count (Counts how many spam materials were given to the score itself.)
keyword (Shows what keyword / phrase was said for how many was given in the message’s score.)

Logic:
1. Scans the entire message given by the viewer to add each spam material to the score when detected.
2. Counts how many words / keywords were used from the list while separating each word by how it was pronounced.
3. Show the results and see what words / keywords were the cause.

Returns:
score
match

## Function: display_results
Displays the results after viewing and scanning the message for spam material.

Parameters:
score (The number on what the score has.)
match (Displays each word / phrase that matches the ones on the list.)
rating (Displays the description of spam likeliness on the message.)

Variables:
item (Each word / phrase that was mentioned in the results.)

Logic:
1. Prints out the message that will show the results and see if the message was filled with spam or not.
2. Displays the results for the score, item match, and rating that the message was given by the viewer.

Returns:
None

## Function: main
The program will tell the viewer to write an email message as it will then be scanned for spam material, which will show the results when finished.

Parameters:
None

Variables:
message (The message given to by the user’s input, which will be later scanned by the system.)
score (Displays the score for each word / phrase used.)
match (Displays the list of word / phrases that match what is on the list.)
rating (Displays the spam rating depending on how much there is.)

Logic:
1. The program welcomes the user to the spam checking system while also asking the user to input a fake email message.
2. After the message is given, the system will scan the message for any spam material. Like words / phrases on the list for example.
3. Once the message has been fully scanned, the program will display the results of how the message was and how much spam was there.
4. If no message was given, the program will stop while asking the viewer to restart the program and try again.

Returns:
None

