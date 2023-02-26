import json
import pickle
import numpy as np

__model=None
__data_columns=None
__target=None

def estimation(sl,sw,pl,pw):
    arr=np.zeros(4)
    arr[0]=sl
    arr[1]=sw
    arr[2]=pl
    arr[3]=pw
    print(arr)
    out=__model.predict([arr])
    st=""
    if out<=1:
        st=__target[0]
    elif out<2:
        st=__target[1]
    else:
        st=__target[2]
    return st

def load_saved_artifacts():
    global __model
    global __data_columns
    global __target

    with open("server/artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
    if __model is None:
        with open("server/artifacts/iris.pickle",'rb') as f:
            __model=pickle.load(f)

    with open("server/artifacts/target.josn",'r') as f:
        __target=json.load(f)['target_names']

if __name__=='__main__':
    load_saved_artifacts()
    print(estimation(5.1,3.5,1.4,0.2))
    print(estimation(6.2, 3.4, 5.4, 2.3))
    print(__model)
