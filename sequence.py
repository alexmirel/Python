class Sequence:
    def __init__(self, sequence):
        self.seq = sequence
        self.__seqvalid = self.__validate()
        self.__seqtype = self.__get_type()

    def __str__(self):
        return self.seq

    def __getitem__(self, item):
        return self.seq[item]

    def __validate(self):
        self.seq = self.seq.upper()
        invalid_nucleotides = 0

        for nucleotide in self.seq:
            if nucleotide not in {"A", "C", "T", "G", "U"}:
                invalid_nucleotides += 1

        if "T" in self.seq and "U" in self.seq:
            invalid_nucleotides += 1

        if invalid_nucleotides > 0:
            return False
        else:
            return True

    def __get_type(self):
        if self.__seqvalid:
            if "T" in self.seq:
                return "DNA"
            elif "U" in self.seq:
                return "RNA"

    def length(self):
        if self.__seqvalid:
            return len(self.seq)

    def count(self, nucleotide):
        if self.__seqvalid:
            return self.seq.count(nucleotide.upper())

    def gc_content(self):
        if self.__seqvalid:
            return round(((self.seq.count("G") + self.seq.count("C"))
                          / len(self.seq)) * 100, 2)

    def complement(self):
        if self.__seqtype == "DNA":
            return self.seq.translate(self.seq.maketrans("ACTG", "TGAC"))

    def reverse_complement(self):
        if self.complement():
            return self.complement()[::-1]

    def transcribe(self):
        if self.__seqtype == "DNA":
            return self.seq.replace("T", "U")

    def reverse_transcribe(self):
        if self.__seqtype == "RNA":
            return self.seq.replace("U", "T")

    def translate(self):
        if self.__seqvalid:
            genetic_code = {
                "GCA": "A", "GCC": "A", "GCT": "A", "GCG": "A", "GGA": "G",
                "GGC": "G", "GGT": "G", "GGG": "G", "GTA": "V", "GTC": "V",
                "GTT": "V", "GTG": "V", "GAA": "E", "GAG": "E", "GAT": "D",
                "GAC": "D", "CTA": "L", "CTC": "L", "CTT": "L", "CTG": "L",
                "TTA": "L", "TTG": "L", "CGA": "R", "CGC": "R", "CGT": "R",
                "CGG": "R", "AGA": "R", "AGG": "R", "CCA": "P", "CCC": "P",
                "CCT": "P", "CCG": "P", "CAA": "Q", "CAG": "Q", "ATG": "M",
                "ATA": "I", "ATC": "I", "ATT": "I", "AGT": "S", "AGC": "S",
                "TCA": "S", "TCG": "S", "TCC": "S", "TCT": "S", "ACT": "T",
                "ACA": "T", "ACG": "T", "ACC": "T", "AAA": "K", "AAG": "K",
                "AAT": "N", "AAC": "N", "TTC": "F", "TTT": "F", "TGG": "W",
                "TGC": "C", "TGT": "C", "TAC": "Y", "TAT": "Y", "CAC": "H",
                "CAT": "H", "TGA": "-", "TAG": "-", "TAA": "-"
            }

            orfs = []

            if self.__seqtype == "RNA":
                dna = self.seq.replace("U", "T")
                dna_rc = dna.translate(dna.maketrans("ACTG", "TGAC"))[::-1]
                orfs = [
                    dna,
                    dna[1:],
                    dna[2:],
                    dna_rc,
                    dna_rc[1:],
                    dna_rc[2:]
                ]

            if self.seq.__seqtype == "DNA":
                orfs = [
                    self.seq,
                    self.seq[1:],
                    self.seq[2:],
                    self.reverse_complement(),
                    self.reverse_complement()[1:],
                    self.reverse_complement()[2:]
                ]

            result = []

            for orf in orfs:
                translated = ""
                while len(orf) >= 3:
                    codon = orf[:3]
                    orf = orf[3:]
                    translated += codon.replace(codon, genetic_code[codon])
                result.append(translated)

            return result