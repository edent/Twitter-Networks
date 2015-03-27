import graph_tool.all as gt

g = gt.Graph()

# The individual nodes
alice  = g.add_vertex()
bob    = g.add_vertex()
carol  = g.add_vertex()
debbie = g.add_vertex()
elaine = g.add_vertex()

# Connections between nodes
g.add_edge(alice,bob)
g.add_edge(bob,carol)
g.add_edge(bob,debbie)
g.add_edge(bob,elaine)
g.add_edge(carol,bob)

gt.graph_draw(g, 
	vertex_text=g.vertex_index, 
	#vertex_font_size=18,
    output_size=(2000, 2000), 
    output="graph.png")
