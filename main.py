import tkinter as tk
from tkinter import ttk
class GraphUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Graph UI")
        self.root.geometry("400x600")

        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=20)

        self.label_node1 = tk.Label(self.frame_top, text="Node 1:")
        self.label_node1.grid(row=0, column=0, padx=5, pady=5)
        self.node1_entry = tk.Entry(self.frame_top)
        self.node1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_node2 = tk.Label(self.frame_top, text="Node 2:")
        self.label_node2.grid(row=1, column=0, padx=5, pady=5)
        self.node2_entry = tk.Entry(self.frame_top)
        self.node2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.label_edge = tk.Label(self.frame_top, text="Edge Weight:")
        self.label_edge.grid(row=2, column=0, padx=5, pady=5)
        self.edge_entry = tk.Entry(self.frame_top)
        self.edge_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_nodes_button = tk.Button(self.frame_top, text="Add Nodes", command=self.add_node)
        self.add_nodes_button.grid(row=3, column=1, padx=5, pady=10)

        self.frame_middle = tk.Frame(self.root)
        self.frame_middle.pack(pady=20)

        self.label_node = tk.Label(self.frame_middle, text="Node:")
        self.label_node.grid(row=0, column=0, padx=5, pady=5)
        self.node_entry = tk.Entry(self.frame_middle)
        self.node_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_heuristic = tk.Label(self.frame_middle, text="Node Heuristic:")
        self.label_heuristic.grid(row=1, column=0, padx=5, pady=5)
        self.node_heuristic_entry = tk.Entry(self.frame_middle)
        self.node_heuristic_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_node_heuristic_button = tk.Button(self.frame_middle, text="Add Node Heuristic",
                                                   command=self.add_node_heuristic)
        self.add_node_heuristic_button.grid(row=2, column=1, padx=5, pady=10)

        self.start_goal_frame = tk.Frame(self.root)
        self.start_goal_frame.pack(pady=20)

        self.start_label = tk.Label(self.start_goal_frame, text="Start Node:")
        self.start_label.grid(row=0, column=0, padx=5, pady=5)
        self.start_entry = tk.Entry(self.start_goal_frame)
        self.start_entry.grid(row=0, column=1, padx=5, pady=5)

        self.goal_label = tk.Label(self.start_goal_frame, text="Goal Node:")
        self.goal_label.grid(row=1, column=0, padx=5, pady=5)
        self.goal_entry = tk.Entry(self.start_goal_frame)
        self.goal_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.start_goal_frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=1, padx=5, pady=5)

        self.dropdown_frame = tk.Frame(self.root)
        self.dropdown_frame.pack(pady=10)

        self.search_label = tk.Label(self.dropdown_frame, text="Search Algorithm:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)
        self.search_var = tk.StringVar(self.dropdown_frame)
        self.search_var.set("BFS")  # Default value

        # Available search algorithms
        search_algorithms = ["BFS", "DFS", "Uniform Cost", "Depth Limited", "Iterative Deepening", "Bidirectional"]

        self.search_dropdown = tk.OptionMenu(self.dropdown_frame, self.search_var, *search_algorithms,
                                             command=self.update_graph_options)
        self.search_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.graph_label = tk.Label(self.dropdown_frame, text="Graph Type:")
        self.graph_label.grid(row=1, column=0, padx=5, pady=5)
        self.graph_var = tk.StringVar(self.dropdown_frame)

        # Initial available graph types based on the default search algorithm (BFS)
        graph_types = ["Undirected"]
        self.graph_var.set(graph_types[0])  # Default value

        self.graph_dropdown = tk.OptionMenu(self.dropdown_frame, self.graph_var, *graph_types)
        self.graph_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(side=tk.BOTTOM, pady=20, fill=tk.BOTH, expand=True)

        self.results_label = tk.Label(self.results_frame, text="RESULT", font=("Arial", 14, "bold"))
        self.results_label.pack(pady=10)

        self.results_text = tk.Text(self.results_frame, width=60, height=20)
        self.results_text.pack()

        generate_path_button = tk.Button(self.results_frame, text="Generate Path", command=self.generate_path)
        generate_path_button.pack(side=tk.RIGHT, padx=5, pady=5)

        generate_graph_button = tk.Button(self.results_frame, text="Generate Graph", command=self.generate_graph)
        generate_graph_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.root.mainloop()

    def update_graph_options(self, search_algorithm):
        # Update the available graph types based on the selected search algorithm
        if search_algorithm == "BFS":
            graph_types = ["Undirected"]
        elif search_algorithm == "DFS":
            graph_types = ["Undirected"]
        elif search_algorithm == "Uniform Cost":
            graph_types = ["Directed"]
        elif search_algorithm == "Depth Limited":
            graph_types = ["Directed"]
        elif search_algorithm == "Iterative Deepening":
            graph_types = ["Directed"]
        elif search_algorithm == "Bidirectional":
            graph_types = ["Undirected"]
        else:
            graph_types = []

        self.graph_var.set("")  # Clear the current selection
        self.graph_dropdown['menu'].delete(0, 'end')  # Clear the current menu options

        for graph_type in graph_types:
            self.graph_dropdown['menu'].add_command(label=graph_type,
                                                    command=lambda value=graph_type: self.graph_var.set(value))

    def update_graph(self):
        if search_algorithm == "BFS":
            graph_types = ["Undirected"]
            search_algorithms = ["BFS", "Best First", "A*"]
        elif search_algorithm == "DFS":
            graph_types = ["Undirected"]
            search_algorithms = ["DFS"]
        elif search_algorithm == "Uniform Cost":
            graph_types = ["Directed"]
            search_algorithms = ["Uniform Cost"]
        elif search_algorithm == "Depth Limited":
            graph_types = ["Directed"]
            search_algorithms = ["Depth Limited"]
        elif search_algorithm == "Iterative Deepening":
            graph_types = ["Directed"]
            search_algorithms = ["Iterative Deepening"]
        elif search_algorithm == "Bidirectional":
            graph_types = ["Undirected"]
            search_algorithms = ["Bidirectional"]
        else:
            graph_types = []
            search_algorithms = []

        self.graph_var.set("")  # Clear the current selection
        self.graph_dropdown['menu'].delete(0, 'end')  # Clear the current menu options

        self.search_var.set(search_algorithms[0])  # Set the default search algorithm

        for graph_type in graph_types:
            self.graph_dropdown['menu'].add_command(label=graph_type,command=lambda value=graph_type: self.graph_var.set(value))

        self.search_dropdown['menu'].delete(0, 'end')  # Clear the current menu options

        for search_algorithm in search_algorithms:
            self.search_dropdown['menu'].add_command(label=search_algorithm, command=lambda value=search_algorithm: self.search_var.set(value))

    def generate_path(self):
        # Generate the path based on the selected search algorithm
        search_algorithm = self.search_var.get()

        if search_algorithm == "BFS":
            path = self.graph.bfs_search(self.start_entry.get(), self.goal_entry.get())
        elif search_algorithm == "DFS":
            path = self.graph.dfs_search(self.start_entry.get(), self.goal_entry.get())
        elif search_algorithm == "Uniform Cost":
            path = self.graph.uniform_cost_search(self.start_entry.get(), self.goal_entry.get())
        elif search_algorithm == "Depth Limited":
            path = self.graph.depth_limited_search(self.start_entry.get(), self.goal_entry.get())
        elif search_algorithm == "Iterative Deepening":
            path = self.graph.iterative_deepening_search(self.start_entry.get(), self.goal_entry.get())
        elif search_algorithm == "Bidirectional":
            path = self.graph.bidirectional_search(self.start_entry.get(), self.goal_entry.get())
        else:
            path = []

        self.results_text.delete(1.0, tk.END)  # Clear previous results

        if path:
            self.results_text.insert(tk.END, "Path: " + " -> ".join(path))
        else:
            self.results_text.insert(tk.END, "No path found.")

    def generate_graph(self):
        # Generate the graph visualization
        self.graph.generate_visualization()

    def submit(self):
        start_node = self.start_entry.get()
        goal_node = self.goal_entry.get()

        if start_node and goal_node:
            search_algorithm = self.search_algo.get()
            graph_type = self.graph_type.get()

            # Replace this with your own logic
            self.results_text.insert(tk.END, f"Search Algorithm: {search_algorithm}\n")
            self.results_text.insert(tk.END, f"Graph Type: {graph_type}\n")
            self.results_text.insert(tk.END, f"Start Node: {start_node}\n")
            self.results_text.insert(tk.END, f"Goal Node: {goal_node}\n")
            self.results_text.insert(tk.END, "Performing search...\n")

            # Perform the search algorithm and update the results_text accordingly
            # self.results_text.insert(tk.END, "Search results...\n")

    def generate_graph(self):
        # Generate the graph based on the added nodes and node heuristics
        self.results_text.insert(tk.END, "Generating graph...\n")
        # Generate the graph logic goes here
        # self.results_text.insert(tk.END, "Graph generated.\n")

    def generate_path(self):
        # Generate the path based on the search algorithm and graph
        self.results_text.insert(tk.END, "Generating path...\n")
        # Generate the path logic goes here
        # self.results_text.insert(tk.END, "Path generated.\n")

    def add_node(self):
        node1 = self.node1_entry.get()
        node2 = self.node2_entry.get()
        edge_weight = self.edge_entry.get()

        if node1 and node2 and edge_weight:
            # Add the node and its edge weight to the graph
            self.results_text.insert(tk.END, f"Adding Node: {node1}, {node2}, Edge Weight: {edge_weight}\n")
            # Add node logic goes here
        else:
            self.results_text.insert(tk.END, "Please enter all the required information.\n")

    def add_node_heuristic(self):
        node = self.node_entry.get()
        heuristic = self.node_heuristic_entry.get()

        if node and heuristic:
            # Add the node and its heuristic to the graph
            self.results_text.insert(tk.END, f"Adding Node: {node}, Heuristic: {heuristic}\n")
            # Add node heuristic logic goes here
        else:
            self.results_text.insert(tk.END, "Please enter all the required information.\n")

if __name__ == "__main__":
        graph_ui = GraphUI()