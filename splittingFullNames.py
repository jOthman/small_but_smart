# 
# Full names Splitter
#
# Version: 1.0.0
# 
# a small program to split a list of full names (of any length)
# into the form of:
# FirstName,MiddleName,LastName,FamilyName
# 
# You can have your full names separated in 4 columns 
# just by pasting the resulting file in an excel sheet
# (you just need to find the dot character "."
# and replace it by the space character " ")
# 
# Note:
# If the length of the full name is greater than 4,
# you will not lose any name; all names will be 
# concatenated by a dot "." in the LastName
#
#
# Copyright (c) 2017-2018 by Othman Aljeezani.  All rights reserved.
# 
# 


def processing(line):

	"""
		Description:
			This function is created to process a full name
			and split it to: 
			first name, middle name, last name and family name

		Arguments:
			line -- the string that contains the full name

		Returns:
			a string that contains the full name after separating it,
			and it will be in the following format:

			FirstName,MiddleName,LastName,FamilyName

		Notes:
			* In the case the full name has only one name,
			  it will be: FirstName,,,
			* If it has two names, 
			  it will be: FirstName,,,FamilyName
			* If it has three names,
			  it will be: FirstName,MiddleName,,FamilyName
			* If it has four names, (the perfect case)
			  it will be: FirstName,MiddleName,LastName,FamilyName
			* If it has more than four names,
			  it will be: FirstName,MiddleName,LastName,FamilyName
			  
			  However, the last name will contain all extra names
			  separated by a dot (there will be a dot "." between names),
			  so you can find and replace the dot with a space later.
	"""

	# Deleteing the return character at the end of the full name
	line.replace("\n", "");
	# Deleting empty spaces at the start and the end of the full name
	line.strip();	
	### START OF THE LOGIC ###
	# The logic of spilitting FullName into fName, mName, lName, and familyName
	fName = "";
	mName = "";
	lName = "";
	family = "";
	# Creating a list by spliting the full name using the space as a delimiter
	myList = line.split();
	count = len(myList);
	if(count == 1):
		fName = myList[0];
	elif(count == 2):
		fName = myList[0];
		family = myList[1];
	elif(count == 3):
		fName = myList[0];
		mName = myList[1];
		family = myList[2];
	elif(count == 4):
		fName = myList[0];
		mName = myList[1];
		lName = myList[2];
		family = myList[3];
	# Concatenating all names in the last name
	else:
		fName = myList[0];
		mName = myList[1];
		index = 2;
		while(index < count-1):
			# concatenating names and putting "." between them
			lName = lName + myList[index] + ".";
			index = index + 1;
		# removing the last character (a dot at the end)
		lName = lName[:-1];
		family = myList[count-1];
	# Writing the full name as 4 parts f, m, l, family saperated by commas
	line = fName + "," + mName + "," + lName + "," + family;
	#### END OF THE LOGIC ###
	return line;

"""
	the main is used to read the names from a text file
	and print the result into a text file
"""
if __name__ == "__main__":
	# creating the output text file
	outputFile = open("names_output.txt", "w");
	# reading the input text file
	inputFile = open("names.txt","r");
	# reading names line by line
	for line in inputFile:
		# processing each line to separate it
		newLine = processing(line);
		# writing each line to the output file
		outputFile.write(newLine + "\n");
	# closing the output file
	outputFile.close();
	print("Names are converted successfully,\n" + 
		  "check (names_output.txt) file.");