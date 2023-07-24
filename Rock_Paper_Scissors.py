import random
name=input('Enter player name:')
print(name,'v/s Computer')
print('All the best!',name)
p=0
c=0
n=int(input('How many games you want to play?:'))
print('r for ROCK\np for PAPER\ns for SCISSOR')
l=['r','p','s']
for i in range(1,n+1):
  print('Game',i)
  ch=input('Enter your choice:')
  ch=ch.lower()
  x=l.index(ch)
  # print(x)
  y=random.randint(0,2)
  # print(y)
  print("Computer's choice:",l[y])
  if (y==0 and x==2) or (y==1 and x==0) or (y==2 and x==1):
    c=c+1
  elif(x==0 and y==2) or (x==1 and y==0) or (x==2 and y==1):
    p=p+1
  print('Scores after game',i,':',name,"'s:",p,"Computer's:",c) 
  print('')  
if p>c:
  print('Congratulations',name,'You are the winner!!!')
elif p==c:
  print("It's a draw")
else:
  print('Well played, Better luck next time')    
