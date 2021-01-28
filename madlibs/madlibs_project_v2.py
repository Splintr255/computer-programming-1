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
object1 = input('Give me an object: ')
object2 = input('Give me another object: ')
object3 = input('Give me one last object: ')

food1 = input('Give me a food: ')
food2 = input('Give me another food: ')
food3 = input('Give me one last food: ')

# adjective variables 
adv1 = input('Give me an adjective ending in "ly": ')
adv2 = input('Give me another adjective ending in "ly": ')

adj1 = input('Give me an adjective: ')
adj2 = input('Give me another adjective: ')
adj3 = input('Give me one last adjective: ')

# misc. variables
past_verb = input('Give me a past tense verb: ')

# story
story = f"""One day, {name1} forgot to bring their {object1} to school. While at school, Mr. {name2} was asking people to show the class something that they thought would describe them.
{name3} brought in a {object2}. {name4} brought in their {name_noun1}'s {object3}. The rest of {name1}'s friends showed their items to the class. {name1} missed out.
It was time for the class to move on to a new subject. {teacher_name} decided that the new subject would be cooking.
{name5} brought up the idea of making a {food1} and {food2} pizza! {teacher_name} thought that was a great idea!
{teacher_name} {adv1} grabbed his cook book. {teacher_name} asked what everyone wanted it to look like?
{name5} said they want it to look kind of {adj1}. The teacher agreed, and they all started to work on making this {adj1} pizza.
The pizza was starting to look {adv2} instead of {adv1}. The class went outside and brought this {adj2} looking pizza.
They placed the {adj2} looking pizza into the oven. After 20 minutes, the pizza turned into a {adj3} looking {food3}.
They pulled out the {food3} and it turned into a {noun1}, and {past_verb} the school.
""".replace('\n', ' ')

print(f'{story}\n\n\tTHE END\nYou\'re welcome for reading. (:')
