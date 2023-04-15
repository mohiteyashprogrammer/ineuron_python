class Dictonary:
    
    def __init__(self,d):
        self.d = d
        
    def show_dict(self):
        '''This will show you your dictionary'''
        return self.d
        
    
    def notdict(self):
        '''if its not the dictionary it will raise error'''
        if type(self.d) != dict:
            raise Exception(self.d,"Not Dictionary")
        return 1
    
    def insert_key_value(self,key,value):
        '''Insert new value pairs'''
        self.d[key] = value
            
    def clear_dict(self):
        '''Remove all items from D.'''
        return self.d.clear()
    
    def copy_dict(self):
        '''a shallow copy of Dictionary'''
        return self.d.copy()
    
    def fromkeysOfdict(self,i,v):
        '''Create a new dictionary with keys from iterable and values set to value.'''
        return self.d.fromkeys(i,v)
    
    def get_value(self,v):
        '''Create a new dictionary with keys from iterable and values set to value.'''
        return self.d.get(v)
    
    def get_items(self):
        '''a set-like object providing a view on Dictionary's items'''
        return self.d.items()
    
    def get_keys(self):
        '''a set-like object providing a view on D's keys'''
        return self.d.keys()
    
    def get_values(self):
        '''an object providing a view on D's values'''
        return self.d.values()
    
    def pop_dict(self,p):
        '''remove specified key and return the corresponding value.'''
        return self.d.pop(p)
    
    def pop_item(self):
        '''Remove and return a (key, value) pair as a 2-tuple'''
        return self.d.popitem()
    
    def set_defalt(self,k,v):
        '''Insert key with a value of default if key is not in the dictionary.'''
        return self.d.setdefault(k,v)
    
    def update_dict(self,dd):
        return self.d.update(dd)

         
    def listsearch(self,element):
        
        if element in self.lst:
            return f"{element}:{True}"
        else:
            return f"{element}:{False}"
    
    def __str__(self):
        return "this is dictionary class"
    