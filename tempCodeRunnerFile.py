
def printKeyValue(**kwargs):

    for k, val in kwargs.items():
        print(k,val)


query = {"a":"apple","b":"banana","c": "cherry"}

printKeyValue(**query)