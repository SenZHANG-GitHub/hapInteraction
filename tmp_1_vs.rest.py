import progressbar, pdb

def isinrange(locirange, lower, upper):
    if lower <= locirange[0] and upper >= locirange[0]:
        return True
    if lower >= locirange[0] and upper <= locirange[1]:
        return True
    if lower <= locirange[1] and upper >= locirange[1]:
        return True
    return False


subchr = 3
subrange = [187498383, 187698383] # [177577480, 177777480][187498383, 187698383][81695481, 81895481][39109460, 39444799]

blocksfilename = 'blocks_info/MIGen_QC_hg19_chr' + str(subchr) + '.blocks.det'
hapfilename = 'tmp_files/MIGen_QC_hg19_chr' + str(subchr) + '_blocks.trans.phased.haps'
outname = 'results_1_vs_rest/snpnums_chr'+str(subchr)+'_block_' + str(subrange[0]) + '-' + str(subrange[1])+'.txt'


block_snpnum = []
block_inrange = [] # The index of blocks that overlap with subrange in subchr (starting from 1)
blocksnps_inrange = []
print('reading '+blocksfilename+'\n')
with open(blocksfilename, mode = 'r') as f:
    f.readline() # The first line is the labels
    lines = f.readlines()
    bar = progressbar.ProgressBar(max_value = len(lines))
    i = 0
    for line in lines:
        bar.update(i)
        i += 1
        tmpsplit = line.split()
        block_snpnum.append(int(tmpsplit[4]))
        if isinrange(subrange, int(tmpsplit[1]), int(tmpsplit[2])):
            block_inrange.append(i)
            blocksnps_inrange.append(int(tmpsplit[4]))
    bar.finish()

with open(outname, mode = 'w') as f:
	for snpnum in blocksnps_inrange:
		f.write(str(snpnum) + ' ')