import pdb

def reindexblocks(prefix, subchr):
    '''
    This function takes a plink prefix and a chromosome number as inputs
    Then will check .bim and .blocks files 
    And output the index in .bim file of the snps of .blocks file
    (reason: not all snps will appear in .blocks)
    Output: e.g. index_in_bim_chr7.blocks
    '''
    bimfilename = "blocks_info/" + prefix + "_chr" +str(subchr) + ".bim"
    blocksfilename = "blocks_info/" + prefix + "_chr"+ str(subchr) + ".blocks"
    outputfilename = "blocks_info/" + "index_in_bim_chr" + str(subchr) + ".blocks"
    #  bimfilename = "MIGen_QC_hg19_chr7.bim"
    #  blocksfilename = "MIGen_QC_hg19_chr7.blocks"
    #  outputfilename = "index_in_bim_chr7.blocks"

    total_snps = []
    print("reading " + bimfilename + "\n")
    with open(bimfilename, mode='r') as f:
        for line in f.readlines():
            total_snps.append(line.split()[1])

    block_snps = []
    print("reading " + blocksfilename + "\n")
    with open(blocksfilename, mode = 'r') as f:
        for line in f.readlines():
            block_snps.extend(line.split()[1:])

    iblock_indices_in_total = []
    iblock = 0
    
    for itotal in range(len(total_snps)):
        if (total_snps[itotal] == block_snps[iblock]):
            iblock_indices_in_total.append(itotal)
            iblock += 1
            if iblock >= len(block_snps):
                break


    print("writing "+outputfilename + "\n")
    with open(outputfilename, mode = 'w') as f:
        for i in range(len(block_snps)):
            f.write(block_snps[i] + "\t" + str(iblock_indices_in_total[i]) + "\n")

