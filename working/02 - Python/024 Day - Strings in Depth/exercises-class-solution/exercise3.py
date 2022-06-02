secret = 'this_is_my_secret'
name = 'Max'
year_of_birth = 1982

if len(secret) < 8:
    print("secret must be at least 8 characters")
else:
    result = secret + name
    result = result[::-1]
    result = result + str(year_of_birth)
    print(result)
