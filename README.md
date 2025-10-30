# 🌍 Unit Converter – US to EU

A simple **Flask web application** that converts common **US and EU measurement units** such as kilograms, pounds, meters, feet, Celsius, and Fahrenheit.

---

## 🚀 Features

- Convert between:
  - **Kilograms ↔ Pounds**
  - **Meters ↔ Feet**
  - **Celsius ↔ Fahrenheit**
- Simple and clean web interface using **HTML + CSS**
- Built with **Flask (Python)** for handling conversions on the backend
- Error handling for invalid inputs and unsupported conversions

---

## 🧮 Example Conversions

| From | To | Example Input | Example Output |
|------|----|----------------|----------------|
| kg | lbs | 10 | 22.05 lbs |
| lbs | kg | 50 | 22.68 kg |
| m | ft | 3 | 9.84 ft |
| °C | °F | 25 | 82.40 °F |

---

## 🧠 How It Works

1. The user enters a number and selects the **unit to convert from** and **unit to convert to**.
2. Flask receives the input through a POST request.
3. The app performs the correct mathematical conversion:
   - `kg ↔ lbs` → uses factor 2.205  
   - `m ↔ ft` → uses factor 3.2808399  
   - `°C ↔ °F` → uses simplified temperature conversion
4. The converted value is displayed on the web page.

---

## 🖥️ Tech Stack

- **Backend:** Python 3 + Flask  
- **Frontend:** HTML, Jinja2 (Flask templating), CSS  
- **Port:** Runs on `127.0.0.1:8080`

---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ymat-jan/Converter-units.git
   cd unit-converter-flask
