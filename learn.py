import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import time

# Création de données aléatoires pour les traces
x_data = np.linspace(0, 10, 100)
y_data1 = np.random.rand(100)
y_data2 = np.random.rand(100)

# Création de la figure avec deux sous-graphiques
fig = make_subplots(rows=2, cols=1, subplot_titles=('Trace 1', 'Trace 2'))

# Ajout des traces initiales
trace1 = go.Scatter(x=x_data, y=y_data1, mode='lines', name='Trace 1')
trace2 = go.Scatter(x=x_data, y=y_data2, mode='lines', name='Trace 2')
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=2, col=1)

# Mise en forme du graphique
fig.update_layout(title='Graphique animé en temps réel',
                  xaxis=dict(title='Temps'),
                  yaxis=dict(title='Valeur'),
                  showlegend=True)

# Affichage initial du graphique
fig.show()

# Mise à jour des données et de l'animation en temps réel
for i in range(100):
    # Mise à jour des données
    y_data1 = np.roll(y_data1, -1)
    y_data2 = np.roll(y_data2, -1)
    y_data1[-1] = np.random.rand()  # Ajout d'une nouvelle valeur aléatoire à la fin
    y_data2[-1] = np.random.rand()  # Ajout d'une nouvelle valeur aléatoire à la fin
    
    # Mise à jour des traces dans le graphique
    fig.update_traces(selector=dict(name='Trace 1'), x=x_data, y=y_data1)
    fig.update_traces(selector=dict(name='Trace 2'), x=x_data, y=y_data2)
    
    # Pause pour simuler le temps réel
    time.sleep(0.1)

    # Mise à jour du graphique affiché
    fig.show()
