# ♻️ EcoSort – Smart Recycling Awareness

**Small Steps, Cleaner Planet.**

EcoSort is a simple recycling awareness website built with **Python** and **Streamlit**.
It was made as an **Environmental Studies (EVS)** college project to spread awareness
about recycling, teach people how to separate waste, and explain the correct way to
dispose of everyday household waste.

Everything runs locally. There are no API keys, no database, no machine learning and
no paid services — all the waste information is stored in plain Python dictionaries
and lists inside `app.py`.

---

## 📁 Project Structure

```
EcoSort/
├── app.py            # The complete website (all pages and data)
├── requirements.txt  # Python dependencies (only Streamlit)
└── README.md         # This file
```

---

## 🚀 How to Run the Project

### 1. Install Python
Install Python 3.9 or newer from <https://www.python.org/downloads/> and make sure
`python` and `pip` work in your terminal.

### 2. Open the project folder
```bash
cd EcoSort
```

### 3. (Optional but recommended) Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install the dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the website
```bash
streamlit run app.py
```

Streamlit will open the website automatically in your browser at
**http://localhost:8501**. If it does not open by itself, copy that address into
your browser.

To stop the server, press `Ctrl + C` in the terminal.

---

## 🧭 Website Sections

| Section | What it does |
| --- | --- |
| **🏠 Home** | Introduction to EcoSort, why waste management matters, three awareness facts and quick links to every section. |
| **🗂️ Waste Categories** | Explains wet waste, dry waste and hazardous waste with examples, the correct bin and the disposal method. |
| **🔍 Waste Identifier** | Pick any common household item from a dropdown and see its category, disposal method and an explanation. |
| **💡 Recycling Tips** | Eight practical tips shown as simple cards. |
| **🧠 Recycling Quiz** | Five multiple-choice questions, automatic scoring, answer review and an encouraging message. |

Use the green sidebar to move between sections.

---

## 🛠️ Technology Used

- **Python 3** – the programming language.
- **Streamlit** – turns the Python script into an interactive website.
- **Python dictionaries and lists** – store all the waste data (no database needed).

---

## ➕ How to Add New Waste Items

Open `app.py` and find the `WASTE_ITEMS` dictionary. Add a new entry in the same format:

```python
"Old clothes": {
    "category": "Dry Waste",
    "disposal": "Give wearable clothes to a donation centre; keep torn cloth for recycling.",
    "explanation": "Textiles can be reused or converted into new fabric, so they should not go into the wet bin.",
},
```

Save the file and refresh the browser — the new item appears in the Waste Identifier
dropdown automatically.

---

## 🩺 Troubleshooting

| Problem | Solution |
| --- | --- |
| `streamlit: command not found` | Run `pip install -r requirements.txt` again, or use `python -m streamlit run app.py`. |
| Port 8501 is already in use | Run `streamlit run app.py --server.port 8502`. |
| The page looks unstyled | Refresh the browser with `Ctrl + F5`. |

---

## 🎓 Academic Note

This project demonstrates:

1. Basic Python data structures (dictionaries and lists).
2. Building an interactive multi-page web app with Streamlit.
3. Waste segregation and recycling awareness, as covered in Environmental Studies.

**EcoSort ♻️ — Small Steps, Cleaner Planet.**
