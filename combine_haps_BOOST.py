import progressbar
samplefilename = "raw_results/MIGen_QC_hg19_chr1.phased.sample"
happrefix= "BOOST_results/hap_BOOST_chr"
outputfilename = "MIGen_QC_hg19_BOOST.txt"
phenofilename = "sample_pheno.txt"

phenos = []
print("reading file: " + samplefilename + "\n")
with open(samplefilename, mode = 'r') as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        phenos.append(str(int(line.split()[6]) - 1))

print("writing file: " + phenofilename + "\n")
with open(phenofilename, mode = 'w') as fphe:
    for phe in phenos:
        fphe.write(phe + "\n")

allhaps = []
for i in range(22):
    sschr = str(i + 1)
    chrhaps = []
    bar = progressbar.ProgressBar(max_value = len(phenos))
    ibar = 0
    print("reading file: " + happrefix + sschr + ".txt\n")
    with open(happrefix + sschr + ".txt", mode = 'r') as fhap:
        for line in fhap.readlines():
            bar.update(ibar)
            chrhaps.append(line.split())
            ibar += 1
    allhaps.append(chrhaps)
    bar.finish()

bar = progressbar.ProgressBar(max_value = len(phenos))
print("writing file: " + outputfilename + "\n")
with open(outputfilename, mode = 'w') as fout:
    for i in range(len(phenos)):
        bar.update(i)
        fout.write(phenos[i] + " ")
        for subchrhap in allhaps:
            fout.write(" ".join(subchrhap[i]) + " ")
        fout.write("\n")
bar.finish()

