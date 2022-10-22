print('Welcome to Aadi Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=6
 
if answer.lower()=='yes':
    answer=input('Question 1: In which country do you live?')
    if answer.lower()=='india':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: In which state do you live? ')
    if answer.lower()=='madhya pradesh':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: In which city do you live?')
    if answer.lower()=='indore':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4: What is the capital of India?')
    if answer.lower()=='delhi':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 5: What is the capital of Madhya Pradesh?')
    if answer.lower()=='bhopal':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 6:What is the full form of MRF?')
    if answer.lower()=='madaras ruber factory' :
        score += 1
        print('correct')
    else:
        print('Wrong Answer ;(')
            
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
print('THANKS FOR PLAYING!')
