import pdb, progressbar
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

prefix = "MIGen_QC_hg19"
#  haplen = []
#  for i in range(22):
    #  with open("blocks_info/" + prefix + "_chr" + str(i+1) + ".blocks.det", mode = 'r') as f:
        #  f.readline()
        #  for line in f.readlines():
            #  haplen.append(int(line.split()[4]))

#  plt.hist(haplen, bins = 30)
#  plt.xlabel("length of haplotypes")
#  plt.ylabel("number of haplotypes")
#  plt.title("histogram of haplotype's length")
#  plt.show()


hapnum_all = []
for ichr in range(22):
    subchr = ichr + 1
    blocksfilename = "blocks_info/" + prefix + "_chr" + str(subchr) + ".blocks.det"
    hapfilename = "tmp_files/" + prefix + "_chr" +str(subchr) + "_blocks.trans.phased.haps"
 
    print('reading '+blocksfilename+'\n')
    with open(blocksfilename, mode = 'r') as f:
        f.readline()
        lines = f.readlines()
        bar = progressbar.ProgressBar(max_value = len(lines))
        i = 0
        for line in lines:
            bar.update(i)
            i += 1
            block_snpnum.append(int(line.split()[4]))
        bar.finish()

    # len(haps_total) = 2 * number_samples
    haps_total = []
    print("reading " + hapfilename + "\n")
    with open(hapfilename, mode = 'r') as f:
        lines = f.readlines()
        bar = progressbar.ProgressBar(max_value = len(lines))
        i = 0
        for line in lines:
            bar.update(i)
            i += 1
            haps_total.append(line.split())
        bar.finish()

    indstart = 0
    hapnum_chr = []

    bar = progressbar.ProgressBar(max_value = len(block_snpnum))
    i = 0
    print("counting haplotype values\n")
    for snplen in block_snpnum: # loop through all haplotype blocks
        bar.update(i)
        i += 1
        tmphaps = [' '.join(ele[indstart:indstart+snplen]) for ele in haps_total]
        tmphapset = Counter(tmphaps)
        hapnum_chr.append(len(tmphapset))
        hapnum_all.append(len(tmphapset))

    bar.finish()
    print("--------------------------\nchr"+str(subchr) + ": \n")
    print("mean number of haplotype values: " + str(np.mean(hapnum_chr))+"\n")
    print("median number of haplotype values: " + str(np.median(hapnum_chr))+"\n")
    print("max number of haplotype values: " + str(max(hapnum_chr))+"\n")
    print("min number of haplotype values: " + str(min(hapnum_chr))+"\n")
    plt.hist(hapnum_chr, bins = 30)
    plt.xlabel("Possible values of haplotypes")
    plt.ylabel("Number of haplotypes")
    plt.title("histogram of haplotype's possible values for chr"+str(subchr))
    plt.show()
    pdb.set_trace()

print("--------------------------\nall chrs:\n")
print("mean number of haplotype values: " + str(np.mean(hapnum_all))+"\n")
print("median number of haplotype values: " + str(np.median(hapnum_all))+"\n")
print("max number of haplotype values: " + str(max(hapnum_all))+"\n")
print("min number of haplotype values: " + str(min(hapnum_all))+"\n")

plt.hist(hapnum_all, bins = 30)
plt.xlabel("Possible values of haplotypes")
plt.ylabel("Number of haplotypes")
plt.title("histogram of haplotype's possible values for all chrs")
plt.show()
pdb.set_trace()

