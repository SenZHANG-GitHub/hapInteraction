from .check_blocks import checkblocks
from .reindex_blocks_snps import reindexblocks
from .clean_haps_blocks import cleanblocks
from .transpose_haps import haptranspose
from .get_hap_values import gethapval, gethapval_thr
from .haps_to_BOOST import hap2boost, hap2boost_thr

import os

foldersNeeded = ["blocks_info", "BOOST_results", "raw_results", "tmp_files"]
for folder in foldersNeeded:
    if not os.path.exists(folder):
        os.system("mkdir " + folder)
