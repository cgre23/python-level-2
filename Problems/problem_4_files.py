"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""
countries = []
# Todo: Read data/countries.txt and save all countries
with open('data/countries.txt', 'r') as file:
    for country in file.readlines():
        countries.append(country.strip())
print(len(countries))
# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Todo: Print the number of countries that start with the letter

# Todo: Create text file that lists the countries starting with the letter
