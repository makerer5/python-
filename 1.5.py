try:
    from Bio import SeqIO

    print("Biopython is successfully installed.")
except ImportError:
    print("Biopython is not installed or not properly configured.")
