name1=input("enter name of first person: ")
name2=input("enter name of second person: ")
combine_string=name1+name2
lowercase_string=combine_string.lower()

t=lowercase_string.count('t')
r=lowercase_string.count('r')
u=lowercase_string.count('u')
e=lowercase_string.count('e')
true=t+r+u+e

l=lowercase_string.count('l')
o=lowercase_string.count('o')
v=lowercase_string.count('v')
e=lowercase_string.count('e')
love=l+o+v+e
 
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"your score is {love_score} ur perfect pair")
elif love_score>=40 and love_score<=50:
    print(f"your love score is {love_score} and u r alright together")
else:
    print(f"your love scoreis {love_score}")