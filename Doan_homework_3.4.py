# Chris Doan homework 3.4.
difference = 0
sequence_1 = input("Enter DNA sequence 1: ")
sequence_2 = input("Enter DNA sequence 2: ")
transitions = 0
for i in range(len(sequence_1)):
    if sequence_2[i] != sequence_1[i]:
        difference = difference + 1
        if sequence_2[i] == "A" and sequence_1[i] == "G":
            transitions = transitions + 1
        elif sequence_2[i] == "C" and sequence_1[i] == "T":
            transitions = transitions + 1
        elif sequence_2[i] == "G" and sequence_1[i] == "A":
            transitions = transitions + 1
        elif sequence_2[i] == "T" and sequence_1[i] == "C":
            transitions = transitions + 1
print("There are", difference, "positions where the DNA sequences differ.")
print("There are", transitions, "transitions.")
print("There are", difference - transitions, "transversions.")
