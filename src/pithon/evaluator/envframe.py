class EnvFrame:
    """
    Représente un environnement d'exécution pour les variables (frame).

    Cette classe permet de stocker des variables dans un contexte local,
    tout en pouvant référencer un environnement parent pour la recherche
    de variables non définies localement (chaînage lexical).

    Attributs :
        vars (dict) : Dictionnaire associant les noms de variables à leurs valeurs.
        parent (EnvFrame ou None) : Référence vers l'environnement parent, ou None si racine.

    Méthodes :
        lookup(name) : Recherche la valeur d'une variable dans l'environnement courant,
                       puis récursivement dans les parents si nécessaire.
        insert(name, value) : Insère ou met à jour une variable dans l'environnement courant.
    """
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def lookup(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent is not None:
            return self.parent.lookup(name)
        else:
            raise NameError(f"Variable '{name}' non définie.")

    def insert(self, name, value):
        self.vars[name] = value
