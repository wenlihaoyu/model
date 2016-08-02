# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:17:49 2016
验证码识别
@author: lywen
"""


# coding: utf-8

# In[1]:




from script.segmentationImg import Imgtest
from script.config import CHARACTERreverse

# In[31]:

#读取训练模型
def loadModel(modelfile='model/segmentation.pkl'):
    import pickle
    fn = modelfile
    with open(fn, 'r') as f:
        model = pickle.load(f) 
    return model
    
def predictImg(model,path):
    row = 120
    col=40
    test_feature = Imgtest(path,row,col).imgmap
    result = model.predict(test_feature)
    return map(lambda x:CHARACTERreverse.get(x),result)


# In[32]:

if __name__ =='__main__':
    
    model = loadModel()
    print '数字识别结果为:%s'%(predictImg(model,'img/test/segmentation/0020.jpeg').__str__())


# In[ ]:




# In[32]:
