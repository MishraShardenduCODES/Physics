import math as mt

def chk_prime(num):
  if(num == 1 or num == 0):
    print(str(num)+" is neither prime nor composite",end="\n");
  else :
    stpr=0;
    sq = mt.floor(mt.sqrt(num));
    for i in range(2,sq+1) :
      if(num%i == 0):
        stpr=1
        break
    if(stpr):
      print(str(num)+" is a composite number! ",end="\n");
    else:
      print(str(num)+" is a prime number! ",end="\n"); 

while(1) :
  a = str(input("Tell a number (TYPE EXIT TO LEAVE): "))
  if(a.lower() == "exit") :
    print("Exiting The Program !!");
    break;
  else:
    chk_prime(int(a));
