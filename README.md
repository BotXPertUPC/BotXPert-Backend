# 🤖 BotXPert - Backend

**BotXPert** és un projecte per automatitzar la creació de bots per a Whatsapp. Aquest repositori conté la infraestructura per executar, desenvolupar i provar el sistema.

---

## 👥 Membres de l’equip

- Anyer Moreno  
- Andreu Sabater  
- Maria Salvat  
- Arnau Ventura  

---

## 🔧 Requisits

- Python 3.12  
- Django 5.1.7  
- Git  

---

## 🚀 Clonar el repositori

### 🔐 Configurar accés SSH (només una vegada)

1. Obre una terminal i executa:

```bash
ssh-keygen -t ed25519 -C "tu@email.com"
```
2. Prem Enter a totes les preguntes.

3. Mostra la clau pública:

**Windows:**
```
type $env:USERPROFILE\.ssh\id_ed25519.pub
```
**Linux/macOS:**
```
cat ~/.ssh/id_ed25519.pub 
```
4. Copia tot el contingut (comença per `ssh-ed25519...`) i afegeix-lo a [https://github.com/settings/ssh](https://github.com/settings/ssh)

5. Torna a GitHub, copia l’enllaç **SSH** del repositori i clona’l a PyCharm o amb:
```
git clone git@github.com:BotXPertUPC/BotXPert-Backend.git
```
⚠️ Si et demana:
```
Are you sure you want to continue connecting?
```
Respon **yes**.

---

## 🧱 Preparar l'entorn virtual

### 🌱 Crear l’entorn (només una vegada)
```
python -m venv .venv
```
### ▶️ Activar l'entorn virtual

**Linux/macOS:**
```
source .venv/bin/activate
```
**Windows:**
```
.venv\Scripts\Activate
```
(Comprova que al principi de la línia de terminal aparegui `(.venv)`)

---

## 📦 Instal·lar dependències

Després d’activar el `.venv`:
```
pip install -r requirements.txt
```
(Repeteix-ho si el fitxer canvia)

---

## 🧪 Executar el projecte localment
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Accedeix a: http://127.0.0.1:8000

🛑 Prem `Ctrl + C` per aturar el servidor quan vulguis.

---

## ✨ Crear noves aplicacions (apps)
```python manage.py startapp nom_app```

Després, afegeix-la a `INSTALLED_APPS` dins `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'nom_app',  # Afegeix la teva nova aplicació aquí
]
```
## 🚀 Desplegament en producció

Per desplegar el projecte al servidor de producció:

1. Connecta’t per SSH a la màquina virtual:
```bash
ssh root@187.33.149.121
```
2. Executa el script de desplegament:
```bash
./start.sh
```
Aquest script actualitza el codi (git pull) i arrenca el contenidor de Docker en segon pla.

### 🛑 Aturar el backend
```bash
./stop.sh
```