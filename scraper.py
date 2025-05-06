import os
from bs4 import BeautifulSoup

# Chemin vers le dossier contenant les fichiers HTML
DOSSIER = "./"  # adapte si nécessaire

# Nom du fichier d'index
INDEX_FILE = os.path.join(DOSSIER, "index.html")

# Fonction pour extraire les formations depuis une page HTML
def extraire_formations(fichier_html):
    formations = []
    with open(fichier_html, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="formation")
        for div in divs:
            titre = div.find("h2").text.strip()
            duree_texte = div.find("span", class_="duree").text.strip()
            description = div.find("p", class_="description").text.strip()
            # Extraction du nombre de semaines
            nb_semaines = int(duree_texte.split(":")[1].strip().split()[0])
            formations.append({
                "titre": titre,
                "duree": nb_semaines,
                "description": description
            })
    return formations

# Lire les domaines dans index.html
def recuperer_domaines():
    domaines = {}
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        liens = soup.find_all("a")
        for lien in liens:
            nom = lien.text.strip().lower()
            href = lien["href"]
            domaines[nom] = os.path.join(DOSSIER, href)
    return domaines

# Lancer le script
def main():
    domaines = recuperer_domaines()
    print("Domaines disponibles :", ", ".join(domaines.keys()))

    domaine_choisi = input("Choisissez un domaine : ").strip().lower()
    duree_min = int(input("Durée minimale (en semaines) : ").strip())

    if domaine_choisi not in domaines:
        print("Domaine non trouvé.")
        return

    fichier_domaine = domaines[domaine_choisi]
    formations = extraire_formations(fichier_domaine)
    filtres = [f for f in formations if f["duree"] >= duree_min]

    if not filtres:
        print("Aucune formation trouvée.")
        return

    with open("resultats.txt", "w", encoding="utf-8") as f_out:
        for f in filtres:
            texte = f"- {f['titre']} ({f['duree']} semaines)\n  {f['description']}\n"
            print(texte)
            f_out.write(texte)

if __name__ == "__main__":
    main()

