current_year = int(input("what's the current year?:"))
year = int(2099)



def calculate_age (year, current_year):
    return year - current_year

result= calculate_age (year, current_year)


if current_year > year:
    print("you don't born yet")
else:
    print( "you will be this year old:", result)

