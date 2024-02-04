"""Program Name: CollegeAdmission.py
   Function: This program determines if a student will be admitted or rejected.
   Input:  Interactive
   Output: Accept or Reject
"""

# Get input and convert to correct data type

# Get input for test score and class rank
testScoreStr = input("Please enter the student's test score: ")  # Prompt for test score
classRankStr = input("Please enter the student's class rank: ")  # Prompt for class rank

# Convert the string representations to integers
testScore = int(testScoreStr)
classRank = int(classRankStr)

# Test using admission requirements and print Accept or Reject
# (Rest of the decision logic remains unchanged)




# Test using admission requirements and print Accept or Reject
if testScore >= 90:

	if  classRank >= 25:
		print("Accept")
	else:
		print("Reject")

elif testScore >= 80:

		if classRank >= 50:
			print("Accept")
		else:
			print("Reject")

elif testScore >= 70:

			if classRank >=75:
				print("Accept")
			else:
				print("Reject")

else:
	print("Reject")
