from random import *
class SubwayPlanner:

    def __init__(self):
        self.network = dict()
        
    def createStation(self,stationName):
        self.network[stationName] = []

    def createLine(self,A,B,L,T):
        Tuple = (B,L,T)
        self.network[A].append(Tuple)

        
    def getLines(self):
        for station in self.network:
            T = self.network[station]
            print("Station: {} Connected to {}".format(station,T[0][0]))
    def getGraph(self):
        return self.network;

def dijkstra(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if  start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node[0] not in path:
                newpath = find_shortest_path(graph, node[0], end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

S = SubwayPlanner()
'''
while True:
    stationName = input("Please enter a station: ")
    if stationName.lower() == 'Q'.lower():
        break;
'''
S.createStation("Burnside")
S.createStation("176")
S.createStation("MountEden")
S.createStation("170")
S.createStation("Fordham")

    
S.createLine("Burnside","176","4",2)
S.createLine("176","MountEden","4",2)
S.createLine("MountEden","170","4",2)
S.createLine("170","MountEden","4",2)
print(S.getGraph())

print(dijsktra2(S.getGraph(),"Burnside"))
