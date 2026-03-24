# 🔧 Outils de Développement Python Modernes

## 🎯 L'Écosystème des Outils de Développement

```
                    🧰 MODERN PYTHON TOOLBOX 🧰
                    
    Code Quality Pipeline:
    
    Raw Code → Linting → Formatting → Type Check → Testing → Deploy
        │         │          │           │          │         │
        ▼         ▼          ▼           ▼          ▼         ▼
    ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    │ ÉDITEUR │ LINTER  │FORMATTER│ TYPAGE  │ TESTING │ DEPLOY  │
    │         │         │         │         │         │         │
    │ VS Code │ ruff    │ black   │ mypy    │ pytest  │ docker  │
    │ PyCharm │ flake8  │ autopep8│ pyrieht │ unittest│ gunicorn│
    │ Vim     │ pylint  │ yapf    │         │ nose2   │ uwsgi   │
    └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
         ▲                                                      │
         │                                                      ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                    PRE-COMMIT HOOKS                         │
    │     Automatise tout le pipeline avant chaque commit        │
    │           Garantit la qualité du code                      │
    └─────────────────────────────────────────────────────────────┘
```

---

## ⚡ Ruff : Le Couteau Suisse Ultra-Rapide

### **La Révolution Ruff : 10+ Outils en 1**

```
                        🚀 RUFF REVOLUTION 🚀
                        
    AVANT RUFF (Stack traditionnelle):
    ┌─────────────────────────────────────────────────────────┐
    │ flake8     → PEP8 compliance + basic linting           │
    │ pylint     → Advanced linting + code smells            │
    │ isort      → Import organization                       │
    │ black      → Code formatting                           │
    │ bandit     → Security vulnerabilities                  │
    │ mypy       → Type checking                             │
    │ autopep8   → Auto PEP8 fixes                          │
    │ pyupgrade  → Syntax modernization                      │
    │ autoflake  → Remove unused imports                     │
    │ pycodestyle→ Style guide enforcement                   │
    │                                                         │
    │ = 10 outils, 10 configs, lenteur 🐌                   │
    └─────────────────────────────────────────────────────────┘
                                │
                                ▼
    AVEC RUFF (Solution unifiée):
    ┌─────────────────────────────────────────────────────────┐
    │                    🦀 RUFF 🦀                          │
    │                                                         │
    │ ✅ Linting (remplace flake8, pylint)                   │
    │ ✅ Import sorting (remplace isort)                      │
    │ ✅ Code formatting (complément black)                   │
    │ ✅ Auto-fixes                                           │
    │ ✅ 10-100x plus rapide (Rust)                          │
    │ ✅ Configuration unique                                 │
    │ ✅ Compatible avec presque tout                         │
    │                                                         │
    │ = 1 outil, 1 config, vitesse éclair ⚡                │
    └─────────────────────────────────────────────────────────┘
```

### **Performance Benchmark : Ruff vs Others**

```
                    ⏱️ SPEED COMPARISON ⏱️
                    
    Projet: 100,000 lignes de Python
    
    pylint    ████████████████████████████████████████  45s
    flake8    ████████████████████████████████████      38s
    black     █████████████████████                     22s
    isort     ████████████████                          18s
    
    ruff      ██  1.2s  ⚡ (30-40x plus rapide!)
    
    ┌─────────────────────────────────────────────────────────┐
    │                 POURQUOI SI RAPIDE?                     │
    │                                                         │
    │ 🦀 Écrit en Rust (langage système)                     │
    │ ⚡ Parallélisme natif                                   │
    │ 🧠 Algorithmes optimisés                               │
    │ 💾 Gestion mémoire efficace                            │
    │ 🔧 Cache intelligent                                    │
    └─────────────────────────────────────────────────────────┘
```

### **Installation et Configuration Ruff**

```bash
# 📥 INSTALLATION
pip install ruff

# 🔍 VÉRIFICATION
ruff --version
# ruff 0.1.15

# 🧪 TEST RAPIDE sur votre code
ruff check .              # Lint tout le projet
ruff check --fix .        # Auto-fix les problèmes
ruff format .             # Format le code
```

### **Configuration Ruff (pyproject.toml)**

