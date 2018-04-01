# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# Read data from file into variables
#y, c, x1, x2 = np.loadtxt('data.txt', unpack=True)

# Map value to color
color_mapper = np.vectorize(lambda x: {0: 'red', 1: 'blue',2:'green',3:'black',4:'pink',5:'orange'}.get(x))

# Plot a line for every line of data in your file
#plt.hlines(y, x1, x2, colors=color_mapper(c))



'''CProcess creates the process and initiate its attributes '''
class CProcess(object):
    def __init__(self, process_name, arrival_time, burst_time, priority=0):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def set_process_name(self, process_name):
        self.process_name = process_name

    def get_process_name(self):
        return self.process_name

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_burst_time(self, burst_time):
        self.burst_time = burst_time

    def get_burst_time(self):
        return self.burst_time

    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def __str__(self):
        return "name of process : %s , arrival time = %s , burst time = %s , priority = %s " % (
        self.process_name, self.arrival_time, self.burst_time, self.priority)


class CHandle(object):
    l_processes = []
    size = 0

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_index_in_list(self, process_name):
        for i in range(self.size):
            if process_name == self.l_processes[i].get_process_name():
                return i
    def arrange_arrival_time(self):
        for i in range(self.size-1):
            j = i+1
            while j < self.size :
                if(self.l_processes[i].get_arrival_time()>self.l_processes[j].get_arrival_time()):
                    temp = self.l_processes[i]
                    self.l_processes[i] = self.l_processes[j]
                    self.l_processes[j] = temp
                j+=1    
    def arrange_arrival_time_shortest_job(self):
        for i in range(self.size-1):
            j = i+1
            while j < self.size :
                if(self.l_processes[i].get_arrival_time()>self.l_processes[j].get_arrival_time()or(self.l_processes[i].get_arrival_time()==self.l_processes[j].get_arrival_time() and self.l_processes[i].get_burst_time()>self.l_processes[j].get_burst_time())):
                    temp = self.l_processes[i]
                    self.l_processes[i] = self.l_processes[j]
                    self.l_processes[j] = temp
                j+=1    
    def arrange_arrival_time_highest_priority(self):
        for i in range(self.size-1):
            j = i+1
            while j < self.size :
                if(self.l_processes[i].get_arrival_time()>self.l_processes[j].get_arrival_time()or(self.l_processes[i].get_arrival_time()==self.l_processes[j].get_arrival_time() and self.l_processes[i].get_priority()>self.l_processes[j].get_priority())):
                    temp = self.l_processes[i]
                    self.l_processes[i] = self.l_processes[j]
                    self.l_processes[j] = temp
                j+=1    
    def get_min_arrival_time(self):
        index_min_arrival_time = 0
        for i in self.l_processes:
            if (i.get_process_name() == self.l_processes[index_min_arrival_time].get_process_name()):
                continue
            elif (i.get_arrival_time() < self.l_processes[index_min_arrival_time].get_arrival_time()):
                index_min_arrival_time = self.get_index_in_list(i.get_process_name())
        return index_min_arrival_time

    def get_highest_priority(self):
        index_highest_priority = 0
        for i in self.l_processes:
            if (i.get_process_name() == self.l_processes[index_highest_priority].get_process_name()):
                continue
            elif (i.get_priority() < self.l_processes[index_highest_priority].get_priority()):
                index_highest_priority = self.get_index_in_list(i.get_process_name())
        return index_highest_priority

    def get_min_burst_time(self):
        index_min_burst = 0
        for i in self.l_processes:
            if (i.get_process_name() == self.l_processes[index_min_burst].get_process_name()):
                continue
            elif (i.get_burst_time() < self.l_processes[index_min_burst].get_burst_time()):
                index_min_burst = self.get_index_in_list(i.get_process_name())
        return index_min_burst

    def add_process(self, process):
        self.l_processes.append(process)
        self.size += 1

    def remove_process(self, process):
        index = self.get_index_in_list(process.get_process_name())
        self.size -= 1
        return self.l_processes.pop(index)


'''
p1 = CProcess("p1",0,15,2)
p2 = CProcess("p2",1,10,0)
p1.get_burst_time()
c1 = CHandle()
c1.add_process(p1)
c1.add_process(p2)
print(c1.get_highest_priority())
print(c1.get_size())
print(c1.remove_process(p1))
print(c1.get_size())
'''

