import random as rd
import turtle as tt

many=20
length=1000/many

runner=[(0,0)]

full=[(x,y) for x in range(many) for y in range(many)]
lenfull=len(full)

tt.title("Maze Runner")
tt.screensize(50,50)
tt.setworldcoordinates(-20,-20,1020,1020)


t=tt.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(0,0)

sub=0
for k in range(many+1):
    t.penup()
    t.goto(0,sub*length)
    t.pendown()
    t.forward(1000)
    sub+=1

t.penup()
t.goto(0,0)
sub=0
t.setheading(90)

for k in range(many+1):
    t.penup()
    t.goto(sub*length,0)
    t.pendown()
    t.forward(1000)
    sub+=1

t.pencolor("blue")
t.shape("square")
t.pensize(length/2-3)
t.penup()
t.goto(length/2,-20)
t.pendown()
t.goto(length/2,length/2)



def go(k):
    i=0
    while i<k:
        last=runner[-1]
        aa=last[0]
        bb=last[1]
        
        temp1=(aa+1,bb)
        temp2=(aa-1,bb)
        temp3=(aa,bb+1)
        temp4=(aa,bb-1)
        temp=[]
        if temp1 in full and temp1 not in runner:
            temp.append(temp1)
        if temp2 in full and temp2 not in runner:
            temp.append(temp2)
        if temp3 in full and temp3 not in runner:
            temp.append(temp3)
        if temp4 in full and temp4 not in runner:
            temp.append(temp4)

        if temp==[]:
            return

        rd.shuffle(temp)

        key=temp[0]
        t.goto((key[0]*length)+(length/2),(key[1]*length)+(length/2))
        runner.append(key)
        
        i+=1

        
while len(runner) != lenfull :
    go(many/2)
    t.penup()
    rd.shuffle(runner)
    t.goto((runner[-1][0]*length)+(length/2),(runner[-1][1]*length)+(length/2))
    t.pendown()


t.penup()
##t.pensize(10)
##t.goto((length/2),(length/2))
##t.pencolor("red")
##t.dot()
##t.goto(1000-(length/2),1000-(length/2))
##t.dot()

t.penup()
t.goto(1000-(length/2),1000-(length/2))
t.pendown()
t.goto(1003,1000-(length/2))

tt.exitonclick()
