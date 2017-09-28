import progressbar

def cleanblocks(prefix, subchr):
    '''
    This function takes a plink prefix and a chromosome number as inputs
    Then removes the snps that are not in the blocks (by leveraging index_in_bim_chr.blocks)
    Output filename: e.g. MIGen_QC_hg19_chr7_blocks.phased.haps
    '''
    hapfilename = "raw_results/" + prefix+ "_chr" + str(subchr) + ".phased.haps"
    indexfilename = "blocks_info/index_in_bim_chr" + str(subchr) + ".blocks"
    outputfilename = "tmp_files/" + prefix + "_chr" + str(subchr) + "_blocks.phased.haps"
    #  hapfilename = "MIGen_QC_hg19_chr7.phased.haps" 
    #  indexfilename = "index_in_bim_chr7.blocks"
    #  outputfilename = "MIGen_QC_hg19_chr7_blocks.phased.haps"

    indices_in_bim = []
    print("reading " + indexfilename + "\n")
    with open(indexfilename, mode = 'r') as f:
        for line in f.readlines():
            indices_in_bim.append(int(line.split()[1]))

    print("reading " + hapfilename + "\n")
    with open(hapfilename, mode = 'r') as f:
        lines = f.readlines()
        print("writing " + outputfilename + "\n")
        bar = progressbar.ProgressBar(max_value = len(indices_in_bim))
        fout = open(outputfilename, mode = 'w')
        i = 0
        for ind in indices_in_bim: 
            bar.update(i)
            i += 1
            fout.write(lines[ind])
        bar.finish()
