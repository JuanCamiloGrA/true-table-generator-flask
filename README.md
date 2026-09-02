# True Table Generator (Flask)

A simple Flask web app to generate truth tables for propositional logic expressions.

## Features

- Generate full truth tables from custom logical expressions
- Supports common operators:
  - Negation: `¬`
  - Conjunction: `∧`
  - Disjunction: `∨`
  - Implication: `→`
  - Biconditional: `↔`
- Clean web interface with quick-insert operator buttons
- Boolean results displayed as `V` (true) and `F` (false)

## Tech Stack

- Python
- Flask
- Jinja2 templates
- HTML/CSS (Bootstrap + custom styles)

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/JuanCamiloGrA/true-table-generator-flask.git
cd true-table-generator-flask
```

### 2) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows (PowerShell)
```

### 3) Install dependencies

```bash
pip install flask
```

### 4) Run the app

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open the home page in your browser.
2. Enter a logical expression (for example: `¬(p∧q)→r`).
3. Click **Generar Tabla de Verdad**.
4. Review the generated truth table.

## Notes

- Variables are inferred automatically from alphabetic characters in the expression.
- Parentheses are supported.
- Invalid expressions may return no table.

## Project Structure

```text
.
├── app.py                  # Flask routes and app entry point
├── logic.py                # Truth table generation logic
├── app.yaml                # Deployment config
├── static/
│   ├── css/styles.css      # UI styles
│   └── js/script.js
└── templates/
    ├── base.html
    └── index.html
```
