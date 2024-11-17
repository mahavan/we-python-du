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

#print(compare_text("task1-1.txt", "task1-2.txt"))

"""
Task 2
You have a text file. Create a new file and write the following statistics based on the source file to it:

Number of characters;
Number of lines;
Number of vowels;
Number of consonants;
Number of digits.
"""
def statistics(file1, file2):
    with open(file1, encoding="utf-8") as f1:
        str_f1 = f1.read()
    splitlines_f1 = str_f1.splitlines()
    characters = len(str_f1)
    lines = len(splitlines_f1)
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    vowels = "aeiouyáéíóúůý"
    consonants = "bcdfghjklmnpqrstvwxyzčďřšťž"
    for char in str_f1:
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1
        elif char.isdigit():
            digits_count += 1
    output = (f"""File {file1}:
--------------------
Number of characters: {characters}
Number of lines: {lines}
Number of vowels: {vowels_count}
Number of consonants: {consonants_count}
Number of digits: {digits_count}""")
    with open(file2, "w", encoding="utf-8") as f2:
        f2.write(output)

#statistics("task2-1.txt", "task2-2.txt")

"""
Task 3
You have a text file. Delete the last line from it. Write the result to another file.
"""
def last_line(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1:
        lines_f1 = f1.readlines()
    last_line = lines_f1[-1]
    with open(file1, "w", encoding="utf-8") as f1, open(file2, "w", encoding="utf-8") as f2:
        f2.write(last_line)
        delete = lines_f1.pop(-1)
        f1.writelines(lines_f1)

#last_line("task3-1.txt", "task3-2.txt")

"""
Task 4
You have a text file. Find the length of the longest line.
"""
def longest_line(file):
    with open(file, "r", encoding="utf-8") as f1:
        lines = f1.readlines()
    length_list = []
    for line in lines:
        length = len(line)
        if "\n" in line:
            length = length - 1
        length_list += [length]
    length_list.sort(reverse=True)
    print(f"Nejdelší řádek má {length_list[0]} znaků.")

longest_line("task4.txt")

"""
Task 5
You have a text file. Count how many times the word specified by the user occurs in it.
"""

"""
Task 6
You have a text file. Find and replace the specified word. The user determines what to search for and to what it should be replaced.
"""