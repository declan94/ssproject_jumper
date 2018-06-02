import cv2 as cv
import numpy as np
import math

def phi(a,b):
    return math.exp(-100*(abs(int(a[0])-int(b[0]))+abs(int(a[1])-int(b[1]))+abs(int(a[2])-int(b[2])))**4)

def change_to_gray(img,theta):  #new record use 100 other use 200
    t_gray=0.299*img[:,:,2]+0.587*img[:,:,1]+0.114*img[:,:,0]
    gray=np.where(t_gray<theta,0,255)
    return gray

def check_end(img):
    fliter=cv.imread("./final.PNG")
    sum=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum+=phi(fliter[i,j,:],img[i+1500,j+410,:])
            count+=1
    print(sum)
    print(count)
    return sum>70000


def check_new_record(img):
    fliter=cv.imread("./record.PNG")
    sum=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum+=phi(fliter[i,j,:],img[i+230,j+430,:])
    print(sum)
    print(count)
    return sum>15000

def choose_number(x,fliter_x,y,fliter_y):
   # return abs(x-fliter_x)<50 and abs(y-fliter_y)<50
    return abs(x-fliter_x)<50

def check_score_window(bmp):
    ex=[0,0]
    count=0
    var=[0,0]
    for i in range(0,bmp.shape[0]):
        for j in range(0,bmp.shape[1]):
            if(bmp[i,j]>=200):
                ex[0]+=i
                ex[1]+=j
                count+=1
    if count==0:
        return -1
    ex[0]/=count
    ex[1]/=count
    for i in range(0,bmp.shape[0]):
        for j in range(0,bmp.shape[1]):
            if(bmp[i,j]>=200):
                var[0]+=(bmp[i,j]-ex[0])**2
                var[1]+=(bmp[i,j]-ex[1])**2
    var[0]/=count
    var[1]/=count

    number=-1
    #judge number here
    if choose_number(var[0],32221,var[1],38811):  #2 or 5
        number=2
    elif choose_number(var[0],30002,var[1],39662): 
        number=6
    elif choose_number(var[0],35884,var[1],28703):
        number=1
    elif choose_number(var[0],40472,var[1],28762):
        number=7
    elif choose_number(var[0],29865,var[1],34285):
        number=4
    else:
        number=-1

    if number==2:
        col=bmp.shape[1]
        col=int(col/2)
        temp=bmp[:,:col]
        cv.imwrite("./temp.bmp",temp)
        temp_exp_row=0
        temp_count=0
        for i in range(0,temp.shape[0]):
            for j in range(0,temp.shape[1]):
                if temp[i,j]>200:
                    temp_exp_row+=i
                    temp_count+=1
        temp_exp_row/=temp_count
        row=int(bmp.shape[0]/2)
        if temp_exp_row<row:
            number=5
        else:
            number=2

    print(var)

    return number

def check_score(bmp):
    window=bmp
    center=window[:,460:600]
    cv.imwrite('./center.bmp',center)
    c=check_score_window(center)
    print('center',c)
    even=[-1,-1,-1,-1,-1,-1,-1,-1] #8
    odd=[-1,-1,-1,-1,-1,-1,-1] #7
    if c==-1 : #even
        print('even')
        now=window[:,520:650]
        cv.imwrite("./cv1.bmp",now)
        c=check_score_window(now)
        even[4]=c
        print(c)
        now=window[:,390:520]
        cv.imwrite("./cv2.bmp",now)
        c=check_score_window(now)
        even[3]=c
        print(c)
        now=window[:,250:380]
        c=check_score_window(now)
        if c==-1:
            return 10*even[3]+even[4]
        even[2]=c
        now=window[:,660:790]
        c=check_score_window(now)
        even[5]=c
        return 1000*even[2]+100*even[3]+10*even[4]+even[5]

    else:   #odd
        print('odd')
        odd[3]=c
        now=window[:,355:475]
        c=check_score_window(now)
        if c==-1:
            return odd[3]
        odd[2]=c
        now=window[:,605,725]
        c=check_score_window(now)
        odd[4]=c
        now=window[:,230:350]
        c=check_score_window(now)
        if now==-1:
            return odd[2]*100+odd[3]*10+odd[4]
        odd[1]=c
        now=window[:,725:850]
        c=check_score_window(now)
        odd[5]=c
        return 10000*odd[1]+odd[2]*1000+odd[3]*100+odd[4]*10+odd[5]
        

def check_result(img):
    '''input: the img of the game now
       output: the result of the game 
               return_value=-1 stand for the game is continuing
               return_value>=0 stand for the game is end and the return_value is the score of the player.'''
    if check_end(img)==False:
        return -1
    if check_new_record(img):
        gray=change_to_gray(img,100)
        gray=gray[540:700,:] 
        return check_score(gray)
    else:
        gray=change_to_gray(img,200)
        gray=gray[300:450,:]
        return check_score(gray)          
    
    
'''    
img=cv.imread("end_num17.png")
print(check_end(img))
print(check_new_record(img))
gray=change_to_gray(img,200)
print(check_score(gray))
'''
img=cv.imread("result2.png")

print(check_result(img))