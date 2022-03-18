# Doan homework 9.
class DNA:
    def __init__(self, name = "ABC123", sequence = "ACGTCGATC"):
        self.sequence = sequence
        self.name = name
    def length(self):
        return len(self.sequence)
    def gc(self):
        self.c = self.sequence.count("C")
        self.g = self.sequence.count("G")
        return (self.c + self.g)/len(self.sequence)
    def __str__(self):
        return "{}".format(self.sequence)
    def complement(self):
        rdna = self.sequence[::-1].lower()
        rdna = rdna.replace("a", "T")
        rdna = rdna.replace("t", "A")
        rdna = rdna.replace("c", "G")
        rdna = rdna.replace("g", "C")
        return rdna
