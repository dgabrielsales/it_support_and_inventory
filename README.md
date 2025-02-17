<h1 align="center"> 🛠️ IT Solution Support & Inventory 📦</h1>

<p align="center">
    <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square">
    <img src="https://img.shields.io/github/languages/count/dgabrielsales/it_support_and_inventory">
</p>

📌 **IT Solution Support & Inventory** é um sistema de gerenciamento de **inventário de TI**.  
Ele permite **registrar equipamentos**, **alocar ativos a setores** e acompanhar movimentações.

---


## 📖 **Base de Conhecimento**
📌 A **base de conhecimento** é uma funcionalidade que permite cadastrar e consultar **problemas e soluções** passo a passo.  


## 🚀 **Funcionalidades**
✔ Cadastro de equipamentos e setores 📋  
✔ Movimentação de ativos entre setores 🔄    
✔ Dashboard para visualização dos dados 📊  
✔ Base de conhecimento integrada 📖  

---

## 📂 **Tecnologias Usadas**
✅ **Back-End:** Flask + SQLAlchemy  
✅ **Banco de Dados:** SQLite (ou MySQL, se configurado)  
✅ **Front-End:** HTML + Bootstrap  
✅ **Gerenciamento de Dependências:** `pip` + `requirements.txt`  

---

## 📖 **Base de Conhecimento**
A **base de conhecimento** é integrada ao projeto para facilitar a compreensão e a manutenção do sistema.  

### 📌 **1. O que é o inventário?**
- O sistema gerencia **ativos de TI**, como **computadores, impressoras e servidores**.  
- Cada equipamento pode ser **alocado a um setor** e **realocar-se quando necessário**.  

### 📌 **2. Como os dados são armazenados?**
O banco de dados usa **SQLite**.  

#### **Tabelas principais:**
| Tabela        | Função |
|--------------|---------------------------|
| `equipamentos` | Cadastro dos equipamentos de TI |
| `setores` | Locais onde os equipamentos estão alocados |
| `alocacoes` | Histórico de movimentações dos equipamentos |

---

## 🛠 **Como Executar o Projeto**
### 1️⃣ **Clone o Repositório**
```bash
git clone https://github.com/dgabrielsales/it_support_and_inventory.git
cd it_support_and_inventory ```
```

```bash
##2️⃣ **Crie um Ambiente Virtual**
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

```bash
##3️⃣ Instale as Dependências
pip install -r requirements.txt
```

```bash
5️⃣ Inicie o Servidor
python app.py
```