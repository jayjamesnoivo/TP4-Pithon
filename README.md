# TP4 – Projet Pithon

Travail pratique pour le cours **420-910-MA** – Hiver 2025  
Auteur : **Jeremy-James Noivo**

# Objectif
Ajouter au langage Pithon :
- La gestion des erreurs via des exceptions
- L’implémentation des classes (sans héritage)
- Des tests unitaires pertinents

# Structure du dépôt

| Fichier         | Description                                 |
|-----------------|---------------------------------------------|
| `evaluator.py`  | Contient la logique d’évaluation du langage |
| `syntax.py`     | Définit la grammaire du langage             |
| `cli.py`        | Interface en ligne de commande              |
| `tests/`        | Tests unitaires pour les fonctionnalités    |

# Branche de développement
Les développements ont été faits dans la branche `develop` puis fusionnés dans `main` pour la remise.

# Installation
```bash
git clone https://github.com/jayjamesnoivo/TP4-Pithon.git
cd TP4-Pithon
python3 cli.py
