# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:11:51 2016
img 文件处理模块
@author: lywen
"""

from PIL import Image as Images 

import numpy as np

import traceback
def readImage(filepath):
    """
    读取图片并转化为灰度矩阵
    取灰度值的图片
    """
    try:
       img = Images.open(filepath)
       return img
    except :
        traceback.print_exc()
        
def imgSplit0(img):
    return img.split()[0]
        
def imgToMatrix(img):
    """
    图片转换为矩阵
    """
    
    return  np.array(img.convert('L'))

def getInterval1(Matrix):
    """
    对矩阵分割数字
    """
    """
    对矩阵分割数字
    """
    XY=Matrix.min(axis=0)
    Max = XY.max().tolist()
    Min = XY.mean().tolist()
    mid = (Max + Min)/2.0
    #mid = XY.mean().tolist()
    mid1 = 0.95*Max
    #if mid<130.0:
    #    mid =130.0
    interval =[]
    temp = []
    interval1 =[]
    temp1 = []
    for i in range(1,len(XY)):
            if i==1:
                if XY[i-1]<=mid:
                    temp.append(i)
            if (XY[i-1]>=mid and XY[i]<mid) :
                temp.append(i)
            if (XY[i-1]<mid and XY[i]>=mid):
                temp.append(i)
                interval.append(temp)
                temp = []
                
            elif i==len(XY)-1:
                if XY[i]<=mid:
                    temp.append(i)
                    interval.append(temp)
                    temp = []
                    
            if i==1:
                if XY[i-1]<=mid1:
                    temp1.append(i)
            if (XY[i-1]>=mid1 and XY[i]<mid1) :
                temp1.append(i)
            if (XY[i-1]<mid1 and XY[i]>=mid1):
                temp1.append(i)
                interval1.append(temp1)
                temp1 = []
                
            elif i==len(XY)-1:
                if XY[i]<=mid1:
                    temp1.append(i)
                    interval1.append(temp1)
                    temp1 = []        
          
    if len(interval)>len(interval1):
        
       return interval
    else:
        return interval1
        
        
#[1]
        
def getInterval(Matrix):
    """
    对矩阵分割数字
    """
    y = Matrix.min(axis = 0).tolist()
    x = range(len(y))
    #diff_x = []
    #diff_y = []
    
    interval = []
    #temp = []
    max_min = []
    ##对Y相邻值进行修正，消除误差
    for i in range(0,len(y)-1):
        if abs(y[i] - y[i+1])<20:
            y[i+1] = y[i]
    diff_y = np.diff(y)##导数 x1-x0=1    
    
    ## 找数据的极大值与极小值对应的下标
    for i in range(1,len(diff_y)-1):
        if abs(diff_y[i]-diff_y[i-1])>=1 and abs(diff_y[i]-diff_y[i+1])>=1 and abs(diff_y[i])>5:
            if diff_y[i]-diff_y[i-1]>0 and diff_y[i]-diff_y[i+1]>0:
                max_min.append((i,diff_y[i],1))##极大值
            if diff_y[i]-diff_y[i-1]<0 and diff_y[i]-diff_y[i+1]<0:
                max_min.append((i,diff_y[i],-1))##极小值
                
    if len(max_min)>0:
        max_len = len(max_min)
        for i  in range(max_len):
            x,value,flag = max_min[i]
            if i == max_len-1 and flag == -1:
                interval.append([x,len(y)-1])
                
            elif i<max_len-1:
                c_x,c_value,c_flag = max_min[i+1]
                if  abs(c_value - value)>10 and abs(c_x-x)>4:
                    if ((flag==1 and c_flag ==1) or (flag==-1 and c_flag ==-1)) :
                        ##同时出现两个极大值与极小值，说明验证码中两个字符出现粘连
                        #print c_x - x
                        interval.append([x,c_x])

                    elif flag==-1 and c_flag ==1:
                         interval.append([x,c_x])
                        
            elif i==0 and flag ==1:
                     interval.append([0,x])
    return interval
#[2]

def expandImg(img,row=100,col=50):
    """
    对分割后的矩阵进行填充，是所有的矩阵大小一致
    """
   
    return img.resize((col,row))

def splitImg(img,x1,x2,y1,y2):
    """
    对图片进行剪切
    """
    return img.crop((x1,y1,x2,y2))
    
def getSplitImg(img,interval):
    """
    获取分割的字图片
    """
    y1=0
    y2 = img.size[1]
    return map(lambda x:splitImg(img,x[0],x[1],y1,y2),interval)
    
def matrixTovector(matrix):
    return sum(matrix.tolist(),[])

def getFiles(path):
    import os 
    files = filter(lambda x:x!='.DS_Store',os.listdir(path))
    return map(lambda x:(list(x.split('.')[0]),os.path.join(path,x)),files)
def Vector01(vector):
    Mean = sum(vector)/1.0/len(vector)
    return map(lambda x: 255 if x > Mean else 0.0,vector)


class Img(object):
    def __init__(self,path,row,col,labelsList):
        img = readImage(path)##读取图片
        matrix = imgToMatrix(img)## 转换为矩阵
        interval = getInterval(matrix)##分割数字
        imgs = map(lambda x:expandImg(x,row,col),getSplitImg(img,interval))## 
        try:
            self.imgmap = map(lambda x,y:(x,Vector01(matrixTovector(imgToMatrix(y)))),labelsList,imgs)
        except:
            traceback.print_exc()
            self.imgmap = None
        
            
        
class Imgtest(object):
    def __init__(self,path,row,col):
        img = readImage(path)##读取图片
        matrix = imgToMatrix(img)## 转换为矩阵
        interval = getInterval(matrix)##分割数字
        imgs = map(lambda x:expandImg(x,row,col),getSplitImg(img,interval))## 
        
        self.imgmap = map(lambda x:Vector01(matrixTovector(imgToMatrix(x))),imgs)