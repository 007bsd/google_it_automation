# def first_and_last(message):
#     if(len(message)==0):
#       return True
#     elif(message[0]==message[-1]):
#         return True
#     else:
#         return False
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))
#
# word = "supercalifragilisticexpialidocious"
# print(word.index('x'))

# def initials(phrase):
#     words = phrase.split()
#     result = ""
#     for word in words:
#         result += word[0].upper()
#     return result
#
# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# def student_grade(name, grade):
#
#     return ("{} received {}% on the exam".format(name, grade))
#
# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))
#
# def convert_distance(miles):
#     km = miles * 1.6
#     result = "{} miles equals {:.1f} km".format(miles, km)
#     return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for word in input_string.lower():
# 		# Add any non-blank letters to the
# 		# end of one string, and to the front
# 		# of the other string.
# 		if word !=' ':
# 			new_string = new_string+word
# 			reverse_string = word+reverse_string
# 	# Compare the strings
# 	if new_string == reverse_string:
# 		return True
# 	return False
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# def nametag(first_name, last_name):
# 	return("{} {}".format(first_name, last_name[0]))
#
# print(nametag("Jane", "Smith"))
# # Should display "Jane S."
# print(nametag("Francesco", "Rinaldi"))
# # Should display "Francesco R."
# print(nametag("Jean-Luc", "Grand-Pierre"))
# # Should display "Jean-Luc G."

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"