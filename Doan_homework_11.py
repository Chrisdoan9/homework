# Chris Doan homework 11
input_FASTA_file = input("Enter FASTA file path: ")
input_file = open(input_FASTA_file, "r")

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
total = A+T+G+C
print("% A =", round(A/total*100, 3))
print("% T =", round(T/total*100, 3))
print("% G =", round(G/total*100, 3))
print("% C =", round(C/total*100, 3))
print("Length of the sequence is:", format(total,"0,"), "bases.")
input_file.close()
input_file = open(input_FASTA_file, "r")
first_line = input_file.readline()
sequence_n = input_file.read()
sequence = sequence_n.replace("\n","")
# print(sequence_n)
k = input("Enter k: ")
n = input("Enter n: ")
n = int(n)
k = int(k)
counts = {}
num_kmers = len(sequence) - k + 1
for i in range(num_kmers):
    kmer = sequence[i:i + k]
    if kmer not in counts:
        counts[kmer] = 0
    counts[kmer] += 1
sorted_frequency = sorted(counts.items(), key=lambda kv: kv[1], reverse = True)
sorted_frequency = sorted_frequency[0:n]
sorted_frequency = dict(sorted_frequency)
for i in sorted_frequency:
    print(i,sorted_frequency[i])
print("# of unique k-mers found =", len(counts))
def exp_frequency(k_mers):
    ex = 1
    for i in range(len(k_mers)):
        if k_mers[i] == "T":
            ex = ex * 0.26592
        elif k_mers[i] == "G":
            ex = ex * 0.23102
        elif k_mers[i] == "A":
            ex = ex * 0.26523
        else:
            ex = ex * 0.23783
    return print(k_mers, ex*(len(sequence)-k+1))
for i in sorted_frequency:
    exp_frequency(i)
input_file.close()