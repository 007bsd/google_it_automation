# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#         if home_team !=away_team:
#             print(home_team + " vs " + away_team)

# for x in [25]:
#     print(x)
# def is_valid(chrr):
#     if len(chrr) > (3):
#         return chrr
# def validate_users(users):
#   for user in users:
#     if is_valid(user):
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")
# validate_users("purplecat")

# def factorial(n):
#     result = 1
#     for x in range(1,n+1):
#         result = result*x
#     return result
#
# for n in range(9):
#     print(n, factorial(n))

# for i in range(100):
#   if i % 7 ==0:
#     print(i)

# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     if n < 1:
#         return 0
#
#     # The recursive case is adding this number to
#     # the sum of the numbers smaller than this one.
#     return (n + sum_positive_numbers(n-1))
#
# print(sum_positive_numbers(2)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# def find_factorial(number):
#     if number < 2:
#         return 1
#     return number * find_factorial(number-1)
# print(find_factorial(2))
# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     # If number is equal to 1, it's a power (base**0).
#     return False
#   if number == base:
#       return True
#   else:
#   # Recursive case: keep dividing number by base.
#     return is_power_of(number/base, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False
# def is_Power(x, y):
#     while (x%y == 0):
#         x = x / y
#     return x == 1
#
# print(is_Power(8,2)) # Should be True
# print(is_Power(64,4)) # Should be True
# print(is_Power(70,10)) # Should be False

# def is_power_of(x, y):
#     if y == 0:
#         return 1
#
#     if y >= 1:
#         return x * is_power_of(x, y - 1)
# print(is_power_of(3, 2))


# number = 1
# while number <= 7:
#     print(number, end=" ")
#     number+=1

# def show_letters(word):
# 	for letter in word:
# 		print(letter)
#
# show_letters("Hello")
# Should print one line per letter

# def digits(n):
#     count = 0
#     if n == 0:
#         return 1
#     while (n > 0):
#         n = n // 10
#         count += 1
#     return count
#
# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1
# count = 1
# while (100 / 10 > 1):
#     count += 1
#     print(count)

# def multiplication_tablemultiplication_table(n):
#     for row in range(1, n + 1):
#         for col in range(1, n + 1):
#             print(row * col, end=" ")
#         print()
#
# #multiplication_tablemultiplication_table(3)
# # Should print the multiplication table shown above
# def multiplication_table(start, stop):
# 	for x in range (start, stop+1):
# 		for y in range (start, stop+1):
# 			print(str(x*y), end=" ")
# 		print()

# multiplication_table(1, 3)
# Should print the multiplication table shown above
#
# def counter(start, stop):
# 	x = start
# 	if x > stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x)
# 			if x >= stop:
# 				return_string += ","
# 			x=x-1
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x)
# 			if x <= stop:
# 				return_string += ","
# 			x+=1
# 	return return_string


#
# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"
#
# n =10
# count = 1
# while (count < n):
#     n = n -1
#     count+=1
#     print(n)



# def decade_counter(year):
#     while year < 50:
#         year += 10
#     return year
# print(decade_counter(10))
#
# for x in range(1, 10, 3):
#     print(x)
#
# for x in range(10):
#     for y in range(x):
#         print(y)

# def votes(params):
# #     for vote in params:
# #         print("Possible option:" + vote)
# # (votes(['yes', 'no', 'may be']))

# def even_numbers(maximum):
# 	return_string = ""
# 	for x in range (2, maximum+1, 2):
# 		return_string += str(x) + " "
# 	return return_string.strip()
#
# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed
# def double_word(word):
#     new_str = word * 2
#     len_of_new_str = len(new_str)
#     return new_str + str(len_of_new_str)
#
#
# print(double_word("hello"))  # Should return hellohello10
# print(double_word("abc"))  # Should return abcabc6
# print(double_word(""))  # Should return 0

def first_and_last(message):
    print(len(message))
    if (message[0]==message[-1]):
      return True
    elif(len(message)==0):
        return True
    else:
        return False

#print(first_and_last("else"))
#print(first_and_last("tree"))
print(first_and_last(""))


