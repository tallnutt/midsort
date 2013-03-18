from Bio import SeqIO, pairwise2
import sys



#example: C:\Python27>midsort31.py trnlmid.fna newctrnl.fna

#sorts different mids in a fasta sequence file into separate output files named after the mid ids.
#uses mids with one mismatch and/or start gap from missmatch mid file
#to run, type: 'midsorter31.py midfile inputfile ' at windows command prompt in the python folder.
#data files must be in the same folder. output will be in the same folder
#where midfile is a fasta file of all the mid sequences with mid name as the id
#and inputfile is the fasta format sequence data to be sorted


# summary of number of each mid found is saved as 'midcounts.txt'
#deletes also next 19 bp to delete m13 - well most of it anyway, given there will be some homopolymer errors
#nb mid file must have two blank lines at start
# now uses pairwise2 module to allow mismatches, mm1 = mid mismatch, mm2 = m13 mismatch
#nb can also delete m13 using separate script- m13del.py

midfile = sys.argv[1] # with one mismatch in each

fastafile = sys.argv[2]

#size1 = sys.argv[3]


#print size1

c = 0

midname = "mid0"

midtot=0
k=0

for midseq in SeqIO.parse(midfile,"fasta"):
	print midseq.id
	print midseq.seq
	c = c+1
	
	infile = file(fastafile) #enter fasta data file here
	#raw_input()#debug

	for line in SeqIO.parse(infile,"fasta"):

		seq1 = line.seq[0:15]
		hit1 = seq1.find(midseq.seq) #reports -1 if string not found, otherwise the string position

		#size2 = len(line.seq)
		#print line.id
		#print line.seq
		#print size1
		#print size2
		#raw_input()#debug
		

		if hit1 <> -1:  #
			
			print "hit " + str(k)		

			#raw_input()#debug

			k=k+1
			item = ">"+ str(line.id) +"\n" + str(line.seq[hit1 + 10 + 19:]) + "\n" #nb strips off mid (10) and m13 (19)
			f = open(midseq.id + ".fna",'a')
			f.write(item + '\n')
			f.close()



	#open and append summary file
		

	j = open("midcounts.txt",'a')
	itemb = str(midseq.id) + "   " + str(midseq.seq) + "   " + str(k) + "\n"
	j.write(itemb)
	j.close()

	k=0

		






