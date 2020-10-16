#!/usr/bin/env python
# coding: utf-8

# In[10]:


import gender_guesser.detector as gender
import pandas as pd
import re
from gender_detector import gender_detector as gd
import numpy as np


# In[11]:


def guess_gender(df,column):
    df['firstname'] = df[column].apply(lambda x : re.match('([^-]+)',re.match('([^\s]+)',str(x))[0])[0].lower().title())
    lst = list(df['firstname'].drop_duplicates())
    gend = gender.Detector()
    names = pd.DataFrame()

    x = 0
    for i in lst[:10]:

        try:
            d = {'name' : i,
                 'gender_1' : gend.get_gender(i),
                 'gender_uk' : gd.GenderDetector('uk').guess(str(i)),
                 'gender_us' : gd.GenderDetector('us').guess(str(i)),
                 'gender_uy' : gd.GenderDetector('uy').guess(str(i)),
                 'gender_ar' : gd.GenderDetector('ar').guess(str(i))
                 }

        except (KeyError,UnicodeDecodeError):
            try: 
                d = {'name' : i,
                     'gender_1' : gend.get_gender(i),
                     'gender_uk' : gd.GenderDetector('uk').guess(str(i)),
                     'gender_us' : gd.GenderDetector('us').guess(str(i)),
                     'gender_uy' : gd.GenderDetector('uy').guess(str(i)),
                     'gender_ar' : 'unknown'
                     }
            except (KeyError,UnicodeDecodeError):      
                d = {'name' : i,
                     'gender_1' : gend.get_gender(i),
                     'gender_uk' : 'unknown',
                     'gender_us' : 'unknown',
                     'gender_uy' : 'unknown',
                     'gender_ar' : 'unknown'
                     }
        x= x +1
        print(x)    
        names = names.append(d,ignore_index=True)

    names['gender'] = np.where(names.gender_1 != 'unknown',names.gender_1,
                        np.where(names.gender_uk != 'unknown',names.gender_uk,
                            np.where(names.gender_us != 'unknown',names.gender_us,
                                     np.where(names.gender_uy != 'unknown',names.gender_uy,
                                        np.where(names.gender_ar != 'unknown',names.gender_uy,'unknown')))))  


#     final = pd.concat([names.loc[names.gender != 'unknown'],names[['gender','name']]])

    return names


    

