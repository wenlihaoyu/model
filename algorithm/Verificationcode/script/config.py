# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:44:33 2016
数字、字母等与模型映射
@author: lywen
"""
def getCHARACTER():
    CHARACTER = u'0123456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPRSTUVWXYZ'
    CHARACTER = list(CHARACTER)
    return dict(zip(CHARACTER,range(len(CHARACTER))))
    
    
def getCHARACTERreverse():
    CHARACTER = u'0123456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPRSTUVWXYZ'
    CHARACTER = list(CHARACTER)
    return dict(zip(range(len(CHARACTER)),CHARACTER))
CHARACTER =  getCHARACTER()
CHARACTERreverse = getCHARACTERreverse()


