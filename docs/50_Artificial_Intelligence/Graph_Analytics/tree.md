# Trees and Forests

!!!note Un **albero** è un grafo non orientato connesso privo di circuiti semplici.

Un grafo non orientato è un albero se e solo se esiste un unico percorso semplice tra qualsiasi coppia di vertici.

**Relazione Vertici-Archi**: In un albero con $n$ vertici, il numero di archi è esattamente $n - 1$.

!!!note Una **foresta** è un grafo non orientato privo di circuiti semplici. Formalmente, è l'unione disgiunta di uno o più alberi. Se un albero è una struttura solitaria, la foresta è una collezione di alberi che non si toccano.

## Traversing a Tree

Esistono metodi sistematici per visitare tutti i vertici di un albero:

- **Preordine** (**Preorder**): Visita la radice, poi ricorsivamente i sottoalberi.
- **Inordine** (**Inorder**): Visita il sottoalbero sinistro, poi la radice, poi il destro (tipico degli alberi binari).
- **Postordine** (**Postorder**): Visita i sottoalberi e infine la radice.
- **Level Order**: Visita i nodi livello per livello, dall'alto verso il basso.

## Spanning Trees

!!!note Dato un grafo semplice $G$, un **albero di copertura** è un sottografo di $G$ che è un albero e contiene tutti i vertici di $G$.

### Minimum Spanning Trees

In un grafo pesato connesso, l'albero di copertura minimo è quello in cui la somma dei pesi degli archi è la minore possibile. Per trovarlo, gli algoritmi standard sono:

- **Algoritmo di Prim**: Costruisce l'albero partendo da un nodo e aggiungendo l'arco più economico connesso ai nodi già scelti.
- **Algoritmo di Kruskal**: Seleziona gli archi in ordine di peso crescente, assicurandosi di non creare cicli.
- **Algoritmo di Eagle**: Un approccio più efficiente per grafi densi, che utilizza una struttura dati chiamata "heap" per gestire gli archi.
