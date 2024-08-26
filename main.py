# commandI to ask Copilot

def parcours_profondeur(graph, sommet, visite):
    visite.add(sommet)

    for voisin in graph[sommet]:
        if voisin not in visite:
            parcours_profondeur(graph, voisin, visite)

# Exemple d'utilisation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visite = set()
parcours_profondeur(graph, 'A', visite)