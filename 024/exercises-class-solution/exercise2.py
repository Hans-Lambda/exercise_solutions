# ###TASK 1

text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

# ###TASK 2

print(text[0])
print(text[-1])

# ###TASK 3

slice = text[:3]
print(slice.upper())

# ###TASK 4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital "
count = text.count('B')
print(count)

# ###TASK 5

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(text[-10:])

# ### TASK 6

text = "---Python programming---"
print(text.strip('-'))

# ### TASK 7

firstname = "Mary"
lastname = "Mat"

print(f'Firstname: {firstname}\nLastname: {lastname}')
