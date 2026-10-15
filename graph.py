import pprint
import heapq

class directed_graph:
    """
    - This class specifies all the functionality required to define a python graph
    """

    def __init__(self,directed=True):
        """
            - This is the constructor that specifies the graph is automatically directed for our usecase
            - It also creates the dictionary that we will base all town connections in
        """
        self.directed=directed
        self.adjacent = {}

    def add_vertex(self,vertex):
        """
        - This adds a particular town as a vertex on the graph
            - Towns are only added if they do not already exist in the graph
            - Towns are automatically assigned to be connected to an empty list of neighbours
        """
        
        if vertex not in self.adjacent.keys():
            self.adjacent[vertex] = []

    def add_edge(self,v1,v2,time,distance,directed=True):
        """
        - This is how we add edges or road connections between different towns in the map
            - Before a connection is added, we make sure the vertex/town exists
            - We then specify that the town in connected to a separate town.
            - This is done as appending a list of values to the list of already present neighbours 
        """
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.adjacent[v1].append((v2,time,distance))

        # This is never executed but just goes to show that you can traverse the graph in two ways - to a forward town or back to a previous one
        if not directed:
            self.adjacent[v2].append((v1,time,distance))

    def full_dict(self):
        """
        - Was a debugging utility that just printed the dictionary in a pretty manner (pretty print)
        """
        pprint.pprint(self.adjacent)

    def build(self):
        """
        - Creates the entire graph
        - This is the more detailed graph that forces our trailer to stay on trunk roads
        """

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

    def simple_build(self):
        """
        - Creates the entire graph
        - This is the graph featuring a high degree of abstraction.
        """
        self.add_edge("Nairobi", "Mai Mahiu", "91m", "55.6 km")
        self.add_edge("Mai Mahiu", "Naivasha", "44m", "34.8 km")
        self.add_edge("Mai Mahiu", "Narok", "91m", "89.1 km")
        self.add_edge("Naivasha", "Gilgil", "39m", "30.4 km")
        self.add_edge("Gilgil", "Nakuru", "61m", "42 km")
        self.add_edge("Nakuru", "Kericho", "139m", "107 km")
        self.add_edge("Nakuru", "Londiani", "97m", "64.9 km")
        self.add_edge("Kericho", "Kisumu", "100m", "84 km")
        self.add_edge("Londiani", "Kapsabet", "139m", "116 km")
        self.add_edge("Kapsabet", "Kondele", "64m", "47.8 km")
        self.add_edge("Kondele", "Kisumu", "59m", "32 km")
        self.add_edge("Narok", "Bomet", "87m", "81 km")
        self.add_edge("Bomet", "Kisii", "104m", "92.1 km")
        self.add_edge("Kisii", "Homa Bay", "72m", "108 km")
        self.add_edge("Homa Bay", "Kisumu", "124m", "108 km")

    def dijkstras(self,start_node):
        """
        - This is a classic implementation of dijkstras algorigthm
        - It starts by specifying 2 new dictionaries
            - distances => tracks the shortest path to get to a particular town
            - previous_nodes => tracks the previous node that was used to get to that town
            - we set the start point of the journey to have a distance of 0
        - We also specify a list called pq, which specifies all the new towns that we will traverse
        - So long as there is a town that has not yet been traversed in pq
            - We will pop the top one from the list using the heapq library (Allows us to know that the top item on the stack has the lowest value always )
            - We will then check if the distance already known to get to that town is shorter
                    - If it is we will not change it but will move on
            - If not we will check all the listed towns that are connected to current town
                - We will get a distance to be the current distance to get to the town and add the distance specified by the adjacency list
                - Compare the distance we found and what is currently present
                - If what we found is less, we will update both the previous towns and the distances
                - We will then push that town into pq
            - We will repeat this until the pq is empty.
        - We then return both the dictionary of all the shortest distances as well as the towns that are traversed to get to those towns
        """
        distances = {towns:float('inf') for towns in self.adjacent}
        distances[start_node] = 0
        previous_nodes = {towns:None for towns in self.adjacent}
        pq=[(0,start_node)]

        while pq:
            current_distance,current_town = heapq.heappop(pq)
            if current_distance > distances[current_town]:
                continue

            for neighbor,time,distance_between in self.adjacent[current_town]:
                # distance = current_distance + float(time[:-1])
                distance = current_distance + float(distance_between[:-2])

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_town
                    heapq.heappush(pq,(distance,neighbor))

        return distances,previous_nodes

    def get_shortest_path(self,start_node,end_node):
        """
        - This allows us to get the shortest path after computing the neighbours from dijkstras
        - Provided we know the end node
                - We will perform dijkstras to get the distances and single adjacent towns
                - Specify an empty list called path
                - Traverse the previous_nodes dictionary backwards from the end node until we get to the start node 
                        - updating our path list from the front each time
                - We end by providing the distances and the path
        """
        distances,previous_nodes = self.dijkstras(start_node)

        path = []
        current = end_node
        while current is not None:
               path.insert(0,current)
               current = previous_nodes[current]

        return distances[end_node],path


"""
This section executes everything and allows us to derive the results we wanted.
It shows the shortest paths as well as the times if uncommented (Saw that we were supposed to only include distances but had already spent time checking times)
"""
NaiToKis = directed_graph()
NaiToKis.simple_build()
shortest_path,path = NaiToKis.get_shortest_path('Nairobi','Kisumu')
# print("Shortest path time is "+str(shortest_path/60)+" hours.")
print("Shortest path distance is "+str(shortest_path)+" km.")
print("Path followed is:")
print(path)

NaiToKis.adjacent={}
NaiToKis.build()
shortest_path,path = NaiToKis.get_shortest_path('Nairobi','Kisumu')
# print("Shortest path time is "+str(shortest_path/60)+" hours.")
print("Shortest path distance is "+str(shortest_path)+" km.")
print("Path followed is:")
print(path)