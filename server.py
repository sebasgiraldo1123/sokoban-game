import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from controllers import canvasTools
from controllers.modelGame import ModelGame
from controllers.readGame import ReadData


data = ReadData("file.txt").read_data()
routes = ["Select Routes", "BFS", "DFS", "UCS",
          "Beam Search", "Hill climbing", "A*"]
heuristics = ["Select Heuristic", "Manhattan", "Euclidean"]

simulation_params = {
    "data": data,
    "route": mesa.visualization.Choice(name="Route",
                                       value="BFS",
                                       choices=routes),
    "heuristic": mesa.visualization.Choice(name="Heuristic",
                                           value=" ",
                                           choices=heuristics),
}


# Cada agente que se dibuja en el mundo grilla pasa por aquí y toma las características aquí definidas.

def agent_portrayal(agent):
    portrayal = {"Shape": agent.path,
                 "Layer": agent.layer,
                 "w": agent.w,
                 "h": agent.h,
                 }
    return portrayal


rows = len(data)
columns = len(data[0])

canvas_height, canvas_width = canvasTools.calculate_canvas_dimensions(
    columns, rows, 600)

grid = CanvasGrid(agent_portrayal, columns, rows, canvas_width, canvas_height)
server = ModularServer(ModelGame, [grid], "Sokoban Game",
                       model_params=simulation_params)
server.port = 8521
server.launch()
