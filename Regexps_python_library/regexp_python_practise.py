import re

regexp = 'burrito'
string = 'boorrito'
result = re.match(regexp, string)
print(result is None)

result = re.match('hedge', 'hedgehog')
print(result is None)
# The output is False,
# because there's 'hedge' in the beginning of the string 'hedgehog'

result = re.match('', 'not an empty string')  # match
print(result is None)

result = re.match('', 'anything')
print(result is None)
# %%
import re

w1 = input()
w2 = input()
if re.match(w1, w2):
    print(len(w1) * 2)
else:
    print('no matching')

#%%
string_1 = 'I love Python 3'
string_2 = 'i love Pitsaw'
string_3 = 'we love Papuan'
string_4 = 'we love php'

template = "..? love P"
for word in [string_1, string_2, string_3, string_4]:
    result = re.match(template, word)
    print(not (result is None))



# %%
def matched(template, string):
    result = re.match(template, string)
    return not (result is None)
# %%
path = 'C:\\tasks\Hyperskill\\new'
print(path)

# %%
import re

good_string = 'You learn Python 3?..'
bad_string = 'You learn Python 3?!.'
template = 'You learn Python 3\?\.\.'

print(matched(template, good_string))
print(matched(template, bad_string))

# %%
import re

# birthday of Python 3
good_string = '03.12.2008'
bad_string = '03-12-2008'
template = '03\.12\.2008'
print(matched(template, good_string))
print(matched(template, bad_string))

# %%
string = 'Annie, are you okay?!'
template = 'Annie, are you okay\\?\\!'
print(matched(template, string))

# %%
import re
template = "20[0-1][0-9]"

for year in range(2000, 2021):
    result = re.match(template, str(year))
    if not result:
        print("Error")
    else:
        print(year)

result = re.match(r'[a]', 'c[a]t')
print(result)

# %%
words_list =["AA", "1", "6f" ,"d9", "3E", "c1", "9", "9j","2jj"]
# template = r"[1-9a-fA-F][1-9a-fA-F]?"
template = r'[1-9a-fA-F]{1,2}$'
for word in words_list:
    result = re.match(template, word)
    if not result:
        print("Error")
    else:
        print("Matched")

# %%
smileys = [":)", ":-)", ":(", ":-(", ":o", ":-o",":D"]
template = r":[)(-o]{1,2}$"

for smiley in smileys:
    result = re.match(template, smiley)
    if not result:
        print("Error")
    else:
        print(smiley)

# %% Regex short hands
print(re.match('\w', 'X'))
print(re.match('\\w', 'X'))
print(re.match(r'\w', 'X'))

# %%
word = "I love Python"
pattern = r'I love Python$'
result = matched(pattern, word)
print(result)

# %%
import re

string = input()
regex = r'\$\d+'
match = re.match(regex, string)
if match:
    print('Amount found: ', match.group())
else:
    print('No match!')

# %%
import re
template = "the"
no_match_result = re.match(template, "paris is the capital of france")
print(no_match_result is None)  # the output is True
match_result = re.match(template, "the paris").span()
print(match_result)

# %%
import re


string = " "
template = r'.'
match = re.match(template, string, flags=re.IGNORECASE)
if match:
    print('Amount found: ', match.group())
else:
    print('No match!')
# %%
template = "ahoy,.me hearties!"
string = "AHOY,\nME HEARTIES!"
match = re.match(template, string, flags=re.DOTALL+re.IGNORECASE)
if match:
    print(match is not None)  # The output is True

# %%
template = r"Good (morning|afternoon|evening)"
string = input()
match = re.match(template, string)
if match:
    print(match.group())
else:
    print('No greeting!')

# %%
string = "@some_twitter_user I love dogs, @another_twitter_user!"
pattern = r'@\w+'
replaced_string = re.sub(pattern, "<AUTHOR>" , string, count=1)
final_string = re.sub(pattern, "<HANDLE>" , replaced_string, count=0)

print(final_string)
# %%
string = "She sells seashells on the seashore."

match = re.findall(r"s\w+",string)
print(match)

# %% GROUP CAPTURING WITH SEARCH OPTION
string= "Something\n<START>\nsomething\n<END>\nsomething"
pattern = r"<START>(.+)<END>"

match = re.search(pattern,string,flags=re.DOTALL)
if match:
    print(match.group(1))
else:
    print('No match!')
# %%
import re
names = input()
pattern = r"\d+"
correct_names = [name for name in re.split(r"\d+", names) if name]
print(correct_names)