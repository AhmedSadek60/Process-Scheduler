# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:23:27 2018

@author: mohamed hussien
"""
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
    round_robin_duration=5
    inside = False

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
                while handle.size != 0:
                    if (start == 0):
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > handle.l_processes[handle.get_min_arrival_time()].get_arrival_time()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            if (handle.l_processes[current_index].get_burst_time() <= handle.l_processes[handle.get_min_burst_time()].get_arrival_time()):
                                process = handle.remove_process(t_pro)
                                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                start += process.get_burst_time()
                                self.add_cell(c)
                            else:
                                c = CCell(handle.l_processes[current_index].get_process_name(), start,start + handle.l_processes[handle.get_min_burst_time()].get_arrival_time())
                                start += handle.l_processes[handle.get_min_burst_time()].get_arrival_time()
                                self.add_cell(c)
                                handle.l_processes[current_index].set_burst_time(handle.l_processes[current_index].get_burst_time() - handle.l_processes[handle.get_min_burst_time()].get_arrival_time())
                    else:
                        if (handle.l_processes[handle.get_min_burst_time()].get_arrival_time() > self.l_cells[self.size_cells - 1].get_end()):
                            current_index = handle.get_min_arrival_time()
                            t_pro = handle.l_processes[current_index]
                            if (handle.l_processes[current_index].get_burst_time() <= handle.l_processes[handle.get_min_burst_time()].get_arrival_time()):
                                process = handle.remove_process(t_pro)
                                c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                                start += process.get_burst_time()
                                self.add_cell(c)
                            else:
                                c = CCell(handle.l_processes[current_index].get_process_name(), start,start + handle.l_processes[handle.get_min_burst_time()].get_arrival_time())
                                start += handle.l_processes[handle.get_min_burst_time()].get_arrival_time()
                                self.add_cell(c)
                                handle.l_processes[current_index].set_burst_time(handle.l_processes[current_index].get_burst_time() - handle.l_processes[handle.get_min_burst_time()].get_arrival_time())

                        else:
                            current_index = handle.get_min_burst_time()
                            t_pro = handle.l_processes[current_index]
                            process = handle.remove_process(t_pro)
                            c = CCell(process.get_process_name(), start, start + process.get_burst_time())
                            start += process.get_burst_time()
                            self.add_cell(c)

        elif (self.algorithm_name == "Round Robin"):
            
            while handle.get_size() != 0:
                i = 0
                while i < handle.size:
                    if self.inside == True :
                        i-=1
                        self.inside = False
                    if(handle.l_processes[i].get_burst_time() > self.round_robin_duration):
                        handle.l_processes[i].set_burst_time( handle.l_processes[i].get_burst_time() - self.round_robin_duration )
                        c=CCell(handle.l_processes[i].get_process_name(), start,start + self.round_robin_duration)
                        start += self.round_robin_duration
                        self.add_cell(c)
                        i+=1
                    else:
                        if(handle.l_processes[i].get_burst_time() < self.round_robin_duration):
                            c = CCell(handle.l_processes[i].get_process_name(), start,start + handle.l_processes[i].get_burst_time())
                            start += handle.l_processes[i].get_burst_time()
                        elif(handle.l_processes[i].get_burst_time() == self.round_robin_duration):
                            c = CCell(handle.l_processes[i].get_process_name(), start,start + self.round_robin_duration)
                            start += self.round_robin_duration
                        self.add_cell(c)
                        handle.remove_process(handle.l_processes[i])
                        if i!=handle.get_size() :
                            self.inside = True
                            i+=1

l_process_name=[]
l_arrival_time=[]
l_burst_time=[]
l_priority=[]
algorithm_name = ""
no_processes=0
d = CHandle()
matrix = []
s = CSimulator("","")
inside = True
initial = 0
final = 0
average_waiting_time = 0
import sys
from PyQt5.QtWidgets import(QApplication,QTabWidget,QTableWidgetItem,QTableWidget,QWidgetItem,QMainWindow,QPushButton,QVBoxLayout,QCheckBox,QHBoxLayout,QLabel,QLineEdit,QRadioButton,QWidget)

            
class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.init_table()
        
    def init_table(self):
        self.cellChanged.connect(self.c_current)
        self.show()
    def c_current(self):
        row = self.currentRow()
        col = self.currentColumn()
        value = self.item(row, col)
        value = value.text()
        if(col==0):
            l_process_name.append(str(value))
        elif(col==1):
            l_arrival_time.append(int(value))
        elif(col==2):
            l_burst_time.append(int(value))
        else:
            l_priority.append(int(value))

class Window (QWidget):
    
    def __init__ (self):
        super().__init__()
        self.l1 = QLabel("algorithms")
        self.l2 = QLabel("no_processes")
        self.l3 = QLabel("average waiting time")
        self.le = QLineEdit()
        self.le2 = QLineEdit()
        self.r1 = QRadioButton("FCFS")
        self.r2 = QRadioButton("RB")
        self.r3 = QRadioButton("SJF NON PREEMPTIVE")
        self.r4 = QRadioButton("SJF PREEMPTIVE")
        self.r5 = QRadioButton("PRIORITY NON PREEMPTIVE")
        self.r6 = QRadioButton("PRIORITY PREEMPTIVE")
        self.psh1 = QPushButton("go to table")
        self.psh2 = QPushButton("ok")
        #self.psh3 = QPushButton("cancel")
        self.init_gui()
        
    def init_gui(self):
        self.setWindowTitle("Schedular Simulator")
        v1 = QVBoxLayout()
        h3 = QHBoxLayout()
        h4 = QHBoxLayout()
        h5 = QHBoxLayout()
        h6 = QHBoxLayout()
        h3.addWidget(self.l2)
        h3.addStretch()
        h3.addWidget(self.le)
        h4.addStretch()
        h4.addWidget(self.psh1)
        h4.addStretch()
        h5.addWidget(self.psh2)
        h6.addWidget(self.l3)
        h6.addStretch()
        h6.addWidget(self.le2)
        #h5.addStretch()
        #h5.addWidget(self.psh3)
        v1.addWidget(self.l1)
        v1.addWidget(self.r1)
        v1.addWidget(self.r2)
        v1.addWidget(self.r3)
        v1.addWidget(self.r4)
        v1.addWidget(self.r5)
        v1.addWidget(self.r6)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h6)
        v1.addLayout(h5)
        self.psh1.clicked.connect(self.btn1_click) 
        self.psh2.clicked.connect(self.btn2_click) 
        self.setLayout(v1)
        self.show()
        
        
    def btn1_click (self):
        if self.r5.isChecked() and self.r6.isChecked():
            self.form_widget = MyTable(int(self.le.text()), 4)
            col_headers = ['process name', 'arrival time', 'burst time', 'priority']
            self.form_widget.setHorizontalHeaderLabels(col_headers)
        else:
            self.form_widget = MyTable(int(self.le.text()), 3)
            col_headers = ['process name', 'arrival time', 'burst time']
            self.form_widget.setHorizontalHeaderLabels(col_headers)
        global no_processes,algorithm_name
        no_processes=int(self.le.text())
        if(self.r1.isChecked()):
            algorithm_name=self.r1.text()
        elif(self.r2.isChecked()):
            algorithm_name=self.r2.text()
        elif(self.r3.isChecked()):
            algorithm_name=self.r3.text()
        elif(self.r4.isChecked()):
            algorithm_name=self.r4.text()
        elif(self.r5.isChecked()):
            algorithm_name=self.r5.text()
        else:
            algorithm_name=self.r6.text()
        
    
    def btn2_click (self):
        
        if(algorithm_name=="PRIORITY NON PREEMPTIVE" or algorithm_name=="PRIORITY PREEMPTIVE"):
            matrix = [l_process_name,l_arrival_time,l_burst_time,l_priority]
            for i in range(len(l_process_name)):
                d.add_process(CProcess(matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i]))
                
        else :
            matrix = [l_process_name,l_arrival_time,l_burst_time]
            for i in range(len(l_process_name)):
                d.add_process(CProcess(matrix[0][i],matrix[1][i],matrix[2][i]))
            global s,initial,final,average_waiting_time,inside
            if algorithm_name=="FCFS":
                s = CSimulator("First Come First Served", "non preemptive")
                s.simulate(d)
                '''
                for i in range(s.size_cells):
                    print(s.remove_cell())
                '''
            elif algorithm_name=="SJF NON PREEMPTIVE":
                s = CSimulator("Shortest Job First", "non preemptive")
                s.simulate(d)
            elif algorithm_name=="SJF PREEMPTIVE":
                s = CSimulator("Shortest Job First", "preemptive")
                s.simulate(d)
                  
            
            for i in range(no_processes):
                    initial = 0
                    final = 0
                    for j in range(s.size_cells):
                       if(l_process_name[i]==s.l_cells[j].get_process_name()):
                           if(inside):
                               inside = False
                               initial = s.l_cells[j].get_begin()
                               final = s.l_cells[j].get_end()
                           else:
                               final = s.l_cells[j].get_end()
                    average_waiting_time+=(final-l_arrival_time[i]-l_burst_time[i])   
            self.le2.setText(str(average_waiting_time/no_processes)) 
           
            
           
            

app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
    

