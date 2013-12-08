#!/usr/bin/env python
# encoding: utf-8
'''
@author: Chris Lyle

Usage: shortest_route <filename> <source> <target>

Input file format

Each Vertices on one line

<node 0 name>:<attached node 1>-<distance from node 0>:...<attached node n>-<distance from node 0>

example:
0:1-6
1:2-4:7-16:0-6
2:3-12:7-4:1-4
3:4-14:7-7:2-12
4:5-2:7-3:3-14
5:4-2:6-6:7-4
6:5-6:8-9:7-8
7:2-4:3-7:4-3:5-4:6-8:1-16
8:6-9:9-16
9:8-16

'''
import sys
from copy import copy

class Router:
    
    def __init__(self):
        self.nodes = []
        self.source = ''
        self.target = ''

    def read_graph(self, graph_file):
        # Graph is read into dictionary of dictionaries
        try:
            f = open(graph_file, 'r')
            self.net = {}
            for line in f:
                vrt = line.strip().split(':')
                self.net[vrt[0]] = {}
                
                for i in range(1, len(vrt)):
                    vd = vrt[i].split('-')
                    self.net[vrt[0]][vd[0]] = int(vd[1])

            f.close()
            
        except:
            print "Error: reading file - " + graph_file
            return False
        return True
            
        
   
    def __dijkstra(self):
        
        self.cost = {}
        self.order = {}

        try:            
            for k in self.net.keys():
                if k == self.source: 
                    self.cost[k] = 0
                else: 
                    self.cost[k] = float("inf")
            
            queue = copy(self.cost)
            
            while len(queue) > 0:
                minNode = min(queue, key=queue.get)
                for i in self.net[minNode]:
                    if self.cost[i] > (self.cost[minNode] + self.net[minNode][i]):
                        self.cost[i] = self.cost[minNode] + self.net[minNode][i]
                        queue[i] = self.cost[minNode] + self.net[minNode][i]
                        self.order[i] = minNode
                del queue[minNode]
       
            temp = copy(self.target)
            revRoute = []
            self.route = []
            while 1:
                revRoute.append(temp)
                if self.order.has_key(temp): 
                    temp = self.order[temp]
                else: 
                    return "There is no route from " + str(self.source) + " to " + str(self.target) + "."
                
                if temp == self.source:
                    revRoute.append(temp)
                    break
               
            for j in range(len(revRoute) - 1, -1, -1):
                self.route.append(revRoute[j])
        except:
            print "Error: internal"
            return False
        return True
            
            
        
    def print_result(self):
        print 'Source Node: ' + self.source
        print 'Target Node: ' + self.target
        print 'Shortest Route: ' + ', '.join(self.route)
        print 'Distance: ' + str(self.cost[self.target])

    
    def get_shortest_route(self, source, target):
        ''' 
        Validate nodes and assign class variables 
        '''
        if source == target:
            print "The start and target nodes are the same"
            return False
        if not self.net.has_key(source):
            print "There is no start node called " + str(source)
            return False
        if not self.net.has_key(target):
            print "There is no target node called " + str(target)
            return False
        self.source = source
        self.target = target
        
        return self.__dijkstra()

def usage():
    print 'Usage: shortest_route <filename> <source> <target>'

def main():
    if len(sys.argv) < 4:
        usage()
        exit()
        
    filename = sys.argv[1]
    s = str(sys.argv[2])
    t = str(sys.argv[3])
    r = Router()
    if r.read_graph(graph_file=filename):
        if r.get_shortest_route(source=s, target=t):
            r.print_result()
        

if __name__ == '__main__':
    sys.exit(main())
