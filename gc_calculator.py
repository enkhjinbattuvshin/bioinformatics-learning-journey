#Project: GC Content Calculator
#Author: Enkhjin
#Date: 2026 (12/27/2025)

#1. Define the DNA sequence
#(In the future, we will load this from a file)
dna_sequence="ATGCCCCGGGTAAA"

#2. Count the Gs and Cs
#We use a built-in tool called .count()
g_count = dna_sequence.count("G")
c_count = dna_sequence. count("C")

#3. FInd the total length of the DNA
# len () is a command that counts the letter for us
sequence_length = len(dna_sequence)

#4. Do the Math
#Formulat (G + C) / Total * 100
gc_content = (g_count + c_count) / sequence_length * 100

#5. Report the results 
print("Sequence Analysis Results:")
print("--------------------------")
print("Sequence Length: " + str(sequence_length))
print("GC Content (%): " + str(gc_content))
