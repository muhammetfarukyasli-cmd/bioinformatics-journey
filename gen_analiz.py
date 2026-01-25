from Bio.Seq import Seq
dna=Seq("ATGGCCATTGTA")
print("1.Analiz Edilen Dna:",dna)
print("protein karsılıgı:",dna.translate())