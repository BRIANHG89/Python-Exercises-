#zip() is used to combine 2 similar containers(list-list or dict-dict)


#initializing list 
questions = ['name', 'colour', 'shap']
answer = ['apple', 'red', 'a circle']

#using zip() to combine two containers
#and print values
for questions, answer in zip(questions, answer):
    print('What is your {0}? I am {1}.'.format(questions, answer))
    
    