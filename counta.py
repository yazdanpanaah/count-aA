lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", 
"Nevada",'a']
#this is print number of both a and A togheter
print(sum(list(map(lambda x : sum([ i.count('a') or i.count('A') for i in x ]) ,lst1))))

#this is print number of both a and A and put them in list as seprated numbers
print([sum(j) for j in zip( *list(map(lambda x :[sum( i.count('a') for i in x ) , sum( i.count('A') for i in x)] ,lst1)) )])


