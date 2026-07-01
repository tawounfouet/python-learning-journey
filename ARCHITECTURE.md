# Architecture du curriculum Python

Ce document décrit la structure et la philosophie du parcours d'apprentissage.

---

## Principe général

Le curriculum suit une progression **linéaire par phases**, du débutant absolu à un niveau avancé/expert. Chaque phase s'appuie sur la précédente. L'apprenant peut ensuite se spécialiser dans un domaine (Web, Data, DevOps).

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5
(Bases)     (Outils)    (Pratiques)  (Frameworks) (Expert)
```

---

## Structure des phases

```
learn/
├── 01-basics/           ← 3 fichiers (92 KB) — Rédigé
├── 02-tools/            ← 2 fichiers (77 KB) — Rédigé
├── 03-best-practices/   ← .gitkeep seulement   ┐
├── 04-frameworks/       ← .gitkeep seulement    ├─ Stubs (à rédiger)
└── 05-advanced/         ← .gitkeep seulement   ┘
```

### Phase 1 — Fondamentaux (🌱)

**Objectif** : Donner les bases solides de Python et configurer l'environnement.

| Fichier | Dépendances |
|---|---|
| `introduction.md` | Aucune — point d'entrée |
| `python-concepts.md` | Introduction comprise |
| `environment-setup.md` | Concepts de base compris |

### Phase 2 — Outils (🔧)

**Objectif** : Maîtriser l'écosystème de développement Python moderne.

| Fichier | Dépendances |
|---|---|
| `package-managers.md` | Environnement Python installé |
| `development-tools.md` | Packages compris |

### Phase 3 — Bonnes Pratiques (📚) *— à rédiger*

**Objectif** : Écrire du code propre, typé, testé et maintenable.

### Phase 4 — Frameworks (🚀) *— à rédiger*

**Objectif** : Appliquer Python dans des contextes réels (Web, Data, Desktop).

### Phase 5 — Expert (🏆) *— à rédiger*

**Objectif** : Maîtriser l'asynchrone, le déploiement et l'architecture.

---

## Parcours de spécialisation

Après la phase 2, l'apprenant peut choisir une branche :

```
                ┌── Phase 3 ──► 04-frameworks/web-frameworks.md
                │                (Django, FastAPI, Flask)
Phase 1 ──► 2 ──┼── Phase 3 ──► 04-frameworks/data-science.md
                │                (NumPy, Pandas, TensorFlow)
                └── Phase 3 ──► 04-frameworks/cli ou desktop
                                 (Click, Typer / Tkinter, PyQt)
```

Toutes les branches convergent vers la phase 5 (expert).

---

## Ressources additionnelles

- `notebooks/poo-exploration.ipynb` — Exploration OOP interactive, complément des phases 1-2
- `notebooks/PCAP_Python Associate.ipynb` — Préparation certification, niveau intermédiaire
- `hello-world/hello.py` — Premier script de démarrage

---

## Format des fichiers pédagogiques

Chaque fichier `.md` suit une charte graphique commune :
- **Diagrammes ASCII** pour la visualisation des concepts
- **Extraits de code Python** exécutables
- **Liens de progression** en fin de fichier (`→ fichier-suivant.md`)
- **Émoji** pour la catégorisation visuelle
