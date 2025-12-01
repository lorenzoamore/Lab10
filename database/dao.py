from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta
class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def get_tratte():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        try:
            print("avvio lettura")
            cursor = cnx.cursor(dictionary=True)
            query = """select LEAST(id_hub_origine,id_hub_destinazione) as id_hub_origine,
		                GREATEST (id_hub_origine,id_hub_destinazione) as id_hub_destinazione,
		                AVG(valore_merce) as guadagno_medio
                        from spedizione 
                        group by LEAST(id_hub_origine,id_hub_destinazione),
                        GREATEST (id_hub_origine,id_hub_destinazione)"""
            cursor.execute(query)
            print("query")
            for row in cursor:
                tratta = Tratta(row["id_hub_origine"],row["id_hub_destinazione"],row["guadagno_medio"])
                print(tratta)
                print("stampa delle tratte")
                result.append(tratta)

            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante la query get_attrazioni: {e}")
            result = None

    @staticmethod
    def get_hub():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM hub"""
            cursor.execute(query)
            for row in cursor:
                hub = Hub(row["id"],row["codice"],row["nome"],row["citta"],row["stato"],row["latitudine"],row["longitudine"])
                result.append(hub)

            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(f"Errore durante la query get_attrazioni: {e}")
            result = None
