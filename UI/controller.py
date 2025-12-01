import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            float(self._view.guadagno_medio_minimo.value)
            count = 1
            self._model.costruisci_grafo(self._view.guadagno_medio_minimo.value)
            numero_di_hubs = self._model.get_num_nodes()
            numero_di_tratte = self._model.get_num_edges()
            self._view.lista_visualizzazione.clean()
            stringa_hubs = f"Numero di Hubs: {numero_di_hubs}"
            stringa_tratte = f"Numero di Tratte: {numero_di_tratte}"
            self._view.lista_visualizzazione.controls.append(ft.Text(stringa_hubs))
            self._view.lista_visualizzazione.controls.append(ft.Text(stringa_tratte))
            tratte = self._model.get_all_edges()
            for tratta in tratte:
                self._view.lista_visualizzazione.controls.append(ft.Text(tratta))
            self._view.update()
        except ValueError:
            self._view.show_alert("Errore: inserire un campo numerico in 'Guadagno medio minimo'")
