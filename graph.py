import pprint
import heapq

class directed_graph:
    def __init__(self,directed=True):
        self.directed=directed
        self.adjacent = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacent.keys():
            self.adjacent[vertex] = []

    def add_edge(self,v1,v2,time,distance,directed=True):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.adjacent[v1].append((v2,time,distance))

        if not directed:
            self.adjacent[v2].append((v1,time,distance))

    def full_dict(self):
        pprint.pprint(self.adjacent)

    # Creates the entire graph
    def build(self):
        self.add_edge("Nairobi","Githurai","26m","16.3km")
        self.add_edge("Githurai","Ruiru","17m","9.6km")
        self.add_edge("Ruiru", "Juja", "14m", "9.1km")
        self.add_edge("Juja", "Thika", "20m", "13.3km")
        self.add_edge("Thika", "Othaya", "114m", "86.8km")
        self.add_edge("Thika", "Sagana", "66m", "63.9km")
        self.add_edge("Thika", "Wang'uru", "70m", "63.1km")
        self.add_edge("Sagana", "Karatina", "25m", "25.8km")
        self.add_edge("Karatina", "Nyeri", "30m", "24.7km")
        self.add_edge("Othaya", "Nyeri", "23m", "16.9km")
        self.add_edge("Wang'uru", "Kutus", "70m", "63.1km")
        self.add_edge("Kutus", "Embu", "32m", "19.3km")
        self.add_edge("Embu", "Chuka", "59m", "43.8km")
        self.add_edge("Chuka", "Chogoria", "23m", "15.8km")
        self.add_edge("Chogoria", "Igoji", "16m", "10.3km")
        self.add_edge("Igoji", "Nkubu", "24m", "16.7km")
        self.add_edge("Nkubu", "Meru", "31m", "16.6km")
        self.add_edge("Meru", "Nanyuki", "81m", "76.2km")
        self.add_edge("Nyeri", "Muiga", "29m", "20.8km")
        self.add_edge("Muiga", "Ndaragwa", "56m", "59.2km")
        self.add_edge("Nanyuki", "Nyeri", "70m", "61.0km")
        self.add_edge("Ndaragwa", "Nyahururu", "30m", "26.2km")
        self.add_edge("Nyahururu", "Bahati", "46m", "42.3km")
        self.add_edge("Bahati", "Nakuru", "39m", "21.0km")
        self.add_edge("Nyahururu", "Dondori", "45m", "36.0km")
        self.add_edge("Dondori", "Nakuru", "60m", "42.8km")
        self.add_edge("Nairobi", "Mai Mahiu", "85m", "53.8km")
        self.add_edge("Mai Mahiu", "Karagita", "43m", "31.1km")
        self.add_edge("Mai Mahiu", "Ntulelei", "55m", "60.3km")
        self.add_edge("Karagita", "Naivasha", "15m", "7.2km")
        self.add_edge("Naivasha", "Gilgil", "39m", "30.4km")
        self.add_edge("Gilgil", "Nakuru", "61m", "42.0km")
        self.add_edge("Ntulelei", "Narok", "30m", "28.8km")
        self.add_edge("Narok", "Bomet", "82m", "81.0km")
        self.add_edge("Bomet", "Keroka", "65m", "56.9km")
        self.add_edge("Keroka", "Keumbu", "20m", "14.3km")
        self.add_edge("Keumbu", "Kisii", "18m", "12.2km")
        self.add_edge("Kisii", "Rongo", "36m", "26.0km")
        self.add_edge("Rongo", "Homa Bay", "38m", "31.0km")
        self.add_edge("Homa Bay", "Kendu Bay", "33m", "31.2km")
        self.add_edge("Kendu Bay", "Ahero", "53m", "53.3km")
        self.add_edge("Kisii", "Oyugis", "38m", "25.3km")
        self.add_edge("Oyugis", "Sondu", "40m", "38.0km")
        self.add_edge("Sondu", "Ahero", "18m", "29.5km")
        self.add_edge("Ahero", "Kisumu", "32m", "23.5km")
        self.add_edge("Muhoroni", "Ahero", "51m", "37.7km")
        self.add_edge("Kapsoit", "Muhoroni", "42m", "28.6km")
        self.add_edge("Kericho", "Kapsoit", "16m", "11.3km")
        self.add_edge("Londiani", "Kericho", "52m", "49.0km")
        self.add_edge("Molo", "Londiani", "31m", "22.1km")
        self.add_edge("Rongai", "Molo", "73m", "46.7km")
        self.add_edge("Nakuru", "Rongai", "58m", "33.2km")

    def dijkstras(self,start_node):
        distances = {towns:float('inf') for towns in self.adjacent}
        distances[start_node] = 0
        previous_nodes = {towns:None for towns in self.adjacent}
        pq=[(0,start_node)]

        while pq:
            current_distance,current_town = heapq.heappop(pq)
            if current_distance > distances[current_town]:
                continue

            for neighbor,time,distance_between in self.adjacent[current_town]:
                distance = current_distance + float(time[:-1])

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_town
                    heapq.heappush(pq,(distance,neighbor))

        return distances,previous_nodes

    def get_shortest_path(self,start_node,end_node):
        distances,previous_nodes = self.dijkstras(start_node)

        path = []
        current = end_node
        while current is not None:
               path.insert(0,current)
               current = previous_nodes[current]

        return distances[end_node],path

NaiToKis = directed_graph()
NaiToKis.build()
shortest_path,path = NaiToKis.get_shortest_path('Nairobi','Kisumu')
print("Shortest path distance is "+str(shortest_path/60)+" hours.")
print("Path followed is:")
print(path)