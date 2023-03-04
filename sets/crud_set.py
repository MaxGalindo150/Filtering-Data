set_countries = {'COL','MEX','EUA'}

size = len(set_countries)
print(size)

print('COL' in set_countries)
print('FRA' in set_countries)

# add
set_countries.add('FRA')
print(set_countries)

# update
set_countries.update({'ARG', 'BRZ', 'FRA'})
print(set_countries)

# remove 
set_countries.remove('COL')
print(set_countries)

set_countries.discard('ARG')
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))

