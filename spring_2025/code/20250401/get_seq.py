import pysam
import argparse
import sw

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start",
                        type=int,
                        required=True,
                        help="Start position of the sequence")
    parser.add_argument("--end",
                        type=int,
                        required=True,
                        help="End position of the sequence")
    parser.add_argument("--start_seq",
                        type=str,
                        required=True,
                        help="Consequence seq from clips at the start")
    parser.add_argument("--end_seq",
                        type=str,
                        required=True,
                        help="Consequence seq from clips at the end")

    return parser.parse_args()

def main():
    args = get_args()

    ref_genome = pysam.FastaFile("GCF_000001405.13_GRCh37_genomic.NC_000001.10.fna")

    # Get the sequence from the reference genome
    seq = ref_genome.fetch("NC_000001.10", args.start, args.end)
    print(seq)

    start_seq = seq[:10]
    end_seq = seq[-10:]

    H = sw.sw_fill_matrix(start_seq, end_seq, -2, -1, 1)
    align_A, align_B, score = sw.sw_traceback(H,start_seq, end_seq, -2, -1, 1)

    micro_h = align_A


    c_begin = micro_h + args.end_seq
    c_end = args.start_seq + micro_h

    start_seq = seq[:len(c_begin)]

    H = sw.sw_fill_matrix(start_seq, c_begin, -2, -1, 1)
    align_A, align_B, score = sw.sw_traceback(H,start_seq, c_begin, -2, -1, 1)

    print(align_A)
    print(align_B)
    print(score)

    end_seq = seq[-1*len(c_end):]

    H = sw.sw_fill_matrix(end_seq, c_end, -2, -1, 1)
    align_A, align_B, score = sw.sw_traceback(H, end_seq, c_end, -2, -1, 1)

    print(align_A)
    print(align_B)
    print(score)







if __name__ == "__main__":
    main()




