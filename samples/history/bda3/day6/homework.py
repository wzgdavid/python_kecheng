#    math    english  sports
#a   67  34  90
#b   87  98  98
#c   89  56  78
#d   54  54  56
#e   56  25  56
#f   67  78  87
#g   54  78  75
#h   98  57  56
#i   57  56  76
#    
#1 求每个人的平均分和总分           
#2 求这个班每门课的平均分           
#3 求三门课都及格的人数            
#4 求有至少两门课及格的人数          
#5 sports有几个人大于90            
#6 几个人english分数 > math分数 


import numpy as np

np.random.seed(89)
scores = np.random.randint(40,99, size=(10, 3))
print(scores)
#1 求每个人的平均分和总分
mean = scores.mean(axis=1)
print( mean )
print( scores.sum(axis=1) )
#2 求这个班每门课的平均分  
print( scores.mean(axis=0) )
#3 求三门课都及格的人数 
ge60 = scores>=60
print(ge60)
jige = ge60.sum(axis=1) # 几门课及格
print(jige)
print((jige>=3).sum())  # 人数

#4 求有至少两门课及格的人数    
print((jige>=2).sum())  # 人数

#5 sports有几个人大于90  scores[:,2]  
sports_scores = scores[:,2]
print((sports_scores>80).sum())

#6 english > math 的人数
english_scores = scores[:,1]
math_scores = scores[:,0]
print((english_scores > math_scores).sum())
