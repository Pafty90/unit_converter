# Unit Converter 🔄
A simple unit converter built with **Python** and **Django**.  
It allows users to convert between **length, weight, and temperature units** via a clean web interface.

---

## 🚀 Features
- Simple and intuitive web interface.
- Supported unit categories:
  - **Length** → millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
  - **Weight** → milligram, gram, kilogram, ounce, pound.
  - **Temperature** → Celsius, Fahrenheit, Kelvin.

Inspired by [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter).

---

## 📸 Preview
![Preview](https://github.com/user-attachments/assets/cf6839e0-6a40-4a43-950d-6d2fa74d7344)

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pafty90/unit_converter.git
cd unit_converter
```

2. **Create and activate a virtual environment**

    **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    **Linux / macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python manage.py runserver
```

5. **Open in browser**
```bash
http://127.0.0.1:8000/converter/
```

---

## 📂 Project Structure
* `converter` → Django app that contains the core logic for unit conversion.
* `mysite` → Main Django project folder (settings, URLs, configuration).
* `converter/static` → Static files (CSS, JavaScript, images).
* `converter/templates` → HTML files for the conversion pages.

---

## 🛠 Usage
1. Open the app in your browser.

2. Choose a category (Length, Weight, Temperature).

3. Enter a value and select units.

4. Click Convert to get the result instantly.