```toml
[tool.ruff]
# 🎯 CONFIGURATION GÉNÉRALE
target-version = "py39"
line-length = 88
indent-width = 4

# 📁 FICHIERS À ANALYSER
include = ["*.py", "*.pyi", "**/pyproject.toml"]
exclude = [
    ".git",
    ".mypy_cache", 
    ".ruff_cache",
    "venv",
    "__pycache__",
    "build",
    "dist",
]

# 🔍 RÈGLES À APPLIQUER
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings  
    "F",   # pyflakes
    "I",   # isort
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "YTT", # flake8-2020
    "S",   # bandit (security)
    "BLE", # flake8-blind-except
    "FBT", # flake8-boolean-trap
    "B",   # flake8-bugbear
    "A",   # flake8-builtins
    "COM", # flake8-commas
    "C4",  # flake8-comprehensions
    "DTZ", # flake8-datetimez
    "T10", # flake8-debugger
    "EM",  # flake8-errmsg
    "EXE", # flake8-executable
    "ISC", # flake8-implicit-str-concat
    "ICN", # flake8-import-conventions
    "G",   # flake8-logging-format
    "INP", # flake8-no-pep420
    "PIE", # flake8-pie
    "T20", # flake8-print
    "PYI", # flake8-pyi
    "PT",  # flake8-pytest-style
    "Q",   # flake8-quotes
    "RSE", # flake8-raise
    "RET", # flake8-return
    "SLF", # flake8-self
    "SIM", # flake8-simplify
    "TID", # flake8-tidy-imports
    "TCH", # flake8-type-checking
    "ARG", # flake8-unused-arguments
    "PTH", # flake8-use-pathlib
    "ERA", # eradicate
    "PD",  # pandas-vet
    "PGH", # pygrep-hooks
    "PL",  # pylint
    "TRY", # tryceratops
    "NPY", # numpy
    "RUF", # ruff-specific
]

# ❌ RÈGLES À IGNORER 
ignore = [
    "S101",  # assert-used
    "S603",  # subprocess-without-shell-equals-true
    "S607",  # start-process-with-partial-path
    "E501",  # line-too-long (black gère ça)
    "W191",  # tab-indentation (black gère ça)
    "E111",  # indentation-not-multiple-of-four (black gère ça)
    "E114",  # indentation-not-multiple-of-four-comment (black gère ça)
    "E117",  # over-indented (black gère ça)
    "D206",  # indent-with-spaces (black gère ça)
    "D300",  # triple-single-quotes (black gère ça)
    "Q000",  # bad-quotes-inline-string (black gère ça)
    "Q001",  # bad-quotes-multiline-string (black gère ça)
    "Q002",  # bad-quotes-docstring (black gère ça)
    "Q003",  # avoidable-escaped-quote (black gère ça)
    "COM812", # trailing-comma-missing (black gère ça)
    "COM819", # trailing-comma-prohibited (black gère ça)
    "ISC001", # single-line-implicit-string-concatenation (black gère ça)
    "ISC002", # multi-line-implicit-string-concatenation (black gère ça)
]

# ✅ AUTO-FIXES AUTORISÉS
fixable = ["ALL"]
unfixable = []

# 📊 CONFIGURATION SPÉCIFIQUE
[tool.ruff.isort]
known-first-party = ["mon_projet"]
known-third-party = ["requests", "pydantic"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]

[tool.ruff.mccabe]
max-complexity = 10

[tool.ruff.pep8-naming]
classmethod-decorators = ["classmethod", "pydantic.validator"]

[tool.ruff.flake8-quotes]
inline-quotes = "double"
multiline-quotes = "double"
docstring-quotes = "double"

[tool.ruff.pylint]
max-args = 5
max-branches = 12
max-returns = 6
max-statements = 50

# 🧪 CONFIG PAR DOSSIER
[tool.ruff.per-file-ignores]
"tests/*" = ["S101", "PLR2004", "S105", "S106"] 
"__init__.py" = ["F401"]  # unused-import
"migrations/*" = ["E501"] # line-too-long OK dans migrations
```

### **Ruff Workflows Pratiques**

