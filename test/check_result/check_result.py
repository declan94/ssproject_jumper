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
  #  print(sum)
  #  print(count)
    sum2=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum2+=phi(fliter[i,j,:],img[i+1347,j+410,:])
   # print("sum2",sum2)
    return sum>50000 ,sum2>55000


def check_new_record(img):
    fliter=cv.imread("./record.PNG")
    sum=0
    count=0
    for i in range(0,fliter.shape[0]):
        for j in range(0,fliter.shape[1]):
            sum+=phi(fliter[i,j,:],img[i+230,j+430,:])
  #  print(sum)
  #  print(count)
    return sum>15000

def choose_number(x,fliter_x,y,fliter_y):
    return abs(x-fliter_x)<100 and abs(y-fliter_y)<100
   # return abs(x-fliter_x)50

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
                var[0]+=(i-ex[0])**2
                var[1]+=(j-ex[1])**2
    var[0]/=count
    var[1]/=count

    number=-1
    #judge number here
    if choose_number(var[0],2098,var[1],1222):  #2 or 5 or 3
        number=2
    elif choose_number(var[0],1879,var[1],1185): #6 or 9
        if ex[0]<75:
            number=9
        else:
            number=6
    elif choose_number(var[0],1910,var[1],187):
        number=1
    elif choose_number(var[0],1875,var[1],894):
        number=7
    elif choose_number(var[0],1424,var[1],1632):
        number=4
    elif choose_number(var[0],2219,var[1],1461):
        number=0
    elif choose_number(var[0],1947,var[1],1313):
        number=8
    else:
        number=-1

    if number==2:
        col=bmp.shape[1]
        col=int(col/2)
        temp=bmp[:,:col]
        #cv.imwrite("./temp.bmp",temp)
        temp_exp_row=0
        temp_count=0
        for i in range(0,temp.shape[0]):
            for j in range(0,temp.shape[1]):
                if temp[i,j]>200:
                    temp_exp_row+=i
                    temp_count+=1
        temp_exp_row/=temp_count
        row=int(bmp.shape[0]/2)
        temp2=bmp[:,col:]
      #  cv.imwrite("./temp2.bmp",temp)
        temp_exp_row2=0
        temp_count2=0
        for i in range(0,temp2.shape[0]):
            for j in range(0,temp2.shape[1]):
                if temp2[i,j]>200:
                    temp_exp_row2+=i
                    temp_count2+=1
        temp_exp_row2/=temp_count2
        #print(temp_exp_row,temp_exp_row2)
        if abs(temp_exp_row-temp_exp_row2)<2:
            number=3
        elif temp_exp_row<temp_exp_row2:
            number=5
        else:
            number=2

#    print(var)

    return number

def check_score(bmp):
    window=bmp
    center=window[:,460:600]
  #  cv.imwrite('./center.bmp',center)
    c=check_score_window(center)
 #   print('center',c)
    even=[-1,-1,-1,-1,-1,-1,-1,-1] #8
    odd=[-1,-1,-1,-1,-1,-1,-1] #7
    if c==-1 : #even
       # print('even')
        now=window[:,520:650]
    #    cv.imwrite("./cv1.bmp",now)
        c=check_score_window(now)
        even[4]=c
     #   print(c)
        now=window[:,390:520]
     #   cv.imwrite("./cv2.bmp",now)
        c=check_score_window(now)
        even[3]=c
     #   print(c)
        now=window[:,240:380]
        c=check_score_window(now)
        if c==-1:
            return 10*even[3]+even[4]
        even[2]=c
        now=window[:,660:800]
        c=check_score_window(now)
        even[5]=c
        return 1000*even[2]+100*even[3]+10*even[4]+even[5]

    else:   #odd
     #   print('odd')
        odd[3]=c
        now=window[:,315:455]
        c=check_score_window(now)
     #   print(c)
        if c==-1:
            return odd[3]
        odd[2]=c
        now=window[:,605:745]
        c=check_score_window(now)
        odd[4]=c
      #  print(c)
        now=window[:,170:310]
        c=check_score_window(now)
        if now==-1:
            return odd[2]*100+odd[3]*10+odd[4]
        odd[1]=c
        now=window[:,750:890]
        c=check_score_window(now)
        odd[5]=c
        return 10000*odd[1]+odd[2]*1000+odd[3]*100+odd[4]*10+odd[5]
        

def check_result(img):
    '''input: the img of the game now
       output: the result of the game 
               return_value=-1 stand for the game is continuing
               return_value>=0 stand for the game is end and the return_value is the score of the player.'''
    result=check_end(img)
    if result[0] + result[1]==False:
        return -1,[None,None]
    if result[0]:
        position=[1750,490]
    else:
        position=[1600,490]
    if check_new_record(img):
        gray=change_to_gray(img,100)
        gray=gray[540:700,:] 
        return check_score(gray),position
    else:
        gray=change_to_gray(img,200)
        gray=gray[300:450,:]
        return check_score(gray),position       
    
    
'''    
img=cv.imread("end_num17.png")
print(check_end(img))
print(check_new_record(img))
gray=change_to_gray(img,200)
print(check_score(gray))
'''


img=cv.imread("end_num17.png")

print(check_result(img))



'''
for i in range(0,10):
    img=cv.imread(str(i)+".png")
    print('***',i,check_result(img))'''