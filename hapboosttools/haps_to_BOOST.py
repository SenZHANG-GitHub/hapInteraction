import progressbar

def hap2boost(prefix, subchr):
    '''
    This function takes a plink prefix and a chromosome number as inputs
    Then transfrom hap_value_chr.txt into hap_BOOST_chr.txt
    Actually do: add up every two rows in hap_value_chr.txt (because each sample contains two haplotypes)
    Output: e.g. hap_BOOST_chr7.txt
    '''
    hapfilename = "tmp_files/hap_values_chr"+ str(subchr) + ".txt"
    #  samplefilename = prefix + "_chr" + str(subchr) + ".phased.sample"
    outputfilename = "BOOST_results/hap_BOOST_chr" + str(subchr) + ".txt"
    #  hapfilename = "hap_values_chr7.txt"
    #  samplefilename = "MIGen_QC_hg19_chr7.phased.sample"
    #  outputfilename = "hap_BOOST_chr7.txt"

    #  pheno = []
    #  print("reading sample file: "+ samplefilename + "\n")
    #  with open(samplefilename, mode = "r") as f:
        #  f.readline()
        #  f.readline()
        #  for line in f.readlines():
            #  pheno.append(line.split()[6])
    #  print("Number of samples read: "+ str(len(pheno)) + "\n")

    print("transforming the data into BOOST format\n")
    print("from " + hapfilename + " to " +outputfilename + "\n")
    with open(outputfilename, mode = "w") as fout:
        with open(hapfilename, mode = "r") as fhap:
           haplines = fhap.readlines()
           bar = progressbar.ProgressBar(max_value = int(len(haplines)/2))
           for i in range(int(len(haplines)/2)):
               bar.update(i)
               hap1 = haplines[2*i].split()
               hap2 = haplines[2*i+1].split()
               #  fout.write(pheno[i] + " ")
               for j in range(len(hap1)):
                   fout.write(str(int(hap1[j]) + int(hap2[j])) + " ")
               fout.write("\n") 
           bar.finish() 

ef hap2boost_thr(prefix, subchr, thr):
    '''
    This function takes a plink prefix and a chromosome number as inputs
    Then transfrom hap_value_chr.txt into hap_BOOST_chr.txt
    Actually do: add up every two rows in hap_value_chr.txt (because each sample contains two haplotypes)
    Output: e.g. hap_BOOST_chr7.txt
    '''
    hapfilename = "tmp_files/hap_values_thr_"+ str(thr)+ "_chr"+ str(subchr) + ".txt"
    #  samplefilename = prefix + "_chr" + str(subchr) + ".phased.sample"
    outputfilename = "BOOST_results/hap_BOOST_thr_"+str(thr)+"_chr" + str(subchr) + ".txt"
    #  hapfilename = "hap_values_chr7.txt"
    #  samplefilename = "MIGen_QC_hg19_chr7.phased.sample"
    #  outputfilename = "hap_BOOST_chr7.txt"

    #  pheno = []
    #  print("reading sample file: "+ samplefilename + "\n")
    #  with open(samplefilename, mode = "r") as f:
        #  f.readline()
        #  f.readline()
        #  for line in f.readlines():
            #  pheno.append(line.split()[6])
    #  print("Number of samples read: "+ str(len(pheno)) + "\n")

    print("transforming the data into BOOST format\n")
    print("from " + hapfilename + " to " +outputfilename + "\n")
    with open(outputfilename, mode = "w") as fout:
        with open(hapfilename, mode = "r") as fhap:
           haplines = fhap.readlines()
           bar = progressbar.ProgressBar(max_value = int(len(haplines)/2))
           for i in range(int(len(haplines)/2)):
               bar.update(i)
               hap1 = haplines[2*i].split()
               hap2 = haplines[2*i+1].split()
               #  fout.write(pheno[i] + " ")
               for j in range(len(hap1)):
                   fout.write(str(int(hap1[j]) + int(hap2[j])) + " ")
               fout.write("\n") 
           bar.finish() 