```bash
# 🔍 ANALYSE ET DIAGNOSTIC
ruff check .                          # Analyse complète
ruff check --output-format=json .     # Output JSON pour CI
ruff check --statistics .             # Statistiques par règle
ruff check --show-fixes .             # Montre les fixes possibles

# 🔧 AUTO-FIXES
ruff check --fix .                    # Fix automatique
ruff check --fix --show-fixes .       # Montre + applique fixes
ruff check --unsafe-fixes .           # Inclut fixes "unsafe"

# 🎨 FORMATTING
ruff format .                         # Format tout
ruff format --check .                 # Check sans modifier
ruff format --diff .                  # Montre différences

# 🎯 FILTRAGE SPÉCIFIQUE
ruff check --select E,W .             # Seulement erreurs/warnings
ruff check --ignore E501 .            # Ignore ligne trop longue
ruff check --extend-ignore COM812 .   # Ignore en plus de config

# 📁 FICHIERS SPÉCIFIQUES
ruff check src/                       # Dossier spécifique
ruff check train.py                   # Fichier spécifique
ruff check *.py                       # Pattern

# 🚀 COMBO PUISSANT
ruff check --fix . && ruff format .   # Lint + format d'un coup
```

---

## 🎨 Black : Le Formateur de Référence

### **Black Philosophy : "Any Color You Like, As Long As It's Black"**

```
                        🎨 BLACK PHILOSOPHY 🎨
                        
    PROBLÈME:                           SOLUTION BLACK:
    ┌─────────────────────┐            ┌─────────────────────┐
    │ Code Style Wars:    │            │ Zero Configuration: │
    │                     │            │                     │
    │ • 2 vs 4 spaces?    │     ──►    │ ✅ 4 spaces         │
    │ • 79 vs 88 chars?   │            │ ✅ 88 characters    │
    │ • Quotes ' vs "?    │            │ ✅ Double quotes    │
    │ • Trailing commas?  │            │ ✅ Always trailing  │
    │ • Line breaks?      │            │ ✅ Consistent rules │
    │                     │            │                     │
    │ = Débats infinis    │            │ = Plus de débats    │
    │   sur le style      │            │   focus sur code    │
    └─────────────────────┘            └─────────────────────┘
```

### **Black en Action : Avant/Après**

```python
# ❌ AVANT: Code inconsistant
def my_func(x,y,z):
    result={'key1':x*2,'key2':y*3,'key3':z*4}
    return result

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
if len(my_list)>10 and isinstance(my_list,list):
    print("Long list detected")

# ✅ APRÈS BLACK: Code consistent
def my_func(x, y, z):
    result = {"key1": x * 2, "key2": y * 3, "key3": z * 4}
    return result


my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
]
if len(my_list) > 10 and isinstance(my_list, list):
    print("Long list detected")
```

### **Installation et Usage Black**

```bash
# 📥 INSTALLATION
pip install black

# 🎨 FORMATTING BASIQUE
black .                               # Format tout le projet
black mon_fichier.py                  # Format un fichier
black --check .                       # Check sans modifier
black --diff .                        # Montre différences

# ⚙️ OPTIONS AVANCÉES
black --line-length 100 .            # Longueur ligne custom
black --target-version py39 .         # Version Python target
black --skip-string-normalization .   # Garde quotes originales
black --fast .                        # Mode rapide (skip AST safety)

# 📁 EXCLUSIONS
black --exclude "/(migrations|venv)/" .
black --force-exclude "legacy_code.py" .
```

### **Configuration Black**

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  # Directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''

# 🔧 OPTIONS AVANCÉES
skip-string-normalization = false
skip-magic-trailing-comma = false
experimental-string-processing = false

# 📝 OPTIONS PREVIEW (experimental)
preview = false
```

---

## 🔍 MyPy : Type Checking Intelligent

### **Type Checking : Pourquoi C'est Important**

```python
                    🐛 BUG SANS TYPE HINTS 🐛
                    
def calculate_discount(price, discount):
    """Calculate discounted price"""
    return price * (1 - discount)

# Utilisation "normale":
result = calculate_discount(100, 0.2)     # ✅ 80.0

# Erreurs subtiles:
result = calculate_discount("100", 0.2)   # ❌ "100100100..." 
result = calculate_discount(100, "20%")   # ❌ TypeError
result = calculate_discount(100, 20)      # ❌ -1900 (20 au lieu de 0.20)

                    🛡️ AVEC TYPE HINTS 🛡️
                    
