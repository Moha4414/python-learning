
secret_word="Mooge"

guess=""
guess_count=0
gues_limit=3

out_gues=False
while guess !=secret_word and not(out_gues):
    
    if guess_count<gues_limit:
    
      guess=input("Enter guess:")
      guess_count+=1
    else:
        out_gues=True

if out_gues:
    print("Out of guesses , You lose")
    

else:

    print("you win")



