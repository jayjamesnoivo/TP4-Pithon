# Projet Pithon – TP4 Jeremy

# Exécution

Lancez `cli.py` pour exécuter un programme Pithon :

```bash
python cli.py
```

# Exemple de programme

```python
programme = [
    ["class", "Personne", {
        "__init__": [
            ["setattr", "self", "nom", ["get", "args", 0]]
        ],
        "__str__": [
            ["+", "Nom: ", ["get", "self", "nom"]]
        ]
    }],
    ["set", "p", ["new", "Personne", "Jeremy"]],
    ["print", "p"]
]
```

# Auteurs

- Jeremy-James Noivo