def calculate_discount(price: float, discount: float) -> float:
    """Calculate discounted price"""
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)

# MyPy détecte ces erreurs AVANT l'exécution:
result = calculate_discount("100", 0.2)   # ❌ error: Arg 1 has type "str"; expected "float"
result = calculate_discount(100, "20%")   # ❌ error: Arg 2 has type "str"; expected "float"
result = calculate_discount(100, 20)      # ⚠️  error: Arg 2 has type "int" > 1.0
```

### **MyPy Installation et Configuration**

```bash
# 📥 INSTALLATION
pip install mypy

# 🔍 TYPE CHECKING BASIQUE
mypy .                                # Analyse tout
mypy mon_fichier.py                   # Analyse un fichier
mypy --strict .                       # Mode strict
mypy --ignore-missing-imports .       # Ignore imports externes

# 📊 RAPPORTS
mypy --html-report rapport/ .         # Rapport HTML
mypy --txt-report rapport.txt .       # Rapport texte
mypy --junit-xml rapport.xml .        # Format JUnit pour CI

# 🔧 OPTIONS AVANCÉES
mypy --show-error-codes .             # Montre codes erreur
mypy --show-column-numbers .          # Colonnes dans erreurs
mypy --pretty .                       # Output coloré
```

### **Configuration MyPy Complète**

```toml
[tool.mypy]
# 🎯 CONFIGURATION GÉNÉRALE  
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_optional = true
no_implicit_optional = true

# 🔍 VÉRIFICATIONS STRICTES
check_untyped_defs = true
disallow_any_unimported = true
disallow_any_expr = false  # Trop strict pour débuter
disallow_any_decorated = false
disallow_any_explicit = false
disallow_any_generics = true
disallow_subclassing_any = true
disallow_untyped_calls = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
disallow_untyped_decorators = true

# 🚫 ERREURS ET WARNINGS
no_implicit_reexport = true
strict_equality = true
extra_checks = true
local_partial_types = true

# 📦 PACKAGES EXTERNES
ignore_missing_imports = false  # Plus strict
namespace_packages = true

# 📁 EXCLUSIONS SPÉCIFIQUES
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
ignore_errors = true

[[tool.mypy.overrides]]  
module = "migrations.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = [
    "requests.*",
    "pandas.*",
    "numpy.*",
]
ignore_missing_imports = true  # Si pas de stubs disponibles

# 🔧 PLUGINS SPÉCIALISÉS
plugins = [
    "pydantic.mypy",
    "sqlalchemy.ext.mypy.plugin",
]

# 📊 REPORTING
show_error_context = true
show_column_numbers = true
show_error_codes = true
color_output = true
error_summary = true
```

---

## 🧪 Pytest : Framework de Tests Moderne

### **Pytest vs Unittest : La Révolution Testing**

```python
                   🧪 UNITTEST VS PYTEST 🧪
                   
# ❌ UNITTEST (verbeux, complexe):
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

# ✅ PYTEST (simple, puissant):
def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# C'est tout! Plus simple, plus lisible ✨
```

### **Pytest Features Avancées**

```python
# 🏭 FIXTURES - Setup/Teardown intelligent
import pytest

@pytest.fixture
def calculator():
    """Fournit une instance Calculator pour les tests"""
    calc = Calculator()
    yield calc  # Le test s'exécute ici
    calc.cleanup()  # Nettoyage après le test

@pytest.fixture(scope="session")
def database_connection():
    """Connexion DB partagée pour tous les tests"""
    conn = create_connection()
    yield conn
    conn.close()

def test_with_fixture(calculator):
    # calculator est automatiquement injecté!
    assert calculator.add(1, 1) == 2

# 🎯 PARAMETERIZED TESTS - Tests multiples
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_addition_multiple(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

# 🏷️ MARKERS - Catégorisation des tests
@pytest.mark.slow
def test_heavy_computation():
    # Test qui prend du temps
    result = heavy_function()
    assert result.is_valid()

@pytest.mark.integration
def test_api_endpoint():
    # Test d'intégration
    response = requests.get("http://api.example.com/health")
    assert response.status_code == 200

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 9), reason="Requires Python 3.9+")
def test_modern_feature():
    pass

# ⚠️ EXPECTED FAILURES
@pytest.mark.xfail
def test_known_bug():
    # Test qui échoue pour l'instant, mais c'est attendu
    assert buggy_function() == "correct_result"
