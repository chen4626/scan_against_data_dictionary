import sys, re
import os, glob
import csv
data_dict='/Users/macbook/Documents/RA/variation.txt'
#Function to read dictionary list, lowercase all,
#return unique existing sorted entries.

with open(data_dict, 'r') as d:
    syndrome=[word.strip().lower() for word in d]
d.close()
#print syndrome

#The program.
#syndrome=read_dictionary_list(data_dict)

f = open(sys.argv[1], 'wt')
writer = csv.writer(f)
writer.writerow( ('filename', 'match', 'snydrome words') )
total_N, positive_N=0,0
path='/Users/macbook/Documents/RA/case_study_txt'
for txtfile in glob.glob(os.path.join(path, '*.txt')):
    with open(txtfile,'r') as txtf:
        article=txtf.read()
    txtf.close()
    article=article.strip().lower()
    #print article
    found_syndrome_words=[]
    found_syndrome_trigger=0
    for word in syndrome:
    	#print (word)
        if re.search(r'\b%s\b'%word,article):
            found_syndrome_words.append(word)
            found_syndrome_trigger = 1
    total_N+=1

    if found_syndrome_trigger==1:
        writer.writerow( (os.path.basename(txtfile), "True", ','.join(found_syndrome_words) ) )
        positive_N+=1
    else:
        writer.writerow( (os.path.basename(txtfile),"False",""))
    print (total_N, positive_N)

f.close()
print total_N, positive_N
