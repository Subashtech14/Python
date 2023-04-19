#Converting Dictionary into a dataframe
#DataFrame is a 2-D data structure that consists of columns of various types.
# It is very similar to python dictionary and you can even convert a dictionary into a pandas dataframe.
import pandas as pd
emp_details={"subash":{"Devil":{"ID":"444","Salery":"Infinity"}}}
df=pd.DataFrame(emp_details['subash'])
print(df)