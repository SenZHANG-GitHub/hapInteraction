from scipy.stats import chi2
import pdb

resultname = "allchrs_InteractionRecords.txt"

plist = []
chi2list = []
with open(resultname, mode = 'r') as f:
    for line in f.readlines():
        tmpchi2 = line.split()[5]
        chi2list.append(tmpchi2)
        plist.append(1-chi2.cdf(float(tmpchi2), 4))

plist.sort()
chi2list.sort()

pdb.set_trace()
