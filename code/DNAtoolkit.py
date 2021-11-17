"""
Yang Belajar: Nurhidayah Nordin
Tarikh: 2021=11-06

Tujuan: Saja nak belajar

"""

#Baca DNA
#-Pastikan yang dibaca ialah DNA
#Transkrip ke RNA
#Terjemah kepada Protein

from structures import *


# "GAKDAKCNAIWFHHDAOEFJWWODHWHFWO" setiap huruf ada tak dalam NukleotidaDNA?

def validate_string(DNAstr):

    """ 
    
    Documentation string
    Pastikan string tersebut ialah DNA

    :input(params) DNAstr: String yang nak disahkan

    :return:
    
    """

    for nuc in DNAstr:
        if nuc in NukleotidaDNA:            #jika item ada dalam senarai, dikira True
            #Kalau DNA, kita return balik DNA tu.
            result= DNAstr
        else:
            #Kalau bukan DNA nak buat apa?
            result = False           #Maksudnya dia bukan DNA
            break

    return result

def countBaseFreq(DNAstr):

    """
    kira kekerapan setiap bes DNA dan pulangkan dalam bentuk dict

    :params DNAstr: DNA yang besnya nak dikira

    :return: dict

    """
    bakul ={
        "A":0,
        "C":0,
        "T":0,
        "G":0,

    }

    #AMBIL HURUF BES
    #CARI BAKUL YANG ADA HURUF SAMA DALAM DICTIONARY
    #MASUKKAN BES DALAM BAKUL 

    for base in DNAstr:
        bakul [base] += 1
        
        
    return bakul 

def make_better_complement(DNAstr):
    """
    Buat complementary strand untuk DNAstr

    :params DNAstr

    :return: str 
    
    """

    complement = ''.join([DNAComplement[base]for base in DNAstr]) 

    #loop join ni sesuai untuk list sahaja
   
    return complement


def make_reverse_complement (DNAstr):
    """
    Makes a reverse complement of the DNA string

    :return:str

    """
    return make_better_complement (DNAstr)[::-1] # -1 tu ambil yang belakang sekali

def make_transcription(DNAstr):

    """
    Buat RNA daripada DNAstr

    :return:str
    
    """

    return make_better_complement(DNAstr).replace ("T","U")



#tuple adalah jenis data yang kita tak boleh ubah

def make_translation(DNAstr):

    """
    Buat list asid amino dari string DNA yang diberi

    :params DNAstr:

    :return: list

    """

    # 012345
    # ABCDEF

    #do this for every item in the list
    acids = [DNACodon[DNAstr[i:i+3]]for i in range (0, len(DNAstr)-2, 3)]

    return acids 
    
    
    #for i in range (0, len(DNAstr)-2, 3): #yang ni untuk bantu buat loop
        #acids.append(DNACodon[DNAstr[i:i+3]])
        
        #[x:x] kiri masuk kanan tak masuk


def make_protein(AcidList):
    """
    Buat protein daripada senarai asid amino yang diberi 
    
    """


#LANGKAH 1:Cari M (START)
#--> Append nilai M dan seterusnya
#LANGKAH 2: Cari _ (STOP)
#-->Jangan append_ dan berhenti

    proteins = []
    protein= []
    for acid in AcidList:
        if acid=="_":
            #IF stop
            if protein:
                for p in protein:
                    #masukkan protein dalam senarai besar
                    proteins.append(p)
                #kosongkan protein yang sekarang lepas dah masuk dalam senarai besar

                protein= []
        else:
            if acid=="M":
                protein.append("") #Inilah bahagian yang mula ambik protein
            for i in range(len(protein)):
                protein[i] += acid

    return proteins                


