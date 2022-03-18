# Chris Doan homework 3.3.
input_strand = input("Enter a strand of DNA: ")
print("Input strand: ", input_strand)
for i in range(len(input_strand)):
    if input_strand[i] == "A":
        input_strand = input_strand[:i] + "T" + input_strand[i + 1:]
    elif input_strand[i] == "T":
        input_strand = input_strand[:i] + "A" + input_strand[i + 1:]
    elif input_strand[i] == "G":
        input_strand = input_strand[:i] + "C" + input_strand[i + 1:]
    else:
        input_strand = input_strand[:i] + "G" + input_strand[i + 1:]
print("Reserve complement:", input_strand[:: -1])


