import re

log = "The error for the log to find the logs entry [12345] Bad error"

find_index = log.index("[")
#print(log[find_index+1:find_index+6])

regex = r"\[(\d+)\]"
result = re.search(regex, log)
#print("regex result is {}".format(result[1]))

result1 = re.search(r"cat", "plaza")
result2 = re.search(r"^cat", "catter")
result3 = re.search(r"ol$", "dettol")
result4 = re.search(r"p....in", "penguin")


def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

#print(check_aei("academia")) # True
#print(check_aei("aerial")) # False
#print(check_aei("paramedic")) # True

#print(re.search(r"p.ng", "Penguin", re.IGNORECASE))

#
# print(re.search(r"[Pp]ython", "Python"))
# print(re.search(r"[a-z]way", "the end of the highway"))
# print(re.search(r"[a-zA-z0-9]oudy", "The weather is 9loudy"))

def check_punctuation (text):
  result = re.search(r"[.,:;?!]", text)
  return result != None

# print(check_punctuation("This is a sentence that ends with a period.")) # True
# print(check_punctuation("This is a sentence fragment without a period")) # False
# print(check_punctuation("Aren't regular expressions awesome?")) # True
# print(check_punctuation("Wow! We're really picking up some steam now!")) # True
# print(check_punctuation("End of the line")) # False

# print(re.search(r"[^a-zA-z]", "The is with the space"))
# print(re.search(r"[^a-zA-z ]", "The is with the space."))  # with the space
# print(re.search(r"cat|dog", "I like cats and dogs."))
# print(re.findall(r"cat|dog", "I like cats and dogs."))  # find all

# print(re.search(r"Py.*n", "Python Programming"))  # greedy
# print(re.search(r"Py[a-z]*n", "Python Programming")) # non greedy
#
#print(re.search(r"o+l+", "goldgold"))
# print(re.search(r"o+l+", "woolly"))

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True

# print(re.search(r"p?each", "I like one in each"))
# print(re.search(r"p?each", "I like one in peach"))

# print(re.search(r"\.com", "mydomain.com"))
#
# print(re.search(r"\w*", "This is regex"))
#
# print(re.search(r"\w*", "This123is123regex"))

import re
def check_character_groups(text):
  result = re.search(r"\w+\s\w+", text)
  return result != None

# print(check_character_groups("One")) # False
# print(check_character_groups("123  Ready Set GO")) # True
# print(check_character_groups("username user_01")) # True
# print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# print(re.search(r"A.*a", "Argentina"))
# print(re.search(r"^A.*a$", "Ajabejan"))

pattern = r"[a-zA-Z_][a-zA-z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))

def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ].*[!?.]$", text)
  return result != None
#
# print(check_sentence("Is this is a sentence?")) # True
# print(check_sentence("is this is a sentence?")) # False
# print(check_sentence("Hello")) # False
# print(check_sentence("1-2-3-GO!")) # False
# print(check_sentence("A star is born.")) # True

def check_web_address(text):
  pattern = r"^[\w*].*[\.][a-zA-Z]*$"
  result = re.search(pattern, text)
  return result != None

# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True



def check_time(text):
  pattern = r"^[1-9].*[:][0-5][0-9][am|AM|pm|PM|\s]"
  result = re.search(pattern, text)
  return result != None

# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False

def contains_acronym(text):
  pattern = r"[\(].*[A-Za-z0-9+][\)]"
  result = re.search(pattern, text)
  return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

result_group1 = re.search(r"^(\w*), (\w*)$", "Lovely, Ida")
# print(result_group1)
# print(result_group1.group())
# print(result_group1[1])
# print(result_group1[2])

def rearrnage_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrnage_name("Lovely, Ida"))
print(rearrnage_name("Myname"))
print(rearrnage_name("This is working"))

print(re.search(r"[a-zA-Z]{5}", "A ghost" ))
print(re.findall(r"[a-zA-Z]{5}", "A scary ghost" ))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost apperead" ))

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return "Not matched"
    return result[1]


log = "The error for the log to find the logs entry [162773] Bad error"
print(extract_pid(log))

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s(\b[A-Z]{5,}\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,;:\-\']"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  #DEBUG CODE GOES HERE


  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False

import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails,
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)
  # Convert the datetime object to string,
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime(r"%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29