```

### **Configuration Pytest**

```toml
[tool.pytest.ini_options]
# 📁 DISCOVERY
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

# 🎯 OPTIONS D'EXÉCUTION
minversion = "7.0"
addopts = [
    "--strict-markers",
    "--strict-config", 
    "--verbose",
    "--tb=short",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html:htmlcov",
    "--cov-report=xml",
    "--cov-fail-under=80",
]

# 🏷️ MARKERS PERSONNALISÉS
markers = [
    "slow: marks tests as slow (may take > 1s)",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
    "api: marks tests that call external APIs",
    "db: marks tests that require database",
    "auth: marks tests related to authentication",
]

# 🔍 FILTRES
filterwarnings = [
    "error",
    "ignore::UserWarning",
    "ignore::DeprecationWarning:django.*",
]

# 🧪 CONFIGURATION ASYNC
asyncio_mode = "auto"

# 📊 LOGGING
log_cli = true
log_cli_level = "INFO"
log_cli_format = "%(asctime)s [%(levelname)8s] %(name)s: %(message)s"
log_cli_date_format = "%Y-%m-%d %H:%M:%S"
```

### **Pytest Workflows Avancés**

```bash
# 🧪 EXÉCUTION BASIQUE
pytest                                # Tous les tests
pytest tests/                         # Dossier spécifique
pytest tests/test_auth.py             # Fichier spécifique
pytest tests/test_auth.py::test_login # Test spécifique

# 🏷️ EXÉCUTION PAR MARKERS
pytest -m "not slow"                 # Exclut tests lents
pytest -m "integration"              # Seulement tests intégration
pytest -m "unit and not db"          # Unit tests sans DB

# 📊 RAPPORTS ET OUTPUTS
pytest --cov=src --cov-report=html   # Coverage HTML
pytest --junitxml=results.xml        # Format JUnit pour CI
pytest --html=report.html            # Rapport HTML avec pytest-html

# ⚡ PERFORMANCE
pytest -x                            # Stop au premier échec
pytest --maxfail=3                   # Stop après 3 échecs
pytest -n auto                       # Parallélisme (pytest-xdist)
pytest --durations=10                # 10 tests les plus lents

# 🔍 DEBUGGING
pytest --pdb                         # Drop en debugger sur échec
pytest --capture=no                  # Pas de capture output
pytest -s                            # Même chose, plus court
pytest -vv                           # Ultra verbose

# 🎯 FILTRAGE AVANCÉ
pytest -k "test_user"                # Tests avec "user" dans le nom
pytest -k "not slow"                 # Exclut tests avec "slow"
pytest --collect-only               # Juste lister, pas exécuter

# 🔄 RE-EXECUTION SMARTES
pytest --lf                          # Seulement failed tests
pytest --ff                          # Failed first, puis les autres
pytest --cache-show                  # Montre cache pytest
```

---

## 🪝 Pre-commit : Automatisation de la Qualité

### **Pre-commit Philosophy : "Never Commit Broken Code"**

```
                    🪝 PRE-COMMIT WORKFLOW 🪝
                    
    SANS PRE-COMMIT:
    ┌─────────────────────────────────────────────────────────┐
    │ Code → Commit → Push → CI Fails → Fix → Commit → Push  │
    │   │              │        │               │             │
    │   ▼              ▼        ▼               ▼             │
    │ 😊            😔😔😔    😡😡😡          😅          │
    │                                                         │
    │ = Cycle frustrant, CI lent, historique sale            │
    └─────────────────────────────────────────────────────────┘
                                │
                                ▼
    AVEC PRE-COMMIT:
    ┌─────────────────────────────────────────────────────────┐
    │     Code → [Auto-check] → Clean Commit → Push → ✅     │
    │       │           │             │                       │
    │       ▼           ▼             ▼                       │
    │     😊         😊             😊                     │
    │                                                         │
    │ = Qualité garantie, CI rapide, équipe heureuse         │
    └─────────────────────────────────────────────────────────┘
```

### **Installation et Setup Pre-commit**

```bash
# 📥 INSTALLATION
pip install pre-commit

# 🔧 INITIALISATION PROJET
cd mon_projet/
pre-commit install                    # Active hooks Git
pre-commit install --hook-type commit-msg  # Messages de commit

