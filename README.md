# ⚖️ BMI Calculator (Streamlit Web App)

A clean and interactive web application built with Streamlit that calculates Body Mass Index (BMI) based on user height and weight inputs. It automatically classifies the result into standard health categories and provides visual feedback based on the outcome.

---

## 📸 App Screenshots

### 1. Normal Weight Result
<img width="1346" height="967" alt="Screenshot 2026-10-07 225518" src="https://github.com/user-attachments/assets/c11aba51-8f91-4519-8fb1-6a83b13c87b1" />

---

### 2. Overweight / Obese Result

<img width="1096" height="962" alt="Screenshot 2026-10-07 225545" src="https://github.com/user-attachments/assets/15a75878-ad17-41e4-9328-fd4cb4fb8a2b" />
---

### 3. Underweight Result

<img width="1000" height="932" alt="Screenshot 2026-10-07 225626" src="https://github.com/user-attachments/assets/d1b4b3ce-4bf9-4c50-a09d-213e6f9a4dcc" />

---

## 🚀 Key Features

* **Interactive Numerical Inputs:** Enter weight in kilograms (kg) and height in meters (m) with min-value bounds.
* **Instant BMI Score Calculation:** Calculates the precise BMI score rounded to two decimal places.
* **Dynamic Health Classifications:**
  * 🟡 **Underweight:** BMI less than 18.5
  * 🟢 **Normal Weight:** BMI between 18.5 and 24.9 (triggers a balloon celebration screen)
  * 🟡 **Overweight:** BMI between 25.0 and 29.9
  * 🔴 **Obese:** BMI 30.0 or higher
* **Visual Status Indicators:** Color-coded alert boxes (warning, success, error) tailored to each health result.

---

## 🛠️ Project Structure

```text
.
├── app.py
├── README.md
└── screenshots/
    ├── Screenshot_1.png
    ├── Screenshot_2.png
    └── Screenshot_3.png
