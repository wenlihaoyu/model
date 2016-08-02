# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:03:58 2016
训练验证码模型
@author: lywen
"""
from script.segmentation import train
if __name__=='__main__':
    train(imgfile='img/segmentation', modelfile='model/segmentation.pkl')