# 🧪 TEST MANUEL
pre-commit run --all-files            # Teste sur tous les fichiers
pre-commit run ruff                   # Teste hook spécifique
pre-commit run --files file1.py file2.py  # Fichiers spécifiques

# 🔄 MAINTENANCE
pre-commit autoupdate                 # Met à jour versions hooks
pre-commit clean                      # Nettoie cache
pre-commit uninstall                  # Désactive hooks
```

### **Configuration Pre-commit Complète**

```yaml
# .pre-commit-config.yaml
repos:
  # 🔧 RUFF - Linting et formatting intégré
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.15
    hooks:
      - id: ruff
        name: ruff-linter
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format
        name: ruff-formatter

  # 🎨 BLACK - Code formatting (si pas utilisation ruff format)
  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        language_version: python3
        args: [--line-length=88]

  # 📊 MYPY - Type checking
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-PyYAML]
        args: [--strict, --ignore-missing-imports]

  # 📋 PRE-COMMIT HOOKS STANDARDS
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace        # Supprime espaces en fin
      - id: end-of-file-fixer         # Assure newline finale
      - id: check-yaml                # Valide YAML
      - id: check-json                # Valide JSON
      - id: check-toml                # Valide TOML
      - id: check-merge-conflict      # Détecte conflits Git
      - id: check-added-large-files   # Empêche gros fichiers
      - id: check-case-conflict       # Conflit de casse fichiers
      - id: check-docstring-first     # Docstring en première
      - id: debug-statements          # Détecte print(), pdb()
      - id: name-tests-test           # Convention noms tests
      - id: requirements-txt-fixer    # Trie requirements.txt

  # 🔒 SÉCURITÉ - Bandit pour vulnérabilités
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-r, -f, json, -o, bandit-report.json]
        exclude: tests/

  # 📝 COMMITS CONVENTIONNELS
  - repo: https://github.com/compilerla/conventional-pre-commit
    rev: v3.0.0
    hooks:
      - id: conventional-pre-commit
        stages: [commit-msg]

  # 🧪 TESTS RAPIDES (optionnel)
  - repo: local
    hooks:
      - id: pytest-fast
        name: pytest-fast
        entry: pytest
        language: system
        types: [python]
        args: [--maxfail=1, --tb=short, -q]
        stages: [commit]

  # 🐳 DOCKERFILE LINTING
  - repo: https://github.com/hadolint/hadolint
    rev: v2.12.1-beta
    hooks:
      - id: hadolint
        args: [--ignore, DL3008, --ignore, DL3009]

  # 📚 DOCUMENTATION
  - repo: https://github.com/myint/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]

# ⚙️ CONFIGURATION GÉNÉRALE
default_stages: [commit]
fail_fast: false  # Continue même si un hook échoue
minimum_pre_commit_version: 3.0.0

# 📁 EXCLUSIONS GLOBALES
exclude: |
    (?x)(
        migrations/|
        \.min\.js$|
        \.min\.css$|
        node_modules/|
        \.venv/|
        build/|
        dist/
    )

ci:
  autofix_commit_msg: |
      [pre-commit.ci] auto fixes from pre-commit hooks

      for more information, see https://pre-commit.ci
  autofix_prs: true
  autoupdate_branch: ''
  autoupdate_commit_msg: '[pre-commit.ci] pre-commit autoupdate'
  autoupdate_schedule: weekly
  skip: []
  submodules: false
```

### **Gitflow avec Pre-commit**

```bash
# 🔄 WORKFLOW QUOTIDIEN AVEC PRE-COMMIT

# 1. Développement normal
echo "def hello_world():\n    print('Hello, World!')" > hello.py

# 2. Commit (pre-commit se déclenche automatiquement)
git add hello.py
git commit -m "feat: add hello world function"

# ⚡ Pre-commit s'exécute:
# - Ruff vérifie et corrige le code
# - Black formate le code  
# - MyPy vérifie les types
# - Tests rapides s'exécutent
# - Vérifications générales

# 3. Si tout est OK:
[main 1a2b3c4] feat: add hello world function
 1 file changed, 2 insertions(+)

