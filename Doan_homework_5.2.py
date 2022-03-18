# Chris Doan homework 5.2
input_FASTA_file = input("Enter FASTA file path: ")
input_file = open(input_FASTA_file, "r")
sequence = 0
A = 0
T = 0
G = 0
C = 0
for line in input_file:
    if (line[0] != ">") and (line != ""):
        A = A + line.count("A")
        T = T + line.count("T")
        G = G + line.count("G")
        C = C + line.count("C")
        sequence = sequence + len(line.rstrip())
total = A+T+G+C
print("% A =", round(A/total*100, 3))
print("% T =", round(T/total*100, 3))
print("% G =", round(G/total*100, 3))
print("% C =", round(C/total*100, 3))
print("Length of the sequence is:", format(sequence,"0,"), "bases.")
input_file.close()


