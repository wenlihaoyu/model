# coding: utf-8
"""
训练验证码识别模型
"""
#from IPython.display import Image
from segmentationImg import Img,getFiles
from config import CHARACTER
import numpy as np
def train(imgfile='img/segmentation', modelfile='segmentation.pkl'):
    
    filelabel = getFiles(imgfile)
    row = 120
    col=40
    data = filter(lambda z: z is not None ,map(lambda x:Img(x[1],row,col,x[0]).imgmap,filelabel))
    data = filter(lambda x:x[0] is not None,sum(data,[]))
    label = np.array(map(lambda x:CHARACTER.get(x[0]),data))
    feature = np.array(map(lambda x:np.array(x[1]),data))
    from xgboost import XGBClassifier
    xgb = XGBClassifier(objective='multi:softmax',reg_alpha=1.0,reg_lambda=0.0,subsample=0.7,n_estimators=100,learning_rate=0.3)
    model = xgb.fit(feature,label,eval_set=[(feature,label)],eval_metric='mlogloss')
    import pickle
    fn = modelfile
    with open(fn, 'w') as f:                     # open file with write-mode
        pickle.dump(model, f)
    
   

    
if __name__=='__main__':
    #import os
    #os.chdir('')
    train()