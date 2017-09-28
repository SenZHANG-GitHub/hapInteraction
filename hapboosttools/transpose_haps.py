import progressbar

def haptranspose(prefix, subchr):
    '''
    This function takes a plink prefix and a chromosome number as inputs
    Then transpose the haps data 
    Before: row(snp), col(sample); After: row(sample), col(snp)
    Output: e.g. MIGen_QC_hg19_chr7_blocks.trans.phased.haps
    '''
    orifilename = "tmp_files/" + prefix + "_chr" + str(subchr) + "_blocks.phased.haps"
    outputfilename = "tmp_files/" + prefix + "_chr" + str(subchr) + "_blocks.trans.phased.haps"
    #  orifilename = "MIGen_QC_hg19_chr7_blocks.phased.haps"
    #  outputfilename = "MIGen_QC_hg19_chr7_blocks.trans.phased.haps"

    snpdata = []
    print("reading " + orifilename + "\n")
    with open(orifilename, mode = 'r') as f:
        lines = f.readlines()
        bar = progressbar.ProgressBar(max_value = len(lines))
        i = 0
        for line in lines:
            bar.update(i)
            i += 1
            snpdata.append(line.split()[5:])
        bar.finish()

    # numhaps = 2 * numsamples
    numhaps = len(snpdata[0])
    print("writing " + outputfilename + "\n")
    with open(outputfilename, mode = 'w') as f:
        bar = progressbar.ProgressBar(max_value = numhaps)
        for i in range(numhaps):
            bar.update(i)
            tmphap = [ele[i] for ele in snpdata]
            f.write(" ".join(tmphap) + "\n")
        bar.finish()


