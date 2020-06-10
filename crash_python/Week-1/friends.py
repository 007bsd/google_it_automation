# friends = ['Alex', 'Megan', 'John']
# for friend in friends:
#     print("Hi ", friend)
#
# for i in range (10):
#     print("Hello")
#
# ratio = (1 + (5 ** (1 / 2)) / 2)
# disk_size = 16*1024*1024*1024
# sector_size = 512
# sector_amount = disk_size/sector_size
#
# print(sector_amount)
#
# total = 2048 + 4357 + 97658 + 125 + 8
# files = 5
# average = total / files
# print("The average size is " + str(average))
#
#
# def month_days(month, day):
#   print(f"{month} has {day} days", month, str(day))
# month_days("June", 30)
# month_days("July", 31)
#
#
#
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize // block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize % block_size
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if (partial_block_remainder > 0 and full_blocks > 0):
#
#         return (block_size*2)*full_blocks
#     return block_size
#
# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192


# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color
#
#
# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown

# def exam_grade(score):
# 	if score > 95:
# 		grade = "Top Score"
# 	elif score >= 60:
# 		grade = "Pass"
# 	else:
# 		grade = "Fail"
# 	return grade
#
# print(exam_grade(65)) # Should be Pass
# print(exam_grade(55)) # Should be Fail
# print(exam_grade(60)) # Should be Pass
# print(exam_grade(95)) # Should be Pass
# print(exam_grade(100)) # Should be Top Score
# print(exam_grade(0)) # Should be Fail

#
# def format_name(first_name, last_name):
# 	string = "Name: "+last_name + " " + first_name
# 	return string
#
#
# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"
#
# print(format_name("", ""))
# # Should return an empty string


# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2) >= len(word1) and len(word2) >= len(word3):
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)
#
#
# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))


# def fractional_part(numerator, denominator):
# # 	# Operate with numerator and denominator to
# # # keep just the fractional part of the quotient
# # 	if denominator == 0:
# # 		return 0
# # 	else:
# # 		return ((numerator / denominator) - int(numerator / denominator))
# #
# # print(fractional_part(5, 5)) # Should be 0
# # print(fractional_part(5, 4)) # Should be 0.25
# # print(fractional_part(5, 3)) # Should be 0.66...
# # print(fractional_part(5, 2)) # Should be 0.5
# # print(fractional_part(5, 0)) # Should be 0
# # print(fractional_part(0, 5)) # Should be 0

# def sum(x, y):
# 	return (x + y)
#
#
# print(sum(sum(1, 2), sum(3, 4)))

# def month_days(month, day):
#   print(f"{month} has {day} days")
# month_days("June", 30)
# month_days("July", 31)

# def count_down(start_number):
# # #   while (start_number > 0):
# # #     print(start_number)
# # #     start_number -= 1
# # #   print("Zero!")
# # #
# # # count_down(3)

# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	n = start
# 	while n <= end:
# 		print(n)
# 		n += 1
# print_range(1, 5)


# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor+=1
#   return "Done"
#
# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT

# def is_power_of_two(n):
# 	# Check if the number can be divided by two without a remainder
# 	while n % 2 == 0:
# 		if n == 0:
# 			return False
# 		n = n / 2
# 	# If after dividing by two the number is 1, it's a power of two
# 	if n == 1:
# 		return True
# 	return False
#
#
# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False

# def sum_divisors(n):
# 	sum = 0
# 	div = 1
# 	while n > div:
# 		if n % div == 0:
# 			sum = sum + div
# 			div = div + 1
# 		else:
# 			div = div + 1
# 	return sum
#
# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114
#

# def multiplication_table(number):
# 	# Initialize the starting point of the multiplication table
# 	multiplier = 1
# 	# Only want to week-3 through 5
# 	while multiplier <= 5:
# 		result = number * multiplier
# 		# What is the additional condition to exit out of the week-3?
# 		if result > 25 :
# 			break
# 		print(str(number) + "x" + str(multiplier) + "=" + str(result))
# 		# Increment the variable for the week-3
# 		multiplier += 1
#
# multiplication_table(3)
# # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
#
# multiplication_table(5)
# # # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
#
# multiplication_table(8)
# # # Should print: 8x1=8 8x2=16 8x3=24

# def square(n):
#     return n*n
#
# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += square(n)
#     return sum
#
# print(sum_squares(10)) # Should be 285

def factorial(n):
    result = 1
    for num in range(1, n+1):
        result = result *num
    return result
print(factorial(5))
for n in range(5):
  print(n, factorial(n))
