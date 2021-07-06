#read files
import csv

def data(csvfile): #opens the information stored in database as a list of dictionaries
	path = 'C:/Users/Soffi/Desktop/liza/dna/databases/' + csvfile
	with open(path) as file:
		raw_database = csv.DictReader(file)
		database = list(raw_database)
		return database

def sequence(file): #opens files to be matched to database
	path = 'C:/Users/Soffi/Desktop/liza/dna/sequences/' + file
	with open(path) as raw_seq:
		seq = raw_seq.read()
	return seq

###################################################################################################################
if __name__ == '__main__':
	#empy (for now) variables
	seqs = {}
	people = [] #contains dictionaries of info about people inside the database
	per_vals = [] #same as people, in the form of list
	names = [] #kinda unzips per_vals. creates list of names of people inside the database
	vals = [] #creates list of the count of dna sequences of people inside the database

	#read files
	database = data(input('plaese enter database: '))#calls "data" function and creates small database
	seq = sequence(input('please enter file name: ')) #calls "sequence" function and makes data usable

	#count sequences
	dna = dict(database[1]).keys()
	dna = list(dna)
	dna = dna[1:]

	for dat in dna:
		index = 0
		real_count = 0
		temp_count = 0
		while index < len(seq):
			if seq[index:index + len(dat)] == dat:
				temp_count = temp_count + 1
				index = index + len(dat)
			else:
				if temp_count > real_count:
					real_count = temp_count
				temp_count = 0
				index = index + 1
		seqs[dat] = str(real_count)

	suspect = list(seqs.values()) #contains info of each "suspect"
#match sequences

for line in database: #creates dictionaries with info of each person inside the database
	person = dict(line)
	people.append(person)

for person in people: # converts data inside dictinaries into lists
	person = person.values()
	per_vals.append(list(person))
#__________________________________________

#match lists

for person in per_vals:
	names.append(person[0])
	vals.append(person[1:])

for person in vals:
	if suspect in vals:
		criminal = vals.index(suspect)
		print(names[criminal])
	else:
		print("no match")
	break