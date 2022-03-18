# Chris Doan homework 3.2.
import math
dominant = input("Enter number of dominant phenotype individuals: ")
dominant = eval(dominant)
recessive = input("Enter number of recessive phenotype individuals: ")
recessive = eval(recessive)
recessive_phenotypes = recessive/(dominant+recessive)
print("Fraction of recessive phenotypes: ", recessive_phenotypes)
q = math.sqrt(recessive_phenotypes)
print("Fraction of recessive alleles: ", q)
p = 1-q
print("Fraction of heterozygous genotypes: ", 2*p*q)