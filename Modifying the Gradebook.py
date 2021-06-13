#Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our
# visual arts class.
#Access the index of the grade for your visual arts class and modify it to be 5 points greater

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['visual arts', 93]]
gradebook[-1][-1] = (93)+5
print(gradebook)

#You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.
#Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
gradebook[2].remove(85)
print(gradebook)


#Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook = [['physics', 98], ['calculus', 97], ['poetry'], ['history', 88]]
gradebook[2].append('Pass')
print(gradebook)