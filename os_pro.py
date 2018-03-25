# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
import sys
print(sys.version)
'''

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


'''   
cell1 = CCell("p1",0,5)
print(cell1.get_begin())
print(cell1)
'''

'''CSimulator has the 4 algorithms'''
class CSimulator(object):
    l_cells = []
    size_cells = 0
    round_robin_duration=5

    def __init__(self, algorithm_name, algorithm_type):
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type

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

    def simulate(self, handle):
        start = 0
        if (self.algorithm_name == "First Come First Served"):
            while handle.get_size() != 0:
                current_index = handle.get_min_arrival_time()
                t_pro = handle.l_processes[current_index]
                process = handle.remove_process(t_pro)
                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                start += process.get_burst_time()
                self.add_cell(c)
        elif (self.algorithm_name == "Shortest Job First"):
            if (self.algorithm_type == "non preemptive"):
                while handle.size != 0:
                    if (start == 0):
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() == handle.l_processes[
                            handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_burst_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                        elif (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > handle.l_processes[
                            handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)
                    else:
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() <= self.l_cells[
                            self.size_cells - 1].get_end()):
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
                while handle.size != 0:
                    if (start == 0):
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > handle.l_processes[
                            handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            if (handle.l_processes[current_index].get_burst_time() <= handle.l_processes[
                                handle.get_min_burst_time()].get_arrival_time()):
                                process = handle.remove_process(t_pro)
                                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                start += process.get_burst_time()
                                self.add_cell(c)
                            else:
                                c = CCell(handle.l_processes[current_index].get_process_name(), start,
                                          start + handle.l_processes[handle.get_min_burst_time()].get_arrival_time())
                                start += handle.l_processes[handle.get_min_burst_time()].get_arrival_time()
                                self.add_cell(c)
                                handle.l_processes[current_index].set_burst_time(
                                    handle.l_processes[current_index].get_burst_time() - handle.l_processes[
                                        handle.get_min_burst_time()].get_arrival_time())
                    else:
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > self.l_cells[
                            self.size_cells - 1].get_end()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            if (handle.l_processes[current_index].get_burst_time() <= handle.l_processes[
                                handle.get_min_burst_time()].get_arrival_time()):
                                process = handle.remove_process(t_pro)
                                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                start += process.get_burst_time()
                                self.add_cell(c)
                            else:
                                c = CCell(handle.l_processes[current_index].get_process_name(), start,
                                          start + handle.l_processes[handle.get_min_burst_time()].get_arrival_time())
                                start += handle.l_processes[handle.get_min_burst_time()].get_arrival_time()
                                self.add_cell(c)
                                handle.l_processes[current_index].set_burst_time(
                                    handle.l_processes[current_index].get_burst_time() - handle.l_processes[
                                        handle.get_min_burst_time()].get_arrival_time())

                        else:
                            current_index = handle.get_min_burst_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)

        elif (self.algorithm_name == "Round Robin"):
            while handle.get_size() != 0:
                for i in handle.size:
                    if(CHandle.l_processes[i].burst_time > CSimulator.round_robin_duration):
                        CHandle.l_processes[i].burst_time -=CSimulator.round_robin_duration
                        c=CCell(CHandle.l_processes[i].get_process_name(), start,
                                    start + CSimulator.round_robin_duration)
                        start += CSimulator.round_robin_duration
                        self.add_cell(c)
                    else:
                        if(CHandle.l_processes[i].burst_time < CSimulator.round_robin_duration):
                            c = CCell(CHandle.l_processes[i].get_process_name(), start,
                                      start + CHandle.l_processes[i].get_burst_time())
                        elif(CHandle.l_processes[i].burst_time == CSimulator.round_robin_duration):
                            c = CCell(CHandle.l_processes[i].get_process_name(), start,
                                  start + CSimulator.round_robin_duration)
                        self.add_cell(c)
                        CHandle.remove_process(CHandle.l_processes[i])

# test shortest job first "preemptive"
p1 = CProcess("p1", 0, 8,9)
p2 = CProcess("p2", 1, 4,3)
p3 = CProcess("p3", 2, 9,100)
p4 = CProcess("p4", 3, 5,3)
d = CHandle()
d.add_process(p1)
d.add_process(p2)
d.add_process(p3)
d.add_process(p4)
s = CSimulator("Round Robin", "preemptive")
print(type(d))
s.simulate(d)
print(s.remove_cell())
print(s.remove_cell())
print(s.remove_cell())
print(s.remove_cell())
print(s.remove_cell())






