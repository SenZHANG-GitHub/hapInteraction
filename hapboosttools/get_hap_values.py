import progressbar, pdb
from collections import Counter

def gethapval(prefix, subchr):
    '''
    This function takes plink prefix and a chromosome number as inputs
    Then transform _block.trans.phased.haps file into hap_values_chr.txt
    Current strategy: 0/1 for most_common/or_not haplotypes
    Output: e.g. hap_values_chr7.txt
    '''

    print("version 2.0\n")
    blocksfilename = "blocks_info/" + prefix + "_chr" + str(subchr) + ".blocks.det"
    hapfilename = "tmp_files/" + prefix + "_chr" +str(subchr) + "_blocks.trans.phased.haps"
    outputfilename = "tmp_files/hap_values_chr" + str(subchr) + ".txt"
    #  blocksfilename = "MIGen_QC_hg19_chr7.blocks.det"
    #  hapfilename = "MIGen_QC_hg19_chr7_blocks.trans.phased.haps"
    #  outputfilename = "hap_values_chr7.txt"

    block_snpnum = []
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
    indend = 0
    haplen = []
    hapvalues = [] # p(num of haps) elements, each element(n) contains the value for one haplotype at all samples 

    bar = progressbar.ProgressBar(max_value = len(block_snpnum))
    i = 0
    print("generating haplotype values\n")
    for snplen in block_snpnum: # loop through all haplotype blocks
        bar.update(i)
        i += 1
        #  tmphapset = set([' '.join(ele[indstart:indstart+snplen]) for ele in haps_total])

        indend = indstart + snplen
        tmphaps = [' '.join(ele[indstart:indend]) for ele in haps_total]
        indstart = indend

        tmphapset = Counter(tmphaps)

        haplen.append(len(tmphapset))

        tmphapvalues = [] # length: number of individuals
        mostcommon_hap = tmphapset.most_common(1)[0][0]
        for hapval in tmphaps:
            if (hapval == mostcommon_hap):
                tmphapvalues.append('0')
            else:
                tmphapvalues.append('1')
        hapvalues.append(tmphapvalues)
    bar.finish()

    print("writing results\n")
    with open(outputfilename, mode = 'w') as f:
        bar = progressbar.ProgressBar(max_value = len(hapvalues[0]))
        i = 0
        for isample in range(len(hapvalues[0])):
            bar.update(i)
            i += 1
            f.write(" ".join([ele[isample] for ele in hapvalues]) + "\n")
        bar.finish()
        
def gethapval_thr(prefix, subchr, thr):
    '''
    This function takes plink prefix and a chromosome number as inputs
    Then transform _block.trans.phased.haps file into hap_values_chr.txt
    Current strategy: 0/1 for most_common/or_not haplotypes
    Output: e.g. hap_values_chr7.txt
    '''
    blocksfilename = "blocks_info/" + prefix + "_chr" + str(subchr) + ".blocks.det"
    hapfilename = "tmp_files/" + prefix + "_chr" +str(subchr) + "_blocks.trans.phased.haps"
    outputfilename = "tmp_files/hap_values_thr_"+ str(thr) + "_chr" + str(subchr) + ".txt"
    #  blocksfilename = "MIGen_QC_hg19_chr7.blocks.det"
    #  hapfilename = "MIGen_QC_hg19_chr7_blocks.trans.phased.haps"
    #  outputfilename = "hap_values_thr_0.5_chr7.txt"

    block_snpnum = []
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

    numhaps_thr = len(haps_total) * thr

    indstart = 0
    haplen = []
    hapvalues = [] # p(num of haps) elements, each element(n) contains the value for one haplotype at all samples 

    bar = progressbar.ProgressBar(max_value = len(block_snpnum))
    i = 0
    print("generating haplotype values\n")
    for snplen in block_snpnum: # loop through all haplotype blocks
        bar.update(i)
        i += 1
        #  tmphapset = set([' '.join(ele[indstart:indstart+snplen]) for ele in haps_total])

        indend = indstart + snplen
        tmphaps = [' '.join(ele[indstart:indend]) for ele in haps_total]
        indstart = indend
        tmphapset = Counter(tmphaps)

        haplen.append(len(tmphapset))

        tmphapvalues = [] # length: number of individuals
        haplist_thr = []
        tmporder = tmphapset.most_common()
        tmpnumhaps = 0

        for m in range(len(tmporder)):
            tmpnumhaps += tmporder[m][1]
            haplist_thr.append(tmporder[m][0])
            if tmpnumhaps > numhaps_thr:
                break

        for hapval in tmphaps:
            if (hapval in haplist_thr):
                tmphapvalues.append('0')
            else:
                tmphapvalues.append('1')
        hapvalues.append(tmphapvalues)
    bar.finish()

    print("writing results\n")
    with open(outputfilename, mode = 'w') as f:
        bar = progressbar.ProgressBar(max_value = len(hapvalues[0]))
        i = 0
        for isample in range(len(hapvalues[0])):
            bar.update(i)
            i += 1
            f.write(" ".join([ele[isample] for ele in hapvalues]) + "\n")
        bar.finish()



            

