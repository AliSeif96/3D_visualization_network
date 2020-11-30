#!/usr/bin/env python
# coding: utf-8

# In[60]:


#/************************************************************************************************/
#/*** Topic: 3D_visualization_network                                                          ***/
#/***                                                                         Ali-Seif         ***/
#/*** Version Release 17.12 rev 11256                                                          ***/
#/*** Date: 12/1/2020                                                                          ***/
#/*** Code implemented in CodeBlocks C++ compiler (v. 17.12),                                  ***/
#/*** MSI: PX60 6QD/ DDR4                                                                      ***/
#/*** Run under a Intel® Core™ i7-6700HQ CPU @ 2.60GHz × 64 based processor with 16 GB RAM     ***/
#/************************************************************************************************/
import igraph as ig
import json
data = []
f = open("datas.txt", "r")
data = json.loads(f.read())
x = data.keys()
N=len(data['nodes'])
L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]
G=ig.Graph(Edges, directed=False)
data['nodes'][0]
labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])   
layt=G.layout('kk', dim=3)
Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
Zn=[layt[k][2] for k in range(N)]# z-coordinates
Xe=[]
Ye=[]
Ze=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    Ze+=[layt[e[0]][2],layt[e[1]][2], None]  
import numpy as np    
import plotly as py
import plotly.graph_objs as go
trace1=go.Scatter3d(x=Xe,
               y=Ye,
               z=Ze,
               mode='lines',
               line=dict(color='rgb(125,125,125)', width=1),
               hoverinfo='none'
               )
trace2=go.Scatter3d(x=Xn,
               y=Yn,
               z=Zn,
               mode='markers',
               name='actors',
               marker=dict(symbol='circle',
                             size=6,
                             color=group,
                             colorscale='Viridis',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               text=labels,
               hoverinfo='text'
               )
axis=dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )
layout = go.Layout(
         title="An Erdos-Renyi network with 40 nodes and a connection probability of 0.4 (3D visualization)",
         width=1000,
         height=1000,
         showlegend=False,
         scene=dict(
             xaxis=dict(axis),
             yaxis=dict(axis),
             zaxis=dict(axis),
        ),
     margin=dict(
        t=100
    ),
    hovermode='closest',
    annotations=[
           dict(
           showarrow=False,
            text="Data source: <a href='https://github.com/aliseif321/3D_visualization_network'>[1] https://github.com/aliseif321/3D_visualization_network/datas.txt</a>",
            xref='paper',
            yref='paper',
            x=0,
            y=0.1,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=14
            )
            )
        
        ],    )

data=[trace1, trace2]
fig=go.Figure(data=data, layout=layout)
fig.show()
fig.write_html("file.html")


# In[ ]:




