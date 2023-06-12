from Labirinto import Labirinto
from agents import AgentDFS, AgentGreedy, AgentAStar

nlin = 13
ncol = 13

posicao_inicial = [0, 0]
posicao_saida = [nlin - 1, ncol - 1]

l1 = Labirinto(nlin,ncol,0.3,[0,0],[nlin-1,ncol-1]) 
ag = AgentGreedy(l1)
caminho = ag.act()

print(caminho)