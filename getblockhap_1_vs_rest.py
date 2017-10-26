import progressbar, pdb

def isinrange(locirange, lower, upper):
    if lower <= locirange[0] and upper >= locirange[0]:
        return True
    if lower >= locirange[0] and upper <= locirange[1]:
        return True
    if lower <= locirange[1] and upper >= locirange[1]:
        return True
    return False


subchr = 20
subrange = [39109460, 39444799] # [177577480, 177777480][187498383, 187698383][81695481, 81895481]

blocksfilename = 'blocks_info/MIGen_QC_hg19_chr' + str(subchr) + '.blocks.det'
hapfilename = 'tmp_files/MIGen_QC_hg19_chr' + str(subchr) + '_blocks.trans.phased.haps'
outname = 'results_1_vs_rest/chr'+str(subchr)+'_block_' + str(subrange[0]) + '-' + str(subrange[1])+'.trans.haps'

block_snpnum = []
block_inrange = [] # The index of blocks that overlap with subrange in subchr (starting from 1)
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


indstart = 0
indend = 0
numhaps = len(haps_total)
rangehaps = [[] for ele in range(numhaps)]

bar = progressbar.ProgressBar(max_value = len(block_snpnum))
i = 0
print("generating haplotype values\n")
for snplen in block_snpnum: # loop through all haplotype blocks
    bar.update(i)
    i += 1 # i-th block, starting from 1

    indend = indstart + snplen 
    if i in block_inrange:
        for ihap in range(numhaps):
            rangehaps[ihap].extend(haps_total[ihap][indstart:indend])
    indstart = indend
bar.finish()

print('writing results for this block\n')
bar = progressbar.ProgressBar(max_value = (len(rangehaps)))
i = 0
with open(outname, mode = 'w') as f:
    for hap in rangehaps:
        bar.update(i)
        i += 1
        f.write(' '.join(hap) + '\n')
bar.finish()