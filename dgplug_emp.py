import pandas as pd
import json
def main():
    
    # Dictionary with list object in values
    '''studentData = {
        'name' : ['jack', 'Riti', 'Aadi'],
        'age' : [34, 30, 16],
        'city' : ['Sydney', 'Delhi', 'New york']
    }'''
    studentData = {}
    with open ("empdata.txt") as f:
        data = f.read()

    print(type(data))
    print(data)
    
    js = json.loads(data)
    print(type(js))
            #(key, val) = line.split(":")
            #studentData[key] = val
    #dfObj = pd.DataFrame(studentData, index=['1', '2', '3']) 
    # Print data frame object on console
    #print(dfObj)

if __name__ == '__main__':
    main()
    




