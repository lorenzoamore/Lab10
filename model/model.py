from database.dao import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        tratte = DAO.get_tratte()
        for tratta in tratte:
            if float(tratta.guadagno_medio) >= float(threshold):
                for hub in DAO.get_hub():
                    # trasformo l'id in : nome(città)
                    if tratta.id_hub_origine == hub.id:
                        tratta.id_hub_origine = f"{hub.nome}({hub.stato})"
                    if tratta.id_hub_destinazione == hub.id:
                        tratta.id_hub_destinazione = f"{hub.nome}({hub.stato})"
                self.G.add_edge(tratta.id_hub_origine, tratta.id_hub_destinazione,weight=tratta.guadagno_medio)

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        count = 0
        for edge in self.G.edges():
            count +=1
        return count

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        hubs = DAO.get_hub()
        return len(hubs)


    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        count = 1
        tratte = []
        for nodo1, nodo2 in self.G.edges():
            guadagno_medio = self.G[nodo1][nodo2]["weight"]
            stringa = f"{count}) [{nodo1} -> {nodo2}] --- guadagno Medio per Spedizione €{guadagno_medio}"
            count += 1
            tratte.append(stringa)
        return tratte


