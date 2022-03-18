# Chris Doan homework 4.4
DNA = input("Enter the DNA strand: ")
print("Original DNA: ", DNA)
print("Codons")
print("Forward 1: ", end="")
for i in range(len(DNA)):
    if (i % 3 == 0) and (i+2 < len(DNA)):
        print(DNA[i:i+3]+" ", end = "")
print("")
print("Forward 2: ", end = "")
for i in range(len(DNA)):
    if (i % 3 == 1) and (i+2 < len(DNA)):
        print(DNA[i:i+3]+" ", end = "")
print("")
print("Forward 3: ", end ="")
for i in range(len(DNA)):
    if i % 3 == 2 and (i+2 < len(DNA)):
        print(DNA[i:i+3]+" ", end = "")

print("")
for i in range(len(DNA)):
    if DNA[i] == "A":
        DNA = DNA[:i] + "T" + DNA[i + 1:]
    elif DNA[i] == "T":
        DNA = DNA[:i] + "A" + DNA[i + 1:]
    elif DNA[i] == "G":
        DNA = DNA[:i] + "C" + DNA[i + 1:]
    else:
        DNA = DNA[:i] + "G" + DNA[i + 1:]
print("Reserve strand:", DNA[:: -1])
com_DNA = DNA[::-1]
print("Codons")
print("Reserve 1: ", end="")
for i in range(len(com_DNA)):
    if (i % 3 == 0) and (i+2 < len(com_DNA)):
        print(com_DNA[i:i+3]+" ", end = "")
print("")
print("Reserve 2: ", end = "")
for i in range(len(com_DNA)):
    if (i % 3 == 1) and (i+2 < len(com_DNA)):
        print(com_DNA[i:i+3]+" ", end = "")
print("")
print("Reserve 3: ", end ="")
for i in range(len(com_DNA)):
    if i % 3 == 2 and (i+2 < len(com_DNA)):
        print(com_DNA[i:i+3]+" ", end = "")