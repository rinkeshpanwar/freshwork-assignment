from datetime import datetime,timedelta
import json
class assignMent:
    def __init__(self,path=''):
        path = path+'data.txt'
        binary_data = open(path, 'r').read()
        jsn = ''.join(chr(int(x, 2)) for x in binary_data.split())
        received_data = json.loads(jsn)
        self.fileData= received_data
    
    def inValue(self,val):
        if val in self.fileData.keys():
            return True
        return False
    
    def insertData(self,k,v,t=None):
        if (self.inValue(k)):
            return 'Key is already present'
        timer = datetime.now()+timedelta(seconds=t) if t else None
        temp = [v,timer]
        self.fileData[k] = temp
        self.saveToFileBinary()
        return 'Succesfully saved'
    
    def deleteData(self,k):
        if (self.inValue(k)):
            del self.fileData[k]
            self.saveToFileBinary()
            return 'Deleted succesfully'
        return 'Key is not present'

    def viewData(self,k):
        if(self.inValue(k)):
            return self.fileData[k][0]
        return 'Key is not available'

    def timer(self):
        delete = []
        for k,v in self.fileData.items():
            if v[1] and (v[1]<datetime.now()):
                delete.append(k)
        if len(delete)<=0:
            return
        for i in delete:
            del self.fileData[i]
            self.saveToFileBinary()
        return

    def saveToFileBinary(self):
        dumped_json_string = json.dumps(self.fileData)
        binary_data = ' '.join(format(ord(letter), 'b') for letter in dumped_json_string)
        f = open('data.txt','w+')
        f.write(binary_data)
        f.close()
        
exit = 1
path=input('Enter path or press 0')
if path!='0':
    obj = assignMent(path)
else:
    obj = assignMent()
while(exit):
    print('''
    1.Insert data
    2.Delete data
    3.View data
    0.EXIT
    ''')
    try:
        exit = int(input())
        if exit==1:
            try:
                keyname = input('Enter Key name:')
                value = input('Enter key value:')
                timer = int(input('Enter how many second after data to be deleted (o for null):'))
                obj.timer()
                print(obj.insertData(keyname,value,timer))
            except :
                print('Please enter a relevant data')
        elif exit == 2:
            obj.timer()
            keyname = input('Enter Keyname to be deleted:')
            data = obj.deleteData(keyname)
            print(data)
        elif exit == 3:
            obj.timer()
            keyname = input('Enter Keyname whose value to be shown:')
            print(obj.viewData(keyname))
        
        else:
            pass
            
    except :
        print('Please enter number only')
        exit = 1
        pass

