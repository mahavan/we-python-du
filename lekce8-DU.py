"""
Task 1
You have two text files. Find out if their lines match. If they don't, print the mismatched line from each file.
"""
def compare_text(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        data_f1 = f1.readlines()
        data_f2 = f2.readlines()
    output = ""
    if len(data_f1) > len(data_f2): # if file2 is shorter add empty lines
        diff = len(data_f1) - len(data_f2)
        for _ in range(diff):
            data_f2.append("\n")
    else: # if file1 is shorter add empty lines
        diff = len(data_f2) - len(data_f1)
        for _ in range(diff):
            data_f1.append("\n")
    for i in range(len(data_f1)): # different lines
        if data_f1[i] != data_f2[i]:
            output += data_f1[i] + data_f2[i]
    return output

print(compare_text("task1-1.txt", "task1-2.txt"))

"""
Task 2
You have a text file. Create a new file and write the following statistics based on the source file to it:

Number of characters;
Number of lines;
Number of vowels;
Number of consonants;
Number of digits.
"""

"""
Task 3
You have a text file. Delete the last line from it. Write the result to another file.
"""

"""
Task 4
You have a text file. Find the length of the longest line.
"""

"""
Task 5
You have a text file. Count how many times the word specified by the user occurs in it.
"""

"""
Task 6
You have a text file. Find and replace the specified word. The user determines what to search for and to what it should be replaced.
"""