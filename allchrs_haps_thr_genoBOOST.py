import pdb, os
from collections import Counter
import hapboosttools as hbt
import combine_haps_BOOST as chb

prefix = "MIGen_QC_hg19"
thrlist = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

for thr in thrlist:
    for chrnum in range(22):
        subchr = chrnum + 1
        hbt.gethapval_thr(prefix, subchr, thr)
        hbt.hap2boost_thr(prefix, subchr, thr)

    chb.combinehaps_thr(thr)

#  a = ["A A T", "A A T", "T C G", "A A T", "T C G", "A A A", "A A T", " C G C"]
#  ac = Counter(a)
#  pdb.set_trace()

