## **LAYOUT**

Alcuni ViewGroup sono designati come **layout** perché organizzano le View figlie in un modo specifico e sono tipicamente usati come **ViewGroup** radice.

I ViewGroup sono definiti nei file di **layout XML**, che si trovano nella cartella layout all'interno della cartella res del progetto Android. La gerarchia delle View, con un ViewGroup alla radice, può diventare complessa in app con molte View sullo schermo. Comprendere questa gerarchia è importante per l'efficienza del rendering e la visibilità delle View. È possibile esplorare la gerarchia delle View di un'app utilizzando l'**Hierarchy Viewer**.

**1. LinearLayout**

Il **LinearLayout** organizza le sue View figlie in una singola direzione: **verticale** o **orizzontale**. Ogni elemento viene disposto uno dopo l'altro, rispettando l'ordine di dichiarazione. È utile quando si desidera una disposizione semplice e sequenziale degli elementi.

**2. RelativeLayout**

Il **RelativeLayout** permette di posizionare le View figlie in relazione tra loro o rispetto al contenitore padre. Ad esempio, un elemento può essere posizionato alla destra di un altro o allineato al bordo superiore del layout. Questo offre una maggiore flessibilità nella disposizione degli elementi rispetto al LinearLayout.

**3. FrameLayout**

Il FrameLayout è progettato per contenere una singola View, ma può gestire anche più elementi sovrapposti. Le View aggiunte successivamente si posizionano sopra le precedenti, creando un effetto di stratificazione. È spesso utilizzato per visualizzare una View principale con elementi sovrapposti, come pulsanti flottanti o indicatori di stato.

**4. ConstraintLayout**

Il **ConstraintLayout** offre un alto grado di flessibilità, permettendo di definire vincoli tra le View per determinare la loro posizione e dimensione. Questo layout è stato introdotto per semplificare la creazione di interfacce complesse senza nidificare più layout, migliorando le prestazioni dell'applicazione.

**6. GridLayout**

Un **GridLayout** (o GridLayoutManager per le liste) organizza gli elementi in **righe e colonne**, creando una struttura a griglia. È utile quando si devono mostrare più elementi con lo stesso peso visivo, come immagini o pulsanti.

**7. StaggeredGridLayout**

Uno **StaggeredGridLayout** è simile a un GridLayout, ma con **colonne o righe di altezze/larghezze diverse**. Questo lo rende perfetto per layout più dinamici e visivamente accattivanti.

![Image: a simplified architecture diagram showing three apps (yellow, red, green) at the top, each connected to a corresponding "Content Resolver" box. All resolvers interact bidirectionally with a central horizontal "Content Provider" layer. The content provider then connects downward to three storage backends: a cloud SQL icon, a database cylinder, and a document/file icon. Arrows indicate request/response flow from apps → resolvers → provider → storage and back.](./Android_images/image_021.png)![- Diagram of Android touch event delivery showing call flow top-to-bottom (notify) and return flow bottom-to-top (handle). - Top: Activity receives dispatchTouchEvent() and may handle in onTouchEvent(). - Middle: Nested containers ViewGroup A and ViewGroup B each get dispatchTouchEvent(), then onInterceptTouchEvent(): - If onInterceptTouchEvent() returns true, the ViewGroup handles the event in its onTouchEvent() (child bypassed). - If false, the event is dispatched down to the next child. - Bottom: Leaf View receives dispatchTouchEvent(); it first gives the event to an OnTouchListener (if present) and then to its onTouchEvent(). - OnTouchListener can consume the event (not shown explicitly) or fall through to onTouchEvent(). - Handling result propagates upward: once a view or viewgroup handles the event, the handled result is returned up the chain to the Activity.](./Android_images/image_022.png)

Il **ConstraintLayout** è un **ViewGroup** in Android che offre un modo flessibile per disporre e allineare le View figlie all'interno di un layout. Utilizza un sistema di **vincoli (constraints)** per determinare la posizione e le dimensioni delle sue View figlie.

Il ConstraintLayout organizza le View figlie utilizzando **punti di ancoraggio**, **bordi e linee guida** per controllare come le View sono posizionate rispetto ad altri elementi nel layout. Un **vincolo** è una connessione o un allineamento a un'altra View, al layout genitore o a una linea guida invisibile.

Ciascun vincolo definisce la posizione della vista lungo l'asse verticale o orizzontale; quindi ogni vista deve avere almeno un vincolo per ogni asse, ma spesso ne sono necessari di più.

![Image with four labeled panels showing common Android view groups and how child views are arranged: - FrameLayout (top-left): light background with two overlapping blue rectangles (children stacked). - LinearLayout (top-right): three blue rectangles laid out side-by-side in a single row (uniform spacing). - RelativeLayout (bottom-left): one large blue rectangle above two smaller side-by-side rectangles (children positioned relative to each other). - ConstraintLayout (bottom-right): a large rectangle and a tall right column with two small rectangles beneath the large one, illustrating flexible constraint-based placement.](./Android_images/image_023.png)**Fissa**: specifica una dimensione specifica nella casella di testo seguente o ridimensionando la vista nell'editor.

![An illustration showing three UI/layout examples side-by-side, each inside a light-blue framed panel with a label below: - Linear: a single vertical column of equal-width horizontal bars stacked top to bottom (a list). - Grid: a uniform 2×3 grid of equal-sized square tiles. - Staggered Grid: two columns of tiles with varying heights arranged like a masonry layout, so rows don’t line up.](./Android_images/image_024.png)**A capo**: la visualizzazione si espande solo per adattarsi ai contenuti.

![A small monochrome icon: a short horizontal line with a short vertical bar at each end, centered on a white background (looks like a dimension/measure or “pinch to expand/contract” style symbol).](./Android_images/image_025.png)**Vincoli di corrispondenza**: la vista si espande il più possibile per soddisfare i vincoli su ogni lato, dopo aver tenuto conto dei margini della vista.
