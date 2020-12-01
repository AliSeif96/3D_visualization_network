# 3D visualization network
## Three-dimensional visualization of the structure of a network


You can view the 3D visualization network  [here]( http://pythonfigure.gigfa.com/) 

[![plotly](https://www.vectorlogo.zone/logos/plot_ly/plot_ly-ar21.svg)](https://plotly.com//)


<p align="center">
 <img src="https://raw.githubusercontent.com/aliseif321/3D_visualization_network/main/Pictures/fig1.png" >
 </p>



# An Erdos-Renyi network with 40 nodes and a connection probability of 0.4 (3D visualization)

We define our graph as an igraph.Graph object. Python igraph is a library for high-performance graph generation and analysis. Install the Python library with sudo pip install python-igraph.


```sh
import igraph as ig
```

Read graph data from a json file:



```sh
import json
data = []
f = open("datas.txt", "r")
data = json.loads(f.read())
x = data.keys()
```


[u'nodes', u'links']

Get the number of nodes:

```sh
N=len(data['nodes'])
N
```

40


Define the list of edges and the Graph object from Edges:


```sh
L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

G=ig.Graph(Edges, directed=False)
```



Extract the node attributes, 'group', and 'name':

```sh
data['nodes'][0]
```
{u'group': 1, u'name': u'Myriel'}

```sh
labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])
```

Get the node positions, set by the Kamada-Kawai layout for 3D graphs:

```sh
layt=G.layout('kk', dim=3)
```

layt is a list of three elements lists (the coordinates of nodes):

```sh
layt[5]
```

[-0.4253241855250862, 0.8963644913019184, 1.0743554858169682]


Set data for the Plotly plot of the graph:

```sh
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
```


```sh
import plotly.plotly as py
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
         title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
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
            text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
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
```      

```sh
data=[trace1, trace2]
fig=go.Figure(data=data, layout=layout)

py.iplot(fig, filename='Les-Miserables')     
``` 

        


<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~priyatharsan/186.embed" height="1000px" width="1000px">





<html>
 
 
<head>
 
 
	<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery-1.8.0.min.js"></script>
 
 
</head>


<body>
 
 
	<script type="text/javascript">
 
 
		function doCall(){
  
  
			$.get('foo').error(function(){
   
   
				parent.afterCall();
    
    
			});
   
   
		}
  
  
	</script>
 
 
</body>


</html>	
