import graphviz
import pandas as pd


data = pd.read_excel('Your_excel.xlsx')


from_value = data['From(Column name)'].iloc[0]


g = graphviz.Digraph(format='svg', engine='dot')


node_shape = 'ellipse'
node_style = 'filled'
node_color = 'white'
node_fontsize = '12'

edge_color = 'black'


unique_nodes = set()


for index, row in data.iterrows():
    current_from = row['From']
    to_value = row['to(Column name)']
    unique_nodes.add(current_from)
    unique_nodes.add(to_value)

for node in unique_nodes:
    g.node(node, shape=node_shape, style=node_style, fillcolor=node_color, fontsize=node_fontsize)


for index, row in data.iterrows():
    current_from = row['From']
    action_value = row['action(Column name)']
    to_value = row['to']


    g.node(current_from, shape=node_shape, style=node_style, fillcolor=node_color, fontsize=node_fontsize)
    g.node(to_value, shape=node_shape, style=node_style, fillcolor=node_color, fontsize=node_fontsize)

   
    g.edge(current_from, to_value, label=action_value, color=edge_color)


for index in range(len(data) - 1):
    current_to = data.loc[index, 'to']
    next_from = data.loc[index + 1, 'From']
    g.edge(current_to, next_from, color=edge_color)


filename = f'{from_value}_flowchart'
g.render(filename, format='svg', cleanup=True)
