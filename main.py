"""Demonstration de la mediatheque. C'est ici, et seulement ici, qu'on
fait des print() : les classes du package restent testables et muettes."""

from mediatheque import DVD, DocumentIndisponible, Document, Livre, Mediatheque, TropDEmprunts


def main():
    mediatheque = Mediatheque("Mediatheque de Dakar")

    mediatheque.ajouter_document(
        Livre("L'Aventure ambigue", 1961, "L001", auteur="Cheikh Hamidou Kane", nb_pages=191)
    )
    mediatheque.ajouter_document(
        DVD("Camp de Thiaroye", 1988, "D001", realisateur="Sembene Ousmane", duree_min=147)
    )
    mediatheque.ajouter_document(
        Livre("Une si longue lettre", 1979, "L002", auteur="Mariama Ba", nb_pages=131)
    )
    mediatheque.ajouter_document(
        Livre("Les Bouts de bois de Dieu", 1960, "L003", auteur="Sembene Ousmane", nb_pages=280)
    )

    awa = mediatheque.inscrire("Awa Diop")

    pret = mediatheque.emprunter(awa.numero, "L001")
    print(pret)  # Livre "L'Aventure ambigue" (1961) - a rendre sous 21 jours
    print(len(awa))  # 1

    try:
        mediatheque.emprunter(awa.numero, "L001")
    except DocumentIndisponible as err:
        print("Impossible :", err)

    try:
        Document("x", 2020, "C1")
    except TypeError as err:
        print("Document est bien abstraite :", err)

    # Awa emprunte encore deux documents : elle atteint la limite de 3.
    mediatheque.emprunter(awa.numero, "D001")
    mediatheque.emprunter(awa.numero, "L002")
    try:
        mediatheque.emprunter(awa.numero, "L003")
    except TropDEmprunts as err:
        print("Trop d'emprunts :", err)

    print("Recherche 'aventure' :", [str(d) for d in mediatheque.rechercher("aventure")])

    mediatheque.rendre(awa.numero, "L001")
    print(len(awa))  # 1

    print("Documents disponibles :")
    for doc in mediatheque.documents_disponibles():
        print(doc)  # le meme appel, un affichage different : polymorphisme


if __name__ == "__main__":
    main()
