"""
MAIL MERGE PROJECT (Day 24)
This script automates the creation of personalized letters by:
1. Reading a list of names from a file.
2. Reading a template letter.
3. Replacing a placeholder in the template with each name.
4. Saving each personalized letter as a new file.
"""

# --- 1. CONFIGURATION ---
# We define our file paths and the placeholder string we want to replace.
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
NAMES_LETTER_PATH = "./Input/Names/invited_names.txt"
OUTPUT_LETTER_PATH = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"

# --- 2. RETRIEVE NAMES ---
# We open the invited_names.txt file and use readlines() to get a list of names.
# Each name in this list will initially have a newline character (\n) at the end.
with open(NAMES_LETTER_PATH) as names_file:
    names = names_file.readlines()

# --- 3. GENERATE LETTERS ---
# We open the starting_letter.txt template and read its entire content once.
with open(STARTING_LETTER_PATH) as letter_file:
    letter_contents = letter_file.read()
    
    # We loop through each name retrieved in Step 2.
    for name in names:
        # .strip() removes any leading or trailing whitespace, including the \n newline.
        stripped_name = name.strip()
        
        # .replace() creates a new string where the [name] placeholder is swapped with the actual name.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # We create a new, unique file for each person in the 'ReadyToSend' folder.
        # mode="w" ensures the file is created (or overwritten if it already exists).
        with open(f"{OUTPUT_LETTER_PATH}letter_for_{stripped_name}.txt", mode="w") as output_file:
            output_file.write(new_letter)

print("Mail merge completed! All letters are ready in the 'ReadyToSend' folder.")