# 4. Si problèmes détectés:
# Pre-commit corrige automatiquement puis s'arrête
# Vous devez re-stagez les corrections et re-commiter

git add hello.py  # Ajouter les corrections
git commit -m "feat: add hello world function"  # Re-commit
```

---

## 🔄 CI/CD Integration : Automatisation Complète

### **GitHub Actions Workflow Python**

```yaml
# .github/workflows/python-ci.yml
name: Python CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11, 3.12]
    
    steps:
      - uses: actions/checkout@v4
      
      # 🐍 Setup Python avec cache
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
      
      # ⚡ Install UV pour performance
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      
      # 📦 Install dependencies
      - name: Install dependencies
        run: |
          uv pip install --system -r requirements.txt
          uv pip install --system -r requirements-dev.txt
      
      # 🔍 Code Quality Checks
      - name: Lint with Ruff
        run: ruff check .
      
      - name: Format check with Ruff
        run: ruff format --check .
      
      - name: Type check with MyPy
        run: mypy .
      
      # 🧪 Tests avec coverage
      - name: Test with pytest
        run: |
          pytest --cov=src --cov-report=xml --cov-report=html
      
      # 📊 Upload coverage
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
      
      # 🔒 Security check
      - name: Security check with Bandit
        run: bandit -r src/

  build:
    needs: quality
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.11
      
      - name: Build package
        run: |
          pip install build
          python -m build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: python-package
          path: dist/
```

---

## 💡 Récapitulatif et Bonnes Pratiques

### **Stack Recommandée 2024**

```
                    🏆 STACK MODERNE RECOMMANDÉE 🏆
                    
    DÉVELOPPEMENT LOCAL:
    ┌─────────────────────────────────────────────────────────┐
    │ 🔧 ruff          → Linting + Import sorting + Fixes    │
    │ 🎨 black         → Code formatting (ou ruff format)    │
    │ 📊 mypy          → Type checking                       │
    │ 🧪 pytest       → Testing framework                    │
    │ 📦 poetry        → Package management                  │
    │ 🪝 pre-commit    → Git hooks automation               │
    │ 💻 VS Code       → IDE avec extensions Python         │
    └─────────────────────────────────────────────────────────┘
    
    CI/CD:
    ┌─────────────────────────────────────────────────────────┐
    │ ⚡ uv pip          → Installation ultra-rapide          │
    │ 🔄 GitHub Actions → Pipeline automatisé                │
    │ 📈 codecov        → Coverage reporting                 │
    │ 🔒 bandit         → Security scanning                  │
    │ 🐳 Docker         → Containerisation                   │
    └─────────────────────────────────────────────────────────┘
```

### **Configuration Workspace VS Code**

```json
// .vscode/settings.json
{
    // 🐍 Python settings
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.terminal.activateEnvironment": true,
    
    // 🔧 Ruff integration
    "pylint.enabled": false,
    "ruff.enable": true,
    "ruff.organizeImports": true,
    "ruff.fixAll": true,
    
    // 🎨 Formatting
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports.ruff": true,
        "source.fixAll.ruff": true
    },
    
    // 📊 Type checking
    "python.analysis.typeCheckingMode": "strict",
    "python.analysis.autoImportCompletions": true,
    
    // 🧪 Testing
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": ["tests"],
    
    // 📏 Editor
    "editor.rulers": [88],
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
}
```

### **Troubleshooting Commun**

```bash
# 🔧 RÉSOLUTION PROBLÈMES FRÉQUENTS

# Ruff et Black en conflit:
# Solution: Configurer ruff pour être compatible
[tool.ruff]
format.quote-style = "double"  # Comme Black

# MyPy ignore imports:
# Solution: Installer type stubs
pip install types-requests types-PyYAML

# Pre-commit lent:
# Solution: Cache et parallélisme
export PRE_COMMIT_COLOR=always
pre-commit run -j 4  # Parallélisme

# VS Code ne détecte pas l'environnement:
# Solution: Spécifier le bon Python
Ctrl+Shift+P → "Python: Select Interpreter" → .venv/bin/python
```

---

**🎯 Prêt pour les frameworks de test avancés ?**

**👉 Passez à : [testing-frameworks.md](testing-frameworks.md)**

---

*"Les outils ne font pas le développeur, mais de bons outils font de meilleurs développeurs !"* 🔧✨