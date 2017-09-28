import pdb

def checkblocks(prefix, subchr):
    '''
    This function takes prefix of plink file and a chromosome number as input
    Then check the .blocks.det file of this chromosome
    pdb stops in the end, and we can check haps and numsnps manually
    E.g. prefix = "MIGen_QC_hg19", chr = 7 -> check file "MIGen_QC_hg19_chr7.blocks.det"
    '''
    filename = "blocks_info/"+prefix + "_chr" + str(subchr) + ".blocks.det"
    # filename =  "MIGen_QC_hg19_chr7.blocks.det"
    haps = []
    numsnps = []
    print("reading " + filename + "\n")
    with open(filename, mode = 'r') as f:
        f.readline()
        for line in f.readlines():
            tmpline = line.split()
            haps.append(tmpline)
            numsnps.append(int(tmpline[4]))

    pdb.set_trace()
