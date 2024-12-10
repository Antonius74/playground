"""
Ecco un esercizio più complesso che combina strutture dati avanzate e analisi Big-O:

Esercizio: Sistema di Gestione di Ordini in Tempo Reale

Sei incaricato di creare un sistema per gestire un gran numero di ordini in un mercato online. 
Ogni ordine ha un timestamp, un ID cliente e un importo totale. 
Devi gestire gli ordini in tempo reale, ottimizzando diverse operazioni.

Operazioni da implementare

	1.	Aggiungi un ordine:
	•	Ogni ordine è rappresentato da un dizionario o una struttura simile con campi: timestamp, customer_id, amount.
	•	Devi aggiungerlo in una struttura che consenta di gestire facilmente le operazioni richieste.
	2.	Trova l'ordine con il massimo importo:
	•	Restituisci l'ordine con l'importo più alto. Questa operazione deve essere più efficiente possibile.
	3.	Trova gli ordini per un cliente specifico:
	•	Dato un customer_id, restituisci una lista degli ordini di quel cliente, ordinati per timestamp.
	4.	Cancella un ordine:
	•	Dato l'ID cliente e il timestamp, rimuovi l'ordine corrispondente.
	5.	Trova il totale degli ordini in un intervallo di tempo:
	•	Dati due timestamp, calcola la somma degli importi di tutti gli ordini in quell'intervallo.

Requisiti

	•	Gli ordini possono essere molto numerosi (ad esempio, milioni).
	•	Devi ottimizzare le operazioni chiave:
	•	Inserire un nuovo ordine.
	•	Recuperare il massimo importo.
	•	Filtrare e ordinare per cliente.
	•	Effettuare operazioni temporali.

Strutture dati suggerite (studiati queste strutture, nel corso propbabilmente avrai visto solo i dizionari. Se non trovi materiale fammi sapere che ti giro qualche video su yt)

	•	Heap: Per trovare rapidamente l’ordine con il massimo importo.
	•	Dizionari indicizzati: Per organizzare gli ordini per cliente o timestamp.
	•	Segment Tree o Fenwick Tree: Per calcolare velocemente il totale degli importi in un intervallo temporale.
	•	B-tree o AVL-tree: Per gestire le query ordinate su timestamp.

Implementazione Base

Classe OrderManager

Una struttura dati che contiene:
	•	Un heap per mantenere il massimo importo.
	•	Un dizionario indicizzato per cliente (customer_orders).
	•	Un dizionario o una struttura indicizzata per timestamp.
"""

# Aggiungi ordini
manager.add_order(1, "cliente1", 100.0)
manager.add_order(2, "cliente2", 200.0)
manager.add_order(3, "cliente1", 150.0)

# Ordine massimo
print("Ordine massimo:", manager.get_max_order())

# Ordini di un cliente
print("Ordini di cliente1:", manager.get_orders_by_customer("cliente1"))

# Totale in un intervallo temporale
print("Totale tra timestamp 1 e 2:", manager.get_total_in_time_range(1, 2))

# Rimuovi un ordine
manager.remove_order(1, "cliente1")
print("Ordini di cliente1 dopo la rimozione:", manager.get_orders_by_customer("cliente1"))

"""
Analisi della complessità in termini di bigO per ogni metodo/funzione

Obiettivo

	•	Migliora la struttura dati per ottenere complessità ancora più basse.
	•	Implementa e testa casi limite (es. milioni di ordini). Fai uno script di simulazione che inserisca 1mln di dati e poi verifia il tempo di esecuzione delle fuznioni di ricerca.
"""