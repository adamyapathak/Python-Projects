print('Welcome to Aadi Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=10
 
if answer.lower()=='yes':
    answer=input('Question 1:What is the capital of United States of America ?')
    if answer.lower()=='washington dc':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2:When India got freedom from britishers ? ')
    if answer.lower()=='15 august 1947':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3:Which game is the national game of England ?')
    if answer.lower()=='cricket':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4:Who is the founder of Apple ?')
    if answer.lower()=='steve jobs':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 5:Who is the president of U.S.A ?')
    if answer.lower()=='joe bidon':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 6:What is the shortcut key for copy in mac ?')
    if answer.lower()=='command+c' :
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 7: Who is the founder of PYTHON programming language?')
    if answer.lower()=='guido van rossum' :
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 8: What is the full form of iit ?')
    if answer.lower()=='indian institutes of technology' :
        score += 1
        print('correct')
    else:   
        print('Wrong Answer :(')

    answer=input('Question 9:What is the full form of ips ?')
    if answer.lower()=='indian police service' :
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 10:What is the full form of iim ?')
    if answer.lower()=='indian institutes of management ' :
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')



 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
print('THANKS FOR PLAYING!')
