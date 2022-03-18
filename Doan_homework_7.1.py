# Doan_homework_7.1
input_FASTA_file = input("Enter FASTA file path: ")
input_file = open(input_FASTA_file, "r")
length = 0
GC_content = 0
numb = 0
total_length = 0
G = 0
total_G = 0
C = 0
total_C = 0
string = "{:^16}  {:^10}  {:^18}"
print(string.format("Accessing number", "GC content", "Length of sequence", sep="\t"))
for line in input_file:  # Read the file line by line.
    if line[0] != ">":
        G = G + line.count("G")
        total_G = total_G + line.count("G")
        C = C + line.count("C")
        total_C = total_C + line.count("C")
    if line[0] == "A" or line[0] == "T" or line[0] == "G" or line[0] == "C":
        length = length + len(line.rstrip())
        total_length = total_length + len(line.rstrip())
    if line[0] == ">" and length != 0:
        print("{:^6,.2f}".format((G + C)*100 / length) + "%", end="\t")
        print("{:^20}".format(length))
        length = 0  # Reset to start count the length of new sequence.
        G = 0  # Reset to start to count the G of new sequence.
        C = 0  # Reset to start to count the C of new sequence.
    a = line.find("|", line.find("|", line.find("|") + 1) + 1)  # Find the third "|".
    b = line.find("|", line.find("|", line.find("|", line.find("|") + 1) + 1) + 1)  # Find the fourth "|".
    if a != -1:  # If I find 2 "|", I will print the accessing number between the index of third "|" and fourth "|".
        numb = numb + 1
        print("{:^18}".format(line[a + 1:b]), end="\t")
print("", format((G + C) / length, "0.2%"), end=" ")  # Print the last GC content.
print("       ", length)  # Print the last length of sequence.
print("Number of sequences:", numb, ".")
print("Average length of sequences:", round(total_length / numb, 2))
print("Average GC content:", format((total_C + total_G) / total_length, "0.2%"))
