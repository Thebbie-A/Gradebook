#You also have your grades from last semester, stored in last_semester_gradebook.
#Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using +
# to have one complete grade book.
#Print full_gradebook to see our completed list.

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88]]
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)