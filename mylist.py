class List:
    
    def __init__(self,lst):
        self.lst = lst
        
    def show_list(self):
        '''This will show the your list'''
        return self.lst
        
    def append_no(self,n):
        '''This method append number on list end'''
        return self.lst.append(n)
        
    def clear_list(self):
        '''This will clear the list'''
        return self.lst.clear()
    
    def copy_list(self):
        '''This will copy the entire list'''
        return self.lst.copy()
    
    def count_listEliments(self,n):
        ''' Return number of occurrences of value'''
        return self.lst.count(n)
    
    def extend_list(self,lt):
        '''Extend list by appending elements from the iterable.'''
        return self.lst.extend(lt)
    
    def find_index(self,i):
        '''Return first index of value.'''
        return self.lst.index(i)
    
    def insert_Element(self,i,lt):
        ''' Insert object before index.'''
        return self.lst.insert(i,lt)
    
    def pop_Element(self,p):
        '''Remove and return item at index (default last).'''
        return self.lst.pop(p)
    
    def remove_Element(self,e):
        '''Remove first occurrence of value.'''
        return self.lst.remove(e)
    
    def reverse_list(self):
        '''Reverse the list'''
        return self.lst.reverse()
    
    def sort_list(self):
        '''Sort the list in ascending order and return None.'''
        return self.lst.sort()
    
    def __str__(self):
        return "This is list Class"
         