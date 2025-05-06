# 🕸️ Exercice de Scraping en python

## Objectif

Ce projet a pour but d’apprendre à faire du **web scraping** à partir de **fichiers HTML statiques** en utilisant **Python**, **requests.Session** et **BeautifulSoup**. L'exercice simule un site web d'une entreprise fictive, **SkillMaster**, qui propose des formations dans différents domaines.

## Compétences visées

- Manipulation de fichiers HTML locaux
- Parcours automatique de pages web
- Extraction de données structurées (titre, durée, description)
- Filtrage des données selon des critères
- Écriture de résultats dans un fichier texte

## Structure du site (fichiers fournis)

- `index.html` : page d'accueil avec les liens vers les domaines.
- `dev.html` : liste des formations en développement.
- `cyber.html` : liste des formations en cybersécurité.
- `data.html` : liste des formations en data science.
- `scraper.py` : script Python principal à exécuter pour lancer le scraping.

## Fonctionnement du script `scraper.py`

Le script effectue les étapes suivantes :

1. Lit le fichier `index.html` pour détecter les domaines disponibles.
2. Demande à l'utilisateur de choisir un domaine (ex : `data`, `dev`, `cyber`) et une **durée minimale** (en semaines).
3. Ouvre la page HTML correspondant au domaine choisi.
4. Extrait toutes les **formations** de cette page :
   - Titre de la formation
   - Durée (en semaines)
   - Description
5. Filtre les formations dont la durée est supérieure ou égale à celle indiquée.
6. Affiche les résultats filtrés dans le terminal.
7. Sauvegarde les résultats dans un fichier `resultats.txt`.

## Exemple d'utilisation

```
$ python scraper_formations.py
Domaines disponibles : développement, cybersécurité, data science
Choisissez un domaine : data
Durée minimale (en semaines) : 4

- Statistiques appliquées (4 semaines)
  Comprendre les statistiques pour analyser des données réelles.

- Introduction au Machine Learning (6 semaines)
  Découvrez les algorithmes de base et appliquez-les avec scikit-learn.
```

## Pré-requis

- Python 3.x
- Bibliothèque `beautifulsoup4` installée :
```bash
pip install beautifulsoup4
```

## Conseils

- Place tous les fichiers HTML et le script `scraper.py` dans le **même dossier**.
- Le script lit les fichiers avec des chemins relatifs (`./`).

## Résultat

Un fichier `resultats.txt` est généré avec les formations filtrées selon vos critères.

---

## Contribution

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration ou si vous trouvez des bugs, n'hésitez pas à ouvrir une *issue* ou une *pull request*.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer, sous réserve de maintenir la licence originale dans toutes les copies ou versions dérivées.

---

Merci d'avoir exploré ce projet ! N'hésitez pas à me contacter pour toute question ou suggestion d'amélioration.

---

## 👨‍💻 Auteur

Projet réalisé par **Jayson MOOKEN**.
🔗 [Mon profil LinkedIn](https://www.linkedin.com/in/jayson-mooken/)

---
