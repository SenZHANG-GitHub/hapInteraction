import hapboosttools as hbt

prefix = "MIGen_QC_hg19"
for i in range(22):
    subchr = i + 1 
    hbt.reindexblocks(prefix, subchr)
    hbt.cleanblocks(prefix, subchr)
    hbt.haptranspose(prefix, subchr)
    hbt.gethapval(prefix, subchr)
    hbt.hap2boost(prefix, subchr)
