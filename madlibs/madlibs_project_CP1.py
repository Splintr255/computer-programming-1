# name / pronoun / name noun variables
name1 = input('What is your name? ')
name2 = input('Give me a random last name: ')
name3 = input('Give me the name of a little kid: ')
name4 = input('Give me another name of a little kid: ')
name5 = input('Give me a boy name: ')

noun1 = input('Give me a random object: ')

name_noun1 = input('Give me a noun (i.e. uncle, dad, brother, etc.): ')

teacher_name = ('Mr. ' + name2)

# object / noun variables
object1 = input('Give me a noun or object: ')
object2 = input('Give me another noun or object: ')
object3 = input('Give me one last noun or object: ')

food1 = input('Give me a food: ')
food2 = input('Give me another food: ')
food3 = input('Give me one last food: ')

# verb / adverb variables
adv1 = input('Give me an adverb: ')
adv2 = input('Give me another adverb: ')

# adjective variables 
adj1 = input('Give me an adjective: ')
adj2 = input('Give me another adjective: ')
adj3 = input('Give me one last adjective: ')

# misc. variables
past_verb = input('Give me a past tense verb: ')

# story
print('One day, {0} forgot to bring their {1} to school. While at school, Mr. {2} was asking people to show the class something that they thought would describe them.'.format(name1, object1, name2), end=' ')
print("{0} brought in a {1}. {2} brought in their {3}'s {4}. The rest of".format(name3, object2, name4, name_noun1, object3), name1, "'s friends showed their items to the class.", name1, ' missed out.', end=' ')
print("It was time for the class to move on to a new subject. {0} decided that the new subject would be cooking.".format(teacher_name), end=' ')
print('{0} brought up the idea of making a {1} and {2} pizza!'.format(name5, food1, food2), str(teacher_name) + ' thought that was a great idea!', end=' ')
print(str(teacher_name) + ' {0} grabbed his cook book.'.format(adv1), str(teacher_name) + ' asked what everyone wanted it to look like?', end=' ')
print('{0} said they want it to look kind of {1}. The teacher agreed, and they all started to work on making this {1} pizza.'.format(name5, adj1), end=' ')
print('The pizza was starting to look {0} instead of {1}. The class went outside and brought this {2} looking pizza.'.format(adv2, adv1, adj2), end=' ')
print('They placed the {0} looking pizza into the oven. After 20 minutes, the pizza turned into a {1} looking {2}.'.format(adj2, adj3, food3), end=' ')
print('They pulled out the ', food3, ' and it turned into a {0}, and {1} the school.'.format(noun1, past_verb ), end=' ')
print('\n')
print('\t''THE END')
print("You're welcome for reading. (:") 