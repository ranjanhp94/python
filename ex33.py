states = {
'Oregon': 'OR' ,'Florida': 'FL' ,'California': 'CA',
'New York': 'NY','Michigan': 'MI'}

cities = {'CA': 'San Francisco','MI': 'Detroit','FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

print('-' * 10)
for state, abbr in states.items():
    print(f"{state} is abbreviated {abbr}")

print('-' * 10)
for abbr, city in cities.items():
    print(f"{abbr} has the city {city}")

for state, abbr in states.items():
	print(f"{state} state is abbreviated {abbr} and has city {cities[abbr]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print('Sorry, no Texas')

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
