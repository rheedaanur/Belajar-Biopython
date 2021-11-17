#ATAS UNTUK PAKEJ YANG DAH SEDIA ADA

import random

#BAWAH NI UNTUK PAKEJ YANG KITA BARU NAK IMPORT

from DNAtoolkit import *

FILEPATH= "data\DNAcontoh.txt"
with open(FILEPATH, "r") as f:  #Bukak fail ini & namakan sebagai f
    sampleDNA= f.read()
   

#DNA = ''.join([random.choice(NukleotidaDNA) for _ in range (50)]) #JANA SEBUAH LIST DENGAN JUMLAH ITEM YANG KITA NAK

#sampleDNA= ""

DNAstr=sampleDNA

#DNAstr = validate_string(sampleDNA)

#BERDASARKAN PILIHAN YANG KITA DAH TETAPKAN iaitu NukleotidaDNA
#join tu maksudnya ambil list yang dijana dalam tu ke dalam string kosong

#Baca DNA
#Pastikan yang dibaca ialah DNA
#Kira berapa kekerapan setiap bes
#Transkrip ke RNA
#Buat Dict untuk padankan bes DNA dengan bes komplemen RNA 
#Tukar bes komplemen jadi bes RNA
#Terjemah kepada Protein
#Buat Dict untuk padankan codon dengan protein


print("[1]-\tDNA yang dikaji:\t:", DNAstr)
print("[2]-\Panjang DNA:\t", len(DNAstr))
print (countBaseFreq(DNAstr))

print("\n[2]\tComplete Strand\t\t:")
print("\t5'", DNAstr,"3'")
print("\t",''.join(['|' for _ in range (len(DNAstr))]))
print("\t3'", make_better_complement(DNAstr),"5'")
print("[3]\tReverse Complement\t:")
print("\t5'", make_reverse_complement(DNAstr), "3'")

print("\n[4]\tRNA strand\t\t:",make_transcription(DNAstr))

print("\n[5]\tProtein\t\t:", make_translation(DNAstr))

acidlist = make_translation(DNAstr)

print("\n[5]\tAmino Acids\t\t:", acidlist)

print("[6]\tProtein\t\t\t\t:",make_protein(acidlist))

