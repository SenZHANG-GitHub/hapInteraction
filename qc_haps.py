import progressbar, pdb
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

prefix = "MIGen_QC_hg19"
#  subchr = 13 

hapnum = []
list_min_freq = []
list_max_freq = []

for ichr in range(22):
    subchr = ichr + 1
    blocksfilename = "blocks_info/" + prefix + "_chr" + str(subchr) + ".blocks.det"
    hapfilename = "tmp_files/" + prefix + "_chr" + str(subchr) + "_blocks.trans.phased.haps"
    outputfilename = "tmp_files/hap_qc_chr" + str(subchr) + ".txt"

    block_snpnum = []
    print('reading ' + blocksfilename + '\n')
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

    num_haps_total = len(haps_total)
    print("number of haplotypes (2*number of samples): " + str(num_haps_total) + "\n")
    indstart = 0

    bar = progressbar.ProgressBar(max_value = len(block_snpnum))
    i = 0 
    print("performing quality control of haplotype values of chr" + str(subchr) + "\n")
    for snplen in block_snpnum:
        bar.update(i)
        i += 1
        tmphaps = [" ".join(ele[indstart:indstart+snplen]) for ele in haps_total]
        tmphapset = Counter(tmphaps)

        hapnum.append(len(tmphapset))
        min_freq = tmphapset.most_common()[-1][1]/num_haps_total
        max_freq = tmphapset.most_common()[0][1]/num_haps_total
        list_min_freq.append(min_freq)
        list_max_freq.append(max_freq)
    bar.finish()

plt.hist(list_min_freq, bins = 30)
plt.xlabel("frequency of the rarest haplotypes")
plt.ylabel("number of haplotype blocks")
plt.title("histogram of the rarest haplotypes")
plt.show()

pdb.set_trace()

plt.hist(list_max_freq, bins = 30)
plt.xlabel("frequency of the most common haplotypes")
plt.ylabel("number of haplotype blocks")
plt.title("histogram of the most common haplotypes")
plt.show()

pdb.set_trace()

#  print("--------------------------\nchr" + str(subchr) + ":\n")
#  print("Number of haplotype blocks: " + str(len(block_snpnum)) + "\n")

#  print("--------------------------\n")
#  print("mean number of haplotype values: " + str(np.mean(hapnum)) + "\n")
#  print("median number of haplotype values: " + str(np.median(hapnum)) + "\n")
#  print("max number of haplotype values: " + str(max(hapnum)) + "\n")
#  print("min number of haplotype values: " + str(min(hapnum)) + "\n")




