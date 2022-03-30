'''- Tuples sind unveränderlic
    - unterstützen aber Indexing'''
my_tuple = ()
print('my_tuple : ' , type( my_tuple ))

another_tuple = 'Frank', 'Sabine', 'Franzi'
print('\n another_tuple :', type(another_tuple))
print('Index 1 von another_tuple :', another_tuple[1])

an_tuple = ('cat',) # das Komma ist der Unterschied zwischen tuple und string
print('\n an_tuple : ' , type(an_tuple))
not_tuple = ('cat')
print('not_tuple : ' ,type(not_tuple))

#another_tuple[3] = 'Peter' # TypeError weil unveränderlich


