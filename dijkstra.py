#class that represents one point in the Graf structure
class Point:
    def __init__(self, point_name: str):
        self.name = point_name
        self.connections = {}
        self.fastest_route = ""

    def add_connection(self, name: str, distance: float):
        self.connections[name] = distance


#data structure that stores all points and main engine of the application
class Graf:
    def __init__(self, name):
        self.all_points = {}    #structure that stores key and value in this way -> {node_name: Node_obj, ...}
        self.name = name

    def add_node(self, new_point: Point):
        if new_point in self.all_points.keys():
            print(f"Can't add point {new_point.name}, point with this name already exist")
        else:
            self.all_points[new_point.name] = new_point
            print(f"Created new point '{new_point.name}'")

    def add_two_points_connection(self, point1_name: str, point2_name: str, distance: float):
        #add if exists
        if point1_name in self.all_points.keys() and point2_name in self.all_points.keys():
            self.all_points[point1_name].add_connection(point2_name, distance)
            self.all_points[point2_name].add_connection(point1_name, distance)
            print(f"Created connection between {point1_name} and {point2_name}: distance {distance}")
            return True

        # error handler
        if point1_name not in self.all_points.keys():
            print(f"Point {point1_name} does not exist")
        if point2_name not in self.all_points.keys():
            print(f"Point {point2_name} does not exist")
        return False


    def print_graf(self):
        print(f"\n'{self.name}' connections:")
        for point in list(self.all_points.keys()):
            print(f"point: {point}, connections:", end="")
            print(self.all_points[point].connections)


    def djikstra_calculate(self, start_point: str, destination_point: str):
        explored_nodes = {}                                 #stores names of nodes that has been explored
        unexplored_nodes = {}                               #values of the unexplored nodes (updates in each loop)
        current_point = self.all_points[start_point]        #current node that we are exploring in each loop iteration

        unexplored_nodes[current_point.name] = 0
        while True:
            if current_point.name == destination_point:
                break
            for connection in list(current_point.connections.keys()):
                if connection in explored_nodes:
                    continue
                if connection not in unexplored_nodes:
                    unexplored_nodes[connection] = current_point.connections[connection] + unexplored_nodes[current_point.name]
                    self.all_points[connection].fastest_route = current_point.name
                else:
                    new_estimate = unexplored_nodes[current_point.name] + current_point.connections[connection]
                    if new_estimate < unexplored_nodes[connection]:
                        unexplored_nodes[connection] = new_estimate
                        self.all_points[connection].fastest_route = current_point.name

            explored_nodes[current_point.name] = unexplored_nodes[current_point.name]
            del unexplored_nodes[current_point.name]
            fastest_unexplored = min(unexplored_nodes, key=unexplored_nodes.get)
            current_point = self.all_points[fastest_unexplored]


        result_time = unexplored_nodes[current_point.name]
        result_path = []
        # getting the path of the shortest route
        while True:
            if current_point.fastest_route == "":
                result_path.append(current_point.name)
                break
            else:
                result_path.append(current_point.name)
                current_point = self.all_points[current_point.fastest_route]
        result_path.reverse()

        return result_time, result_path


#testing
graf = Graf("graf2")

graf.add_node(Point("A"))
graf.add_node(Point("B"))
graf.add_node(Point("C"))
graf.add_node(Point("D"))
graf.add_node(Point("E"))
graf.add_node(Point("F"))

graf.add_two_points_connection("A", "B", 4.0)
graf.add_two_points_connection("A", "C", 2.0)
graf.add_two_points_connection("B", "C", 5.0)
graf.add_two_points_connection("B", "D", 10.0)
graf.add_two_points_connection("C", "D", 3.0)
graf.add_two_points_connection("C", "E", 4.0)
graf.add_two_points_connection("D", "F", 11.0)
graf.add_two_points_connection("E", "F", 2.0)
graf.add_two_points_connection("B", "E", 8.0)

graf.print_graf()

start_point = "A"
destination_point = "F"

result = graf.djikstra_calculate(start_point, destination_point)
print(f"\nfastest time between nodes {start_point} and {destination_point}: {result[0]}")
print(f"nodes in the path: {result[1]}")



