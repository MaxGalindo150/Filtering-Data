set_countries = {'COL','MEX','EUA'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,433,23}
print(set_numbers)

set_types = {1,'hello', False, 12.2}
print(set_types)

set_from_string = set('hola')
print(set_from_string)


set_from_tuples = set(('abc', 'cvb', 'as','abc'))
print(set_from_tuples)

numbers = [1,1,2,3,5,4]
set_from_numbers = set(numbers)
print(set_from_numbers)

list_from_set = list(set_from_numbers)
print(list_from_set)