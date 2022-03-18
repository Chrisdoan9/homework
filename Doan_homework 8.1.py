# Doan_homework_8.1
import homework_8
input_file = input("Enter file path: ")
output_file = input("Enter output file path and name: ")
input_file = open(input_file, "r")
output_file = open(output_file, "w")
line_1_hete = 0
for line in input_file:
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 = line.split("=") # Split a line into 13 parts by "=".
    a = line.find(".")
    # After splitting, the nucleotide index of each individual will be 0 and 2.
    if ((a2[0] != a2[2]) or (a3[0] != a3[2]) or (a4[0] != a4[2]) or (a5[0] != a5[2]) or (a6[0] != a6[2]) \
        or (a7[0] != a7[2]) or (a8[0] != a8[2]) or a9[0] != a9[2] or a10[0] != a10[2] or a11[0] != a11[2] \
        or a12[0] != a12[2] or a13[0] != a13[2]) and a == -1:
    # This if only write a line has at least one heterozygote individual and doesn't have any ".".
        line_1_hete = line_1_hete + 1
        output_file.write(line)
print("The number of line has at least one heterozygous individual are:", line_1_hete)
input_file.close()
output_file.close()
