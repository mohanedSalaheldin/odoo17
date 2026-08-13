# Odoo 17 ERP Development & Customization Portfolio

[![Odoo Version](https://img.shields.io/badge/Odoo-17.0%20(Community%20%26%20Enterprise)-875A7B?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![JavaScript OWL](https://img.shields.io/badge/Frontend-OWL%202.0%20%2F%20JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://github.com/odoo/owl)
[![License](https://img.shields.io/badge/License-LGPL--3.0-blue?style=for-the-badge)](LICENSE)

> A comprehensive, hands-on repository showcasing custom **Odoo 17 ERP module development**, advanced **ORM & business workflow design**, modern **OWL 2.0 (Odoo Web Library)** frontend components, **QWeb PDF reporting engines**, and security access control architectures.

---

## 📌 Repository Overview

This repository demonstrates practical proficiency in full-stack Odoo 17 development, following official Odoo guidelines and architectural best practices. It covers backend business logic modeling, relational data structuring, transient wizards, automated sequence numbering, automated communication chatter, security access rights, dynamic QWeb reports, and custom interactive JavaScript frontend widgets using Odoo's OWL 2.0 framework.

---

## 🚀 Key Modules & Architecture

The custom addons located in [`projects/myaddons/`](projects/myaddons/) include:

```text
projects/myaddons/
├── 🏥 my_hospital/       # Hospital & Healthcare Management ERP
├── ⚡ owl_dev/           # Modern Odoo Web Library (OWL 2.0) Components & Custom Widgets
├── 📄 qweb_app/          # Advanced QWeb PDF Report Design & Engines
└── 🧪 testapp/           # ORM Deep Dive, Triggers, Constraints & Workflow State Machines
```

---

### 1. 🏥 Hospital Management System (`my_hospital`)

A comprehensive healthcare operational module designed to manage patients, doctors, appointments, medical prescriptions, and clinical history.

#### 🔑 Key Features & Technical Implementations:
- **Model Extension (`res.partner` & `res.users`)**:
  - Inherited `res.partner` to create specialized **Patient** profiles with age computation, appointment history (`One2many`), and dynamic smart button actions.
  - Inherited `res.users` to configure **Doctor** and **Supervisor** roles with specific domains.
- **Appointment Management (`the.appointments`)**:
  - Automated sequence generation (`ir.sequence`) for unique record numbering (`APP0/00001`).
  - Multi-state lifecycle workflow (`Draft` ➔ `Confirm` ➔ `Done` / `Cancelled`) with statusbar visualization.
  - Integration with `mail.thread` and `mail.activity.mixin` for real-time chatter tracking, message followers, and scheduled activities.
  - Relational links to patients, doctors, medical notes, and prescriptions.
- **Prescription & Pharmacy Management (`the.prescription`, `the.medicines`)**:
  - Medical prescription lines linked directly to consultations and medicine catalog.
- **Transient Model Wizard (`the.add.appointments`)**:
  - Interactive popup wizard for rapid appointment scheduling with context-based data pre-filling.
- **Analytics & Advanced Views**:
  - **Tree (List) View**: Clean tabular presentation with filtering and search domains.
  - **Form View**: Responsive layout with header action buttons, statusbar, notebooks, and chatter widget.
  - **Pivot View**: Multi-dimensional pivot table analysis (Appointments by Doctor and State).
  - **Graph View**: Interactive bar charts for appointment metrics.
- **Custom QWeb PDF Reports**:
  - **Patient Medical History Report**: Detailed printable PDF summarizing patient visits and diagnostics.
  - **Prescription Printout**: Formal prescription document generated directly from consultation records.
- **Security & Access Control (RBAC)**:
  - Custom user security groups (`security/security.xml`) and Model Access Control Lists (`ir.model.access.csv`).

---

### 2. ⚡ Modern OWL 2.0 Frontend Development (`owl_dev`)

Showcases the creation of interactive, reactive UI components utilizing **OWL 2.0** (Odoo Web Library), integrated seamlessly with Odoo 17's Web Client architecture.

#### 🔑 Key Components:
- **Custom Range Slider Widget (`rang_widget`)**:
  - Interactive slider field widget for real-time numeric value manipulation.
- **Real-Time Email Validation Widget (`vaild_email_widget`)**:
  - Dynamic client-side input validation widget with instant visual feedback.
- **Interactive To-Do List Application (`todo_list`)**:
  - Full-featured standalone OWL component utilizing reactive state hooks, task filtering, and dynamic DOM manipulation.
- **Standard View Inheritance & Customization (`inheritance_view`)**:
  - Extending core Odoo views (`res.partner` List, Kanban, and Form views) using OWL template patches and custom JavaScript components.
- **Web Assets Management**:
  - Configured bundle registration in `__manifest__.py` under `web.assets_backend` with modular SCSS and XML templates.

---

### 3. 📄 Advanced QWeb Reporting (`qweb_app`)

Demonstrates pixel-perfect document styling and dynamic PDF report generation using Odoo's QWeb engine.

#### 🔑 Key Highlights:
- Custom report actions and dynamic paper formats.
- Advanced QWeb directives (`t-if`, `t-foreach`, `t-set`, `t-esc`, `t-field`).
- Professional styling, table layouts, dynamic data aggregation, headers, and footers.

---

### 4. 🧪 ORM Mastery & Business Logic (`testapp`)

A dedicated module for validating core Odoo ORM mechanics, decorators, validation logic, and order workflows.

#### 🔑 Key Highlights:
- **ORM Decorators**: Practical implementation of `@api.depends`, `@api.onchange`, and `@api.constrains`.
- **Database Constraints**: Multi-field SQL constraints (`_sql_constraints`) and Python exceptions (`ValidationError`).
- **Order Processing Workflow**: Master-detail relationship (`my.order` ➔ `my.order.item`) with conditional domain filters and state automation.

---

## 🛠️ Technology Stack & Skills

| Domain | Technologies / Concepts |
| :--- | :--- |
| **ERP Platform** | Odoo 17.0 (Community & Enterprise) |
| **Backend** | Python 3.10+, Odoo ORM API, Business Logic, Workflows |
| **Frontend** | JavaScript (ES6+), OWL 2.0 (Odoo Web Library), SCSS, XML |
| **Database** | PostgreSQL, SQL Constraints, Query Optimization |
| **Reporting** | QWeb XML Engine, Wkhtmltopdf, Custom Layouts |
| **Architecture** | MVC / ORM, Modular Addons, Mixins (`mail.thread`), Transient Models |
| **Security** | Role-Based Access Control (RBAC), ACLs (`ir.model.access.csv`), Record Rules |
| **Version Control** | Git, GitHub |

---

## 💻 Installation & Local Setup

### 1. Prerequisites
Ensure you have the following installed on your machine:
- **Python 3.10+**
- **PostgreSQL 14+**
- **Wkhtmltopdf** (0.12.5 with patched qt for PDF reporting)

### 2. Clone the Repository
```bash
git clone https://github.com/mohanedSalaheldin/odoo17.git
cd odoo17
```

### 3. Virtual Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Running Odoo with Custom Addons
Start the Odoo server by including the custom addons directory in the `addons-path`:

```bash
python odoo-bin --addons-path=addons,projects/myaddons -d odoo17_db -u my_hospital,owl_dev,qweb_app,testapp
```

Access the instance in your browser at `http://localhost:8069`.

---

## 💼 CV / Resume Highlights

> *Summary points ready for CV, LinkedIn Projects, or Technical Portfolios:*

- **Odoo 17 Custom ERP Development**: Designed and deployed full-lifecycle custom modules with complex relational data models (`One2many`, `Many2one`, `Many2many`), smart buttons, and automated sequences.
- **Modern OWL 2.0 Frontend Engineering**: Built reactive web components, custom form field widgets, and inherited standard Kanban/List views using Odoo's OWL 2.0 JavaScript framework.
- **Business Process Automation**: Implemented state machine workflows, email chatter integration (`mail.thread`, `mail.activity.mixin`), transient wizards, and multi-dimensional Pivot/Graph analytics.
- **Enterprise Reporting & Security**: Engineered pixel-perfect QWeb PDF reports and established robust Role-Based Access Control (RBAC) security groups and record-level rules.

---

## 👨‍💻 Author

**Mohaned Salaheldin**  
*Odoo Developer & Software Engineer*  

- **GitHub**: [@mohanedSalaheldin](https://github.com/mohanedSalaheldin)  
- **Website / Portfolio**: [mohanedsalaheldin.com](https://www.mohanedsalaheldin.com)  

---

## 📄 License
This project is licensed under the [LGPL-3.0 License](LICENSE).
