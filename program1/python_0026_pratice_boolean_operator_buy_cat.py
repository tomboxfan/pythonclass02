# Requirement: A customer walks into a Pet's store, he said, 'I want a
# male cat, white or yellow
# Or a female cat, not white
# Or just a black cat
# You need to get input from console about cat gender and cat color
# You program needs to tell whether the customer wants it or not


gender = input("Is the cat male or female? ")
color = input("What's the color of the cat? ")

# the if clause contains 3 scenarios, any one of them is True, the whole if clause is True, because they are joined by 'or'
# The 3 scenarios are:
# gender == 'male' and (color == 'white' or color == 'yellow')
# gender == 'female' and color != 'white'
# color == 'black'
if gender == 'male' and (color == 'white' or color == 'yellow') or gender == 'female' and color != 'white' or color == 'black':
    print("I will take it")
else:
    print("I don't want it")
