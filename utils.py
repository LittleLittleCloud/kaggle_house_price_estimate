import numpy as np
import pandas as pd


#t is the known target
#t1 is the estimated target
def RMSE(t,t1):
    print((t1-t)*(t1-t))
    res=np.sqrt(np.sum((t1-t)*(t1-t))/len(t1))
    return res

#return a a_d df
#x is the rol (all the possible value of a)
#d is the column (all the possible values of all property except a)
#a_d is a df that show how many times the pair (ai,di) happened in df
def a_d_probability(df,X):
    dummy_col=pd.get_dummies(df.drop(X,1)).columns.values
    a_d_prob=pd.DataFrame(index=np.unique(df[X].values),columns=dummy_col)
    df_dummy=pd.get_dummies(df)
    for i in a_d_prob.index:
        _tmp_series=df_dummy[X+'_'+i]==1
        _tmp_df=df_dummy[_tmp_series].sum(0)
#     _tmp_df=_tmp_df.filter(axis=0,regex='^[BldgType].*')
        a_d_prob.loc[i]=_tmp_df
    return a_d_prob

#calc the discrete missing data using a_d
def calc_missing_data(df_dummy,a_d):
    #TODO
    #if the X* property in df_dummy is all zero, then we found a missing data
    #since p(a|D)=p(D|a)*p(a) (here we suppose there are no intermediate dependent between properties other than a, for example b->a<-c)
    #we can use a_d to calc p(a) and p(D|a)
    #then pick the largest answer
    pass

if __name__=='__main__':
    a=np.arange(0,3)
    b=np.arange(3,6)
    print(RMSE(a,b)) 
