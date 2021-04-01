import time
import threading
def quiz():
    global timer
    timer = 25
    for x in range(25,0,-1):
        timer = timer -1
        time.sleep(1)
    print("\nGame over")    
    if score == 5:
        print("The Performance is : Excellent") 
    elif score == 4:
        print("The Performance is : very good") 
    elif score == 3:
        print("The Performance is : Average") 
    elif score == 2:
        print("The Performance is : poor")
    elif score == 1:
        print("The Performance is : Very poor")
    else:
        print("Rejected")
    print("The score is :", score)
quiz_thread = threading.Thread(target = quiz )
quiz_thread.start()
Mode = input("Choose mode : \na. Easy  \nb. Medium \nc. Hard \nmode :")

while timer > 0:
    if Mode== "a" or Mode== "Easy":
        score = 0
    # Q 1.
        time.sleep(.1)
        ans = input("What is capital of India ?  \na . Kolkata \nb. Chennai \nc. Delhi \nd. Kashmir \nans:")
        time.sleep(.1)
        if ans == "c" or ans == "Delhi":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            print("Score", score)
            print("\n")
        time.sleep(.1)         
        if timer == 0:
            break
    # Q 2.
        time.sleep(.1)
        ans = input("What is capital of U.P. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "b" or ans == "Lucknow":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            print("Score", score)
            print("\n")
        time.sleep(.1)    
        if timer == 0:
            break
        # Q 3.
        time.sleep(.1)
        ans = input("What is capital of WestBengal ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Kolkata":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break    
    # Q 4.
        time.sleep(.1)
        ans = input("What is capital of Maharashtra. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Mumbai \nanswer:")
        time.sleep(.1)
        if ans == "d" or ans == "Mumbai":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break    
    # Q 5.
        time.sleep(.1)
        ans = input("What is capital of M.P. ?  \na . Bhopal \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Bhopal":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break
        break

    elif Mode== "b" or "Medium":
        score = 0
    # Q 1.
        time.sleep(.1)
        ans = input("What is capital of India ?  \na . Kolkata \nb. Chennai \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "c" or ans == "Delhi":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1)         
        if timer == 0:
            break
    # Q 2.
        time.sleep(.1)
        ans = input("What is capital of U.P. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "b" or ans == "Lucknow":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1)    
        if timer == 0:
            break
        # Q 3.
        time.sleep(.1)
        ans = input("What is capital of WestBengal ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Kolkata":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break    
    # Q 4.
        time.sleep(.1)
        ans = input("What is capital of Maharashtra. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Mumbai \nanswer:")
        time.sleep(.1)
        if ans == "d" or ans == "Mumbai":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1) 
        if timer == 0:
            break   
    # Q 5.
        time.sleep(.1)
        ans = input("What is capital of M.P. ?  \na . Bhopal \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Bhopal":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break
        break

    elif Mode== "c" or "Hard":
        score = 0
    # Q 1.
        time.sleep(.1)
        ans = input("What is capital of India ?  \na . Kolkata \nb. Chennai \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "c" or ans == "Delhi":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 1
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break         

    # Q 2.
        time.sleep(.1)
        ans = input("What is capital of U.P. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "b" or ans == "Lucknow":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 2
            print("Score", score)
            print("\n")
        time.sleep(.1) 
        if timer == 0:
            break   

        # Q 3.
        time.sleep(.1)
        ans = input("What is capital of WestBengal ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Kolkata":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 2
            print("Score", score)
            print("\n")
        time.sleep(.1) 
        if timer == 0:
            break   
    # Q 4.
        time.sleep(.1)
        ans = input("What is capital of Maharashtra. ?  \na . Kolkata \nb. Lucknow \nc. Delhi \nd. Mumbai \nanswer:")
        time.sleep(.1)
        if ans == "d" or ans == "Mumbai":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 2
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break    
    # Q 5.
        time.sleep(.1)
        ans = input("What is capital of M.P. ?  \na . Bhopal \nb. Lucknow \nc. Delhi \nd. Kashmir \nanswer:")
        time.sleep(.1)
        if ans == "a" or ans == "Bhopal":
            score += 1
            print("Correct")
            print("score:", score)
            print("\n")
        else :
            print("Incorrect")
            score -= 2
            print("Score", score)
            print("\n")
        time.sleep(.1)
        if timer == 0:
            break
        break