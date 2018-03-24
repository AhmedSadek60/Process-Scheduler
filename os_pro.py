# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
import sys
print(sys.version)
'''
class CProcess (object) :
    def __init__ (self,index,process_name,arrival_time,burst_time,priority = 0):
        self.index = index 
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
    
    def set_index (self,index):
        self.index = index
    
    def get_index (self):
        return self.index
    
    def set_process_name (self,process_name):
        self.process_name = process_name
    
    def get_process_name (self):
        return self.process_name
    
    def set_arrival_time (self,arrival_time):
        self.arrival_time = arrival_time
    
    def get_arrival_time (self):
        return self.arrival_time
    
    def set_burst_time (self,burst_time):
        self.burst_time = burst_time
    
    def get_burst_time (self):
        return self.burst_time
    
    def set_priority (self,priority):
        self.priority = priority
    
    def get_priority (self):
        return self.priority
    
class CHandle (object) :
    l_processes = []
    size = 0

    def set_size(self,size):
        self.size = size
        
    def get_size(self):
        return self.size
    
    def get_min_arrival_time (self):
        index_min_arrival_time = 0
        for i in self.l_processes :
            if (i.get_index() == index_min_arrival_time):
                continue
            elif (i.get_arrival_time()<self.l_processes[index_min_arrival_time].get_arrival_time()):
                index_min_arrival_time = i.get_index()
        return index_min_arrival_time
    
    def get_highest_priority (self):
        index_highest_priority = 0
        for i in self.l_processes :
            if (i.get_index() == index_highest_priority):
                continue
            elif (i.get_priority()<self.l_processes[index_highest_priority].get_priority()):
                index_highest_priority = i.get_index()
        return index_highest_priority
    
    def get_min_burst_time (self):
        index_min_burst = 0
        for i in self.l_processes :
            if (i.get_index() == index_min_burst):
                continue
            elif (i.get_burst_time()<self.l_processes[index_min_burst].get_burst_time()):
                index_min_burst = i.get_index()
        return index_min_burst
    
    def add_process (self,process):
        self.l_processes.append(process)
        self.size+=1
        
    def remove_process (self,index):
        self.size-=1
        return self.l_processes.pop(index)

'''
p1 = CProcess(0,"p1",0,15,2)
p2 = CProcess(1,"p2",1,10,0)
p1.get_burst_time()
c1 = CHandle()
c1.add_process(p1)
c1.add_process(p2)
print(c1.get_highest_priority())
c1.remove_process(0)
print(c1.get_size())
'''

class cell (object) :
    def __init__ (self,process_name,begin,end):
        self.process_name = process_name
        self.begin = begin
        self.end = end
        
    def set_process_name (self,process_name):
        self.process_name = process_name
        
    def get_process_name (self):
        return self.process_name
    
    def set_begin (self,begin):
        self.begin = begin
        
    def get_begin (self):
        return self.begin
    
    def set_end (self,end):
        self.end = end
        
    def get_end (self):
        return self.end
    
'''
cell1 = cell("p1",0,5)
print(cell1.get_begin())
'''

class simulator (object) :
   
    def __init__ (self,algorithm_name,algoritm_type,l_processes,size_processes, l_cells = [] , size_cells = 0):
        self.algorithm_name = algorithm_name
        self.algoritm_type = algoritm_type
        self.l_processes = l_processes
        self.size_processes = size_processes
        self.l_cells = l_cells
        self.size_cells = size_cells
    
    def set_algorithm_name (self,algorithm_name):
        self.algorithm_name = algorithm_name
    
    def set_algorithm_type (self,algorithm_type):
        self.algorithm_type = algorithm_type
        
    def get_algorithm_name (self):
        return self.algorithm_name
    
    def get_algorithm_type (self):
        return self.algorithm_type
    
    def add_cell (self,cell):
        self.l_cells.append(cell)
        self.size_cells+=1
        
    def remove_cell (self):
        self.size_cells-=1
        return self.l_cells.pop(0)
    
    def simulate (self):
        start = 0 
        if(self.algorithm_name=="First Come First Served"):
            for i in range(0,self.size_processes) :
                current_index = self.l_processes.get_min_arrival_time()
                process = self.l_processes.remove_process(current_index)
                c = cell(process.get_process_name(),start,start+process.get_burst_time())
                start += process.get_burst_time()
                self.l_cells.add_cell(c)
        elif(self.algorithm_name =="Shortest Job First") :
            if(self.algorithm_type =="non preemptive"):
                while self.size_processes != 0 :
                    if (start == 0) :
                        if(self.l_processes[self.l_processes.get_min_burst_time()].get_arrival_time()==self.l_processes[self.l_processes.get_min_arrival_time()].get_arrival_time()):
                            current_index = self.l_processes.get_min_burst_time()
                            process = self.l_processes.remove_process(current_index)
                            c = cell(process.get_process_name(),start,start+process.get_burst_time())
                            start += process.get_burst_time()
                            self.l_cells.add_cell(c)
                        elif(self.l_processes[self.l_processes.get_min_burst_time()].get_arrival_time()>self.l_processes[self.l_processes.get_min_arrival_time()].get_arrival_time()):
                            current_index = self.l_processes.get_min_arrival_time()
                            process = self.l_processes.remove_process(current_index)
                            c = cell(process.get_process_name(),start,start+process.get_burst_time())
                            start += process.get_burst_time()
                            self.l_cells.add_cell(c)
                    else:
                        if(self.l_processes[self.l_processes.get_min_burst_time()].get_arrival_time()<=self.l_cells[self.size_cells-1].get_end()):
                            current_index = self.l_processes.get_min_burst_time()
                            process = self.l_processes.remove_process(current_index)
                            c = cell(process.get_process_name(),start,start+process.get_burst_time())
                            start += process.get_burst_time()
                            self.l_cells.add_cell(c)
                        else:
                            current_index = self.l_processes.get_min_arrival_time()
                            process = self.l_processes.remove_process(current_index)
                            c = cell(process.get_process_name(),start,start+process.get_burst_time())
                            start += process.get_burst_time()
                            self.l_cells.add_cell(c)
                     
            
            

