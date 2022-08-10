class Cell():
    def __init__(self,value=0, owner=0):
        self.value = value # Ακέραιος που δείχνει την τρέχουσα τιμή του κελιού
        self.owner = owner # Ακέραιος που δείχνει τον ιδιοκτήτη του κελιού
        # Owner:  0=κανένα, 1=κόκκινο, 2=πράσινο


    # Μέθοδος που καλεί την τιμή value του κελιού
    def getValue(self):
        return self.value
    
    # Μέθοδος που θέτει νέα τιμή value του κελιού
    def setValue(self, value):  
        self.value = value
    
    # Μέθοδος που καλεί την τιμή owner (κάτοχο) του κελιού
    def getOwner(self):  
        return self.owner
    
    # Μέθοδος που θέτει νέα τιμή owner του κελιού (νέο κάτοχο)
    def setOwner(self, owner):  
        self.owner = owner

    # Μέθοδος για να μπορούμε να εκτυπώσουμε τη λίστα με τα cells μετά από κάθε αλλαγή ώστε να βλέπουμε αν είναι σωστή
    def __repr__(self):
        rep = 'Cell(' + str(self.value) + ',' + str(self.owner) + ')'
        return rep



class Proximity2(): # Η κλάση του παίκτη
    def __init__(self, pid, length_X, length_Y):
        self.pid = pid # pid=1,2 (Δηλαδή κόκκινο ή πράσινο)
        self.length_X = length_X    # X,Y Ακέραιοι που δείχνουν το μέγεθος του ταμπλό
        self.length_Y = length_Y

    # Μέθοδος που θέτει τιμή στην ταυτότητα του παίκτη
    def setPid(self, pid):          
        self.pid = pid

    # Μέθοδος που θέτει τις διαστάσεις του ταμπλό
    def setBoardSize(self, length_X, length_Y):
        self.length_X = length_X
        self.length_Y = length_Y

    # Μέθοδος που εκτυπώνει το όνομα της ομάδας
    def getPlayerName(self):
        print("Fragkos")

    # Μέθοδος που ελέγχει αν ένα κελί έχει owner και αν δεν έχει, θέτει ως owner του κελιού τον παίκτη
    # lista: το ταμπλό στην τρέχουσα κατάσταση
    def if_getowner_process(self, lista, index):
        if lista[index].getOwner() == 0:
            lista[index].setOwner(self.pid)

    # Μέθοδος για την εύρεση των μη κατειλημμένων γειτονικών κελιών των κελιών που έχουν ήδη owner
    # lista: το ταμπλό στην τρέχουσα κατάσταση
    def findNeighbours(self, lista: list):
        neib_lista = list.copy(lista) # Αντιγραφή του ταμπλό στην τρέχουσα κατάσταση
        
        for i in range(len(neib_lista)): # Διατρέχουμε ένα-ένα τα κελιά του ταμπλό
            if neib_lista[i].getOwner() != 0 and neib_lista[i].getValue() !=0: # Το κελί να είναι κατηλειμμένο στην τρέχουσα κατάσταση του ταμπλό

                # length_Υ άρτιος και η πρώτη γραμμή ξεκινάει από έξω
                if i == 0: # Πρώτο κελί του ταμπλό
                    Proximity2.if_getowner_process(self, neib_lista, 1)
                    Proximity2.if_getowner_process(self, neib_lista, self.length_X)

                elif i == self.length_X - 1: # Τελευταίο κελί της 1ης γραμμής
                    Proximity2.if_getowner_process(self, neib_lista, self.length_X - 2)
                    Proximity2.if_getowner_process(self, neib_lista, 2 * self.length_X - 1)
                    Proximity2.if_getowner_process(self, neib_lista, 2 * self.length_X - 2)

                elif i == (self.length_Y - 1) * self.length_X : # Πάνω αριστερά γωνιακό κελί
                    Proximity2.if_getowner_process(self, neib_lista, (self.length_Y - 2) * self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, (self.length_Y - 1) * self.length_X + 1)
                    Proximity2.if_getowner_process(self, neib_lista, (self.length_Y - 2) * self.length_X + 1)

                elif i == (self.length_X * self.length_Y) - 1 : # Πάνω δεξιά γωνιακό κελί
                    Proximity2.if_getowner_process(self, neib_lista, (self.length_X * self.length_Y) - 2)
                    Proximity2.if_getowner_process(self, neib_lista, (self.length_Y - 1) * self.length_X - 1)


                elif i > (self.length_Y-1)*self.length_X and i < (self.length_X * self.length_Y) - 1: # Το κελί να είναι στην τελευταία γραμμή
                    Proximity2.if_getowner_process(self, neib_lista, i - 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + 1)
                    Proximity2.if_getowner_process(self, neib_lista, i - self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, i - self.length_X + 1)

                elif i < self.length_X - 1 and i > 0: # Να είναι στην 1η γράμμη
                    Proximity2.if_getowner_process(self, neib_lista, i - 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, i + self.length_X - 1)

                elif i % self.length_X == 0: # Να είναι στην 1η στήλη
                    Proximity2.if_getowner_process(self, neib_lista, i + 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, i - self.length_X)

                    if (i // self.length_X) % 2 == 1: # Αν είναι σε άρτια σειρά, έχει επιπλέον και αυτά για γειτονικά
                        Proximity2.if_getowner_process(self, neib_lista, i + self.length_X + 1)
                        Proximity2.if_getowner_process(self, neib_lista, i - self.length_X + 1)


                elif i % self.length_X == self.length_X - 1: # Να είναι στην τελευταία στήλη
                    Proximity2.if_getowner_process(self, neib_lista, i - 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, i - self.length_X)

                    if (i // self.length_X) % 2 == 0: # Αν είναι σε περιττή σειρά, έχει επιπλέον και αυτά για γειτονικά
                        Proximity2.if_getowner_process(self, neib_lista, i + self.length_X - 1)
                        Proximity2.if_getowner_process(self, neib_lista, i - self.length_X - 1)


                else: # Να είναι οπουδήποτε αλλού στο εσωτερικό του ταμπλό
                    Proximity2.if_getowner_process(self, neib_lista, i - 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + 1)
                    Proximity2.if_getowner_process(self, neib_lista, i + self.length_X)
                    Proximity2.if_getowner_process(self, neib_lista, i - self.length_X)

                    if (i // self.length_X) % 2 == 1: # Άρτια σειρά
                        Proximity2.if_getowner_process(self, neib_lista, i + self.length_X + 1)
                        Proximity2.if_getowner_process(self, neib_lista, i - self.length_X + 1)

                    elif (i // self.length_X) % 2 == 0: # Περιττή σειρά
                        Proximity2.if_getowner_process(self, neib_lista, i + self.length_X - 1)
                        Proximity2.if_getowner_process(self, neib_lista, i - self.length_X - 1)

        return neib_lista

    # Μέθοδος που επιλέγει τη θέση που θα τοποθετηθεί ο δοσμένος αριθμός
    # number: ο τυχαίος αριθμός που δίνεται από το παιχνίδι
    def placeTile(self, number, lista):
        s = 0 # Θα τσεκάρουμε αν είναι ο πρώτος αριθμός που τοποθετείται στο ταμπλό με τη χρήση του μετρητή s
        for i in range(len(lista)): # Παίρνουμε όλα τα στοιχεία της λίστας
            if lista[i].getOwner() != 0: # Αν κάποιο κελί έχει κάτοχο, αλλάζει ο μετρητής
                s += 1                  
        if s == 0: # Αν ο μετρητής είναι 0 μετά το τέλος της for, κανένα κελί δεν έχει κάτοχο, άρα είναι η αρχή του παιχνιδιού
            bestplace = int((self.length_X * self.length_Y) / 2 + self.length_X / 2)
        
        else: # Το παιχνίδι έχει ήδη αρχίσει
            neib_lista = Proximity2.findNeighbours(self, lista)
            bestscore = 0 # Προσωρινό best score
            for index in range(len(neib_lista)):       
                if (neib_lista[index].getOwner() != 0) and (neib_lista[index].getValue() == 0):
                    myneib_lista = Proximity2.findMyNeighbours(self, index)
                    score = 0
                    for i in range(len(myneib_lista)):
                        if lista[myneib_lista[i]].getOwner() == 0:
                           pass
                        elif lista[myneib_lista[i]].getOwner() == self.pid:
                            score += 1
                        else:
                            if lista[myneib_lista[i]].getValue() >= number:
                                pass
                            else:
                                score += lista[myneib_lista[i]].getValue()
                    if score > bestscore:
                        bestscore = score
                        bestplace = index # index του κελιού στη neiblista το οποίο έχει έχει το best score
        return bestplace
                    
            
    # Μέθοδος που μας δίνει τους γείτονες ενός συγκεκριμένου κελιού, ανεξαρτήτως κατόχου και τιμής αυτών
    # chosen_cell: το κελί που έχει επιλεχθεί
    def findMyNeighbours(self, chosen_cell: int):
        neighbours = []
        if chosen_cell == 0: # Οι γείτονες του κελιού 0
            neighbours = [1, self.length_X]

        elif chosen_cell == self.length_X - 1: # Οι γείτονες του κάτω δεξιά κελιού, με θέση length(x)-1
            neighbours = [self.length_X - 2, 2 * self.length_X - 1, 2 * self.length_X - 2]

        elif chosen_cell == (self.length_Y - 1) * self.length_X: # Για το πάνω αριστερά κελί
            neighbours = [(self.length_Y - 2) * self.length_X, (self.length_Y - 2) * self.length_X + 1, chosen_cell + 1]

        elif chosen_cell == (self.length_X * self.length_Y) - 1 : # Για το πάνω δεξιά κελί
            neighbours = [(self.length_X * self.length_Y) - 2, (self.length_Y - 1) * self.length_X - 1]

        elif chosen_cell > (self.length_Y - 1) * self.length_X and chosen_cell < (self.length_X * self.length_Y) - 1 : # Να είναι στην τελευταία γραμμή
            neighbours = [chosen_cell - 1, chosen_cell + 1, chosen_cell - self.length_X, chosen_cell - self.length_X + 1]

        elif chosen_cell < self.length_X - 1 and chosen_cell > 0: # Να είναι στην 1η γράμμη
            neighbours = [chosen_cell - 1, chosen_cell + 1, chosen_cell + self.length_X, chosen_cell + self.length_X - 1]
           
        elif chosen_cell % self.length_X == 0: # Να είναι στην 1η στήλη
            if (chosen_cell // self.length_X) % 2 == 1 : # Περιττή σειρά
                neighbours = [chosen_cell + 1, chosen_cell + self.length_X, chosen_cell - self.length_X]

            if (chosen_cell // self.length_X) % 2 == 0 : # Άρτια σειρά
                neighbours = [chosen_cell + 1, chosen_cell + self.length_X, chosen_cell - self.length_X, chosen_cell + self.length_X + 1, chosen_cell - self.length_X + 1]
                 
        elif chosen_cell % self.length_X == -1: # Να είναι στην τελευταία στήλη
            if (chosen_cell // self.length_X) % 2 == 1: # Άρτια σειρά
                neighbours = [chosen_cell - 1, chosen_cell + self.length_X, chosen_cell - self.length_X]
                       
            if (chosen_cell // self.length_X) % 2 == 0: # Περιττή σειρά (1,3,5,...)
                neighbours = [chosen_cell - 1, chosen_cell + self.length_X, chosen_cell - self.length_X, chosen_cell + self.length_X - 1, chosen_cell - self.length_X - 1]
                
        else: # Να είναι οπουδήποτε αλλού στο εσωτερικό του ταμπλό
            if (chosen_cell // self.length_X) % 2 == 1: # Άρτια σειρά 2,4,6,...
                neighbours = [chosen_cell - 1, chosen_cell + 1, chosen_cell + self.length_X, chosen_cell - self.length_X, chosen_cell + self.length_X + 1, chosen_cell - self.length_X + 1]
                     
            if (chosen_cell // self.length_X) % 2 == 0: # Περιττή σειρά 1,3,5,...
                neighbours = [chosen_cell - 1, chosen_cell + 1, chosen_cell + self.length_X, chosen_cell - self.length_X, chosen_cell + self.length_X - 1, chosen_cell - self.length_X - 1]
        return neighbours

    # Μέθοδος που τοποθετεί τον αριθμό στην θέση που του έχει υποδείξει η placeTile και αλλάζει τα γειτονικά κελιά με βάση τους κανόνες
    def applyChanges(self, number, lista):
        bestplace = Proximity2.placeTile(self, number, lista)
        lista[bestplace].setOwner(self.pid)
        lista[bestplace].setValue(number)
        myneibs = Proximity2.findMyNeighbours(self, bestplace)
        for i in range(len(lista)): # Αναιρεί την αλλαγή του κατόχου που έκανε η findNeighbours στα γειτονικά κελιά
            if lista[i].getValue() == 0:    
                lista[i].setOwner(0)
        for i in range(len(myneibs)):   # Αλλαγές των κελιών που είναι γειτονικά με το κελί που επιλέχθηκε για να τοποθετηθεί ο αριθμός
            if lista[myneibs[i]].getOwner() == self.pid:    # Αυξάνεται κατά 1 αν είναι του παίκτη
                s = lista[myneibs[i]].getValue()
                lista[myneibs[i]].setValue(s+1)
            elif lista[myneibs[i]].getOwner() == 0: # Δεν αλλάζει τίποτα
                pass
            else:
                if lista[myneibs[i]].getValue() >= number:  # Διατηρεί το κελί ως έχει ή αλλάζει τον owner
                    pass
                else:
                    lista[myneibs[i]].setOwner(self.pid)
        return lista


''' #Δοκιμή για την findNeighbours:
paiktis = Proximity2(2, 10, 10)
tablo = [Cell(), Cell(), Cell(15, 1), Cell(8, 2), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
geitones = Proximity2.findNeighbours(paiktis, tablo)
print(geitones)
'''

'''
#Δοκιμή της λειτουργίας της placeTile για ταμπλό διαστάσεων 8x6:
#αν ειναι η αρχη του παιχνιδιου
tablo_arxi = [Cell() for i in range(48)]
paiktis = Proximity2(2, 8, 6)
keli_arxi = Proximity2.placeTile(paiktis, 20, tablo_arxi)
print(keli_arxi)
'''

'''
#Δοκιμή της λειτουργίας της applyChanges για ταμπλό διαστάσεων 8x6:
#αν ειναι η αρχη του παιχνιδιου
tablo_arxi = [Cell() for i in range(48)]
paiktis = Proximity2(2, 8, 6)
allagmeni = Proximity2.applyChanges(paiktis, 20, tablo_arxi)
print(allagmeni)
'''


'''#Δοκιμή της λειτουργίας της placeTile για το παρακάτω ταμπλό:
paiktis = Proximity2(2, 8, 6)
tablo = [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(18, 2), Cell(1, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 2), Cell(18, 1), Cell(16, 2), Cell(20, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(4, 1), Cell(17, 1), Cell(18, 1), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 1), Cell(16, 1), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
keli = Proximity2.placeTile(paiktis, 20, tablo)
print(keli)
'''

'''
#Δοκιμή της λειτουργίας της applyChanges για το παρακάτω ταμπλό:
paiktis = Proximity2(2, 8, 6)
tablo = [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(18, 2), Cell(1, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 2), Cell(18, 1), Cell(16, 2), Cell(20, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(4, 1), Cell(17, 1), Cell(18, 1), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 1), Cell(16, 1), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
allagmeni = Proximity2.applyChanges(paiktis, 20, tablo)
print(allagmeni)
'''


'''
#Δοκιμή της λειτουργίας της findMyNeighbours για το παρακάτω ταμπλό:
paiktis = Proximity2(2, 8, 6)
tablo = [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(18, 2), Cell(1, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 2), Cell(18, 1), Cell(16, 2), Cell(20, 2), Cell(), Cell(),
         Cell(), Cell(), Cell(4, 1), Cell(17, 1), Cell(18, 1), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(13, 1), Cell(16, 1), Cell(), Cell(), Cell(), Cell(),
         Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
geitones = Proximity2.findMyNeighbours(paiktis, 36)
print(geitones)
'''