'''CCell prints the output of the processes'''
class CCell(object):
    def __init__(self, process_name, begin, end):
        self.process_name = process_name
        self.begin = begin
        self.end = end
       
        
    def set_process_name(self, process_name):
        self.process_name = process_name

    def get_process_name(self):
        return self.process_name

    def set_begin(self, begin):
        self.begin = begin

    def get_begin(self):
        return self.begin

    def set_end(self, end):
        self.end = end

    def get_end(self):
        return self.end

    def __str__(self):
       return "name of process : %s , starts = %s , ends = %s" % (self.process_name, self.begin, self.end)


'''CSimulator has the 4 algorithms'''
class CSimulator(object):
    l_cells = []
    size_cells = 0
    inside = False

    def __init__(self, algorithm_name, algorithm_type,round_robin_quantum=0):
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type
        self.round_robin_quantum = round_robin_quantum

    def set_algorithm_name(self, algorithm_name):
        self.algorithm_name = algorithm_name

    def set_algorithm_type(self, algorithm_type):
        self.algorithm_type = algorithm_type

    def get_algorithm_name(self):
        return self.algorithm_name

    def get_algorithm_type(self):
        return self.algorithm_type

    def add_cell(self, cell):
        self.l_cells.append(cell)
        self.size_cells += 1

    def remove_cell(self):
        self.size_cells -= 1
        return self.l_cells.pop(0)

    def xplt(name, begin , end):
        plt.hlines(1, begin, end, colors=color_mapper(int(name[1:])))
        
    def simulate(self, handle):
        start = 0
        if (self.algorithm_name == "First Come First Served"):
            while handle.get_size() != 0:
                current_index = handle.get_min_arrival_time()
                t_pro = handle.l_processes[current_index]
                process = handle.remove_process(t_pro)
                self.xplt(process.get_process_name(), start, (start + process.get_burst_time()))
                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                start += process.get_burst_time()
                self.add_cell(c)
            
        elif (self.algorithm_name == "Shortest Job First"):
            if (self.algorithm_type == "non preemptive"):
                while handle.size != 0:
                    if (start == 0):
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() == handle.l_processes[handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_burst_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                        elif (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > handle.l_processes[handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                    else:
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() <= self.l_cells[self.size_cells - 1].get_end()):
                            current_index = handle.get_min_burst_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                        else:
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
            elif (self.algorithm_type == "preemptive"):
                handle.arrange_arrival_time_shortest_job()
                current_index=0
                counter = 1
                start = 0
                out = False
                while handle.size != 0:
                    while ((start != handle.l_processes[handle.get_size()-1].get_arrival_time()) and (not out)):
                        
                            t_pro = handle.l_processes[current_index]
                            if (handle.l_processes[current_index].get_burst_time() <= handle.l_processes[current_index+counter].get_arrival_time()-start):
                                process = handle.remove_process(t_pro)
                                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                start += process.get_burst_time()
                                self.add_cell(c)
                                current_index+=1
                            else:
                                if( (handle.l_processes[current_index].get_burst_time()-(handle.l_processes[current_index+counter].get_arrival_time()+start)) > handle.l_processes[current_index+counter].get_burst_time()):
                                    c = CCell(handle.l_processes[current_index].get_process_name(), start,start + handle.l_processes[current_index+counter].get_arrival_time())
                                    start += handle.l_processes[current_index+counter].get_arrival_time()
                                    self.add_cell(c)
                                    handle.l_processes[current_index].set_burst_time(handle.l_processes[current_index].get_burst_time() - handle.l_processes[current_index+counter].get_arrival_time())
                                    current_index+=1
                                   
                                else:     
                                    counter+=1
                            if (current_index+counter)==handle.get_size():
                                out=True
                    out = True                       
                    current_index = handle.get_min_burst_time()
                    t_pro = handle.l_processes[current_index]
                    process = handle.remove_process(t_pro)
                    c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                    start += process.get_burst_time()
                    self.add_cell(c)

        elif (self.algorithm_name == "Round Robin"):
            handle.arrange_arrival_time()
            while handle.get_size() != 0:
                i = 0
                while i < handle.size:
                    if(handle.l_processes[i].get_burst_time() > self.round_robin_quantum):
                        if(handle.get_size()==1):
                            c=CCell(handle.l_processes[i].get_process_name(), start,start + handle.l_processes[i].get_burst_time())
                            self.add_cell(c)
                            handle.remove_process(handle.l_processes[i])
                        else :
                            handle.l_processes[i].set_burst_time( handle.l_processes[i].get_burst_time() - self.round_robin_quantum )
                            c=CCell(handle.l_processes[i].get_process_name(), start,start + self.round_robin_quantum)
                            start += self.round_robin_quantum
                            self.add_cell(c)
                            i+=1
                    else:
                        if(handle.l_processes[i].get_burst_time() < self.round_robin_quantum):
                            c = CCell(handle.l_processes[i].get_process_name(), start,start + handle.l_processes[i].get_burst_time())
                            start += handle.l_processes[i].get_burst_time()
                        elif(handle.l_processes[i].get_burst_time() == self.round_robin_quantum):
                            c = CCell(handle.l_processes[i].get_process_name(), start,start + self.round_robin_quantum)
                            start += self.round_robin_quantum
                        self.add_cell(c)
                        handle.remove_process(handle.l_processes[i])

                    
        elif (self.algorithm_name == "Priority"):
            if (self.algorithm_type == "non preemptive"):
                handle.arrange_arrival_time_highest_priority()
                while handle.size != 0:
                    if (start == 0):
                        if (handle.l_processes[handle.get_highest_priority()].get_arrival_time() == handle.l_processes[handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_highest_priority()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                        elif (handle.l_processes[handle.get_highest_priority()].get_arrival_time() > handle.l_processes[handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                    else:
                        if (handle.l_processes[handle.get_highest_priority()].get_arrival_time() <= self.l_cells[self.size_cells - 1].get_end()):
                            current_index = handle.get_highest_priority()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                        else:
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
        
            elif (self.algorithm_type == "preemptive"):
                handle.arrange_arrival_time_highest_priority()
                current_index=0
                counter = 1
                start = 0
                out = False
                print(handle.l_processes[handle.get_size()-1].get_arrival_time())
                while handle.size != 0:
                    while ((start != handle.l_processes[handle.get_size()-1].get_arrival_time()) and (not out)):
                        
                            
                            if (handle.l_processes[current_index].get_priority() <= handle.l_processes[current_index+counter].get_priority()):
                                counter+=1
                            else:
                                if (handle.l_processes[current_index].get_burst_time() > (handle.l_processes[current_index+counter].get_arrival_time()-start)):
                                    if(handle.l_processes[current_index+counter].get_arrival_time()>start):
                                        c = CCell(handle.l_processes[current_index].get_process_name(), start,start + (handle.l_processes[current_index+counter].get_arrival_time()-start))
                                        start += (handle.l_processes[current_index+counter].get_arrival_time()-start)
                                        self.add_cell(c)
                                        handle.l_processes[current_index].set_burst_time(handle.l_processes[current_index].get_burst_time() - (handle.l_processes[current_index+counter].get_arrival_time()-handle.l_processes[current_index].get_arrival_time()))
                                        current_index+=1
                                        counter=1
                                    else:
                                        current_index+=1
                                        counter=1
                                   
                                else:     
                                    t_pro = handle.l_processes[current_index]
                                    process = handle.remove_process(t_pro)
                                    c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                    start += process.get_burst_time()
                                    self.add_cell(c)
                                    current_index+=1
                                    counter=1
                                    
                            if (current_index+counter)==handle.get_size():
                                out=True
                    out = True                       
                    current_index = handle.get_highest_priority()
                    t_pro = handle.l_processes[current_index]
                    process = handle.remove_process(t_pro)
                    c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                    start += process.get_burst_time()
                    self.add_cell(c)
                        


            
# test round robin
                        

p1 = CProcess("p1", 0,10,3)
p2 = CProcess("p2", 0, 1,1)
p3 = CProcess("p3", 0, 2,4)
p4 = CProcess("p4", 0, 1,5)
p5 = CProcess("p5", 0, 5,2)
d = CHandle()
d.add_process(p1)
d.add_process(p2)
d.add_process(p3)
d.add_process(p4)
d.add_process(p5)
s = CSimulator("First Come First Served", "preemptive")
print(type(d))
s.simulate(d)
for i in range(s.size_cells):
	print(s.remove_cell())







