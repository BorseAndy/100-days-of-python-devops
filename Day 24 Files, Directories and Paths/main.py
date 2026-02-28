"""
PYTHON FILE I/O GUIDE (Day 24)
This script demonstrates how to interact with the local file system.
The 'with' keyword is used to ensure files are closed automatically.
"""

# --- 1. READING A FILE (Mode: "r" - Default) ---
# We use this to retrieve information stored on the hard drive.
# If you don't specify a mode, Python assumes you want to Read.
filepath = "../myfile.txt"

print("--- Reading File ---")

with open(filepath) as file:
    contents = file.read()
    print(f"File contents: {contents}")


# --- 2. OVERWRITING A FILE (Mode: "w") ---
# WARNING: This deletes everything currently in the file and starts fresh.
# It's like erasing a whiteboard and writing one new sentence.
print("\n--- Overwriting File ---")
with open(filepath, mode="w") as file:
    # Note: .write() returns the number of characters written.
    file.write("This is the new content. The old content is gone!")


# --- 3. APPENDING TO A FILE (Mode: "a") ---
# This is for adding data to the end of an existing file without deleting it.
# We use '\n' to ensure the new text starts on a new line.
print("--- Appending to File ---")
with open(filepath, mode="a") as file:
    file.write("\nThis line was added using append mode!")


# --- 4. CREATING A NEW FILE AUTOMATICALLY ---
# If you try to open a file in "w" or "a" mode that doesn't exist yet, 
# Python will create it for you on the spot.
print("--- Creating New File ---")
with open("brand_new_file.txt", mode="w") as file:
    file.write("Python created this file because it didn't exist before.")

print("\nAll file operations completed successfully!")
