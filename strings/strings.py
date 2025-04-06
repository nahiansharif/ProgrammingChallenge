# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

s = "hello, world!"
word = s.split(" ")
# this splits the word when there's a space. 

s = "I am from Planet Namik"
word = s.split()
# this split word based on space by default. 

word = s.split("a")
# this will split string when there's a. 

upper = s.upper()
lowercase = upper.lower()
# upper and lowercase 

import re 
cleantext = re.sub(r'[^a-zA-Z0-9\s]', '', s)
# this function returns only characters and numbers. anything else is being replaced with nothing

size = len(s)
lastChar = s[-1]

sliced = s[0:5]
name = "lalu"
greetings = sliced + ", " + name
# concatenated 

# add space to every character and join. 
balloon = "Sammy has a balloon"
joinStr = " ".join(balloon)
 #Ouput   S a m m y  h a s  a  b a l l o o n


s = "Nahian Sharif"

#convert each character into array of lists. 
char = list(s)
#join all characters into one string
joinedStr =  "". join(char ) 


s = "Ali is the king"
s = s.replace("Ali", "Kobalis")
s = s.replace("the ", "")
# replace functionalities

char2int = ord("N")
int2Char = chr(65)
# convert letter to number & number to letter. 


# page 
# Counts the occurrences of a substring with optional start and end position

text = "the quick brown fox jump over the lazy white dog"
countThe = text.count("the")


# Returns the index of the first occurrence of a substring or returns -1 if the substring is not found

email = "naina@gmail.com"
atIndex = email.find("@")
username = email[:atIndex]



# Converts the string to all lowercase or uppercase 

txt = "Hello World"

low = txt.lower()
upperCase = txt.upper()

#140

# Replaces old substring with new substring 

# Removes withspace or optional characters 

# Splits a string separated by whitespace or an optional separator. Returns a list 

# Replaces tabs with spaces. 

# Bool
# String consists of only alphanumeric characters (no symbols) 

# String consists of only alphabetic characters (no symbols)

# String’s alphabetic characters are all lower case 

# String consists of only numeric characters 

# String consists of only whitespace characters 

# String is in title case  

# String’s alphabetic characters are all upper case

