# Chris homework 5.1
input_file = input("Enter file path: ")
output_file = input("Enter output file path and name: ")
input_file = open(input_file, "r")
output_file = open(output_file,"w")
for line in input_file:
    line = line.replace(",","\t")
    print(line, end = "")
    output_file.write(line)
input_file.close()
output_file.close()
# don't need a for loop
