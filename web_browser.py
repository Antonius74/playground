"""
1)	visit_page():
	Aggiunge un nuovo URL allo stack della cronologia di navigazione.
	Cancella lo stack “forward”, poiché visitare una nuova pagina rimuove il contesto di navigazione in avanti.
2)	go_back():
	Sposta la pagina corrente nello stack “forward”.
	Estrae l’ultima pagina dallo stack della cronologia come “nuova” pagina corrente.
3)	go_forward():
	Sposta la pagina corrente nello stack della cronologia.
	Estrae l’ultima pagina dallo stack “forward” per navigare in avanti.
4)	Operazioni dello Stack:
	La cronologia viene gestita utilizzando due stack:
	history_stack: Tiene traccia della navigazione all’indietro.
	forward_stack: Tiene traccia della navigazione in avanti.
	Entrambi utilizzano le operazioni dello stack (push e pop) per navigare.
"""


class BrowserHistory:
    def __init__(self):
        # Inizializziamo gli stack vuoti e la pagina corrente
        self.history_stack = []  # Stack per la cronologia indietro
        self.forward_stack = []  # Stack per la cronologia in avanti
        self.current_page = None  # Pagina attualmente visualizzata
    
    def visit_page(self, url):
        # Visita una nuova pagina
        # Se c'è una pagina corrente, la spostiamo nella cronologia
        if self.current_page:
            self.history_stack.append(self.current_page)
        
        # Impostiamo la nuova pagina come pagina corrente
        self.current_page = url
        
        # Puliamo lo stack forward perché stiamo visitando una nuova pagina
        self.forward_stack = []
    
    def go_back(self):
        # Torna alla pagina precedente. 
        # Returns: L'URL della pagina precedente o None se non è possibile tornare indietro
        # Verifichiamo se possiamo tornare indietro
        if not self.history_stack:
            return None
        
        # Spostiamo la pagina corrente nello stack forward
        self.forward_stack.append(self.current_page)
        
        # Prendiamo l'ultima pagina dallo stack della cronologia
        self.current_page = self.history_stack.pop()
        
        return self.current_page
    
    def go_forward(self):
        # Vai alla pagina successiva
        # Returns: L'URL della pagina successiva o None se non è possibile andare avanti
        # Verifichiamo se possiamo andare avanti
        if not self.forward_stack:
            return None
        
        # Spostiamo la pagina corrente nello stack della cronologia
        self.history_stack.append(self.current_page)
        
        # Prendiamo l'ultima pagina dallo stack forward
        self.current_page = self.forward_stack.pop()
        
        return self.current_page


# Creiamo un'istanza della classe BrowserHistory
browser = BrowserHistory()

# Visitiamo alcune pagine
browser.visit_page("google.com")
browser.visit_page("youtube.com")
browser.visit_page("github.com")

# Torniamo indietro
print(browser.go_back())  # Stampa: youtube.com
print(browser.go_back())  # Stampa: google.com

# Andiamo avanti
print(browser.go_forward())  # Stampa: youtube.com

# Visitiamo una nuova pagina
browser.visit_page("python.org")
# Ora lo stack forward è vuoto perché abbiamo visitato una nuova pagina
print(browser.go_forward())  # Stampa: None