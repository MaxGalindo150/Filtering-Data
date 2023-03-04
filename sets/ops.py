A = {'COL', 'MEX', 'BOL'}
B = {'PER', 'BOL', 'BRZ'}

# Union
C = A.union(B)
print(A | B) # other way to make th union

# Intersection
I = A.intersection(B)
print(A & B) # other way to make the intersection 


# Difference 
D1 = A.difference(B)
D2 = B.difference(A)

print(A-B)
print(B-A)

# symmetric difference
S = A.symmetric_difference(B)
print(A ^ B)
