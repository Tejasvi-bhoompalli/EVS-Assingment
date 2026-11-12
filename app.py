"""EcoSort - Smart Recycling Awareness
========================================
A simple recycling awareness website built with Python and Streamlit.

This is a beginner-friendly Environmental Studies (EVS) college project.
All the waste information is stored in normal Python dictionaries and lists,
so no database, API key, machine learning or internet connection is needed.

Run the website with:
    streamlit run app.py
"""

import streamlit as st

# ---------------------------------------------------------------------------
# 1. PAGE CONFIGURATION  (must be the first Streamlit command)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="EcoSort - Smart Recycling Awareness",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# 2. COLORFUL PAGE STYLES (clean green environmental theme)
# ---------------------------------------------------------------------------
CSS = """<style>
/* ---------- Base theme ---------- */
.stApp {
    background-color: #f4faf4;
}
.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}
h1, h2, h3, h4 {
    color: #14532d;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}
.stApp p, .stApp li, .stApp label {
    color: #374151;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}

/* ---------- Hero banner on the home page ---------- */
.hero {
    background: linear-gradient(135deg, #14532d 0%, #2e7d32 55%, #4caf50 100%);
    border-radius: 18px;
    padding: 44px 38px;
    color: #ffffff;
    box-shadow: 0 10px 26px rgba(20, 83, 45, 0.20);
    margin-bottom: 28px;
}
.hero .hero-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.40);
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 0.78rem;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: #eaf7ea;
}
.hero h1 {
    color: #ffffff;
    font-size: 3.2rem;
    margin: 14px 0 0 0;
    letter-spacing: 0.5px;
}
.hero .tagline {
    font-size: 1.30rem;
    font-weight: 600;
    color: #c8e6c9;
    margin: 6px 0 18px 0;
}
.hero p.hero-text {
    color: #eaf7ea;
    font-size: 1.02rem;
    line-height: 1.65;
    max-width: 780px;
    margin: 0;
}

/* ---------- Statistics cards ---------- */
.stat-card {
    background: #ffffff;
    border: 1px solid #d7ecdc;
    border-left: 6px solid #2e7d32;
    border-radius: 14px;
    padding: 22px 20px;
    height: 100%;
    box-shadow: 0 4px 14px rgba(20, 83, 45, 0.07);
}
.stat-card .stat-icon {
    font-size: 1.55rem;
}
.stat-card .stat-value {
    font-size: 2.0rem;
    font-weight: 700;
    color: #14532d;
    margin: 4px 0 2px 0;
}
.stat-card .stat-text {
    font-size: 0.93rem;
    line-height: 1.5;
    color: #4b5563;
    margin: 0;
}

/* ---------- Waste category / info cards ---------- */
.eco-card {
    background: #ffffff;
    border: 1px solid #d7ecdc;
    border-top: 5px solid #2e7d32;
    border-radius: 14px;
    padding: 24px 22px;
    height: 100%;
    box-shadow: 0 4px 16px rgba(20, 83, 45, 0.08);
}
.eco-card .card-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 54px;
    height: 54px;
    border-radius: 14px;
    font-size: 1.7rem;
    background: #e8f5e9;
    margin-bottom: 10px;
}
.eco-card .card-title {
    margin: 4px 0 2px 0;
    font-size: 1.28rem;
    color: #14532d;
}
.eco-card .card-sub {
    font-size: 0.88rem;
    color: #6b7280;
    margin: 0 0 14px 0;
}
.eco-card p {
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0 0 10px 0;
}
.eco-card strong {
    color: #14532d;
}
.card-note {
    background: #f1f8f2;
    border-left: 4px solid #66bb6a;
    border-radius: 8px;
    padding: 12px 14px;
    font-size: 0.90rem !important;
    line-height: 1.55;
    color: #374151;
    margin-top: 12px;
}

/* ---------- Waste identifier result ---------- */
.result-badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.92rem;
    margin-bottom: 6px;
}

/* ---------- Tips cards ---------- */
.tip-card {
    background: #ffffff;
    border: 1px solid #d7ecdc;
    border-radius: 14px;
    padding: 20px;
    height: 100%;
    box-shadow: 0 3px 12px rgba(20, 83, 45, 0.06);
    margin-bottom: 16px;
}
.tip-card .tip-icon {
    font-size: 1.6rem;
    display: block;
    margin-bottom: 8px;
}
.tip-card .tip-title {
    font-weight: 700;
    color: #14532d;
    font-size: 1.0rem;
    display: block;
    margin-bottom: 6px;
}
.tip-card .tip-text {
    font-size: 0.92rem;
    line-height: 1.55;
    color: #4b5563;
    margin: 0;
}

/* ---------- Quiz result ---------- */
.result-card {
    background: linear-gradient(135deg, #1b5e20 0%, #388e3c 100%);
    border-radius: 16px;
    padding: 30px 26px;
    text-align: center;
    color: #ffffff;
    box-shadow: 0 8px 22px rgba(20, 83, 45, 0.20);
    margin-bottom: 18px;
}
.result-card .result-score {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
}
.result-card .result-msg {
    font-size: 1.05rem;
    color: #eaf7ea;
    margin-top: 10px;
}

/* ---------- Sidebar navigation ---------- */
section[data-testid="stSidebar"] {
    background: #14532d;
}
section[data-testid="stSidebar"] * {
    color: #e8f5e9;
}
section[data-testid="stSidebar"] h3 {
    color: #ffffff;
    margin-bottom: 0;
}
section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    background: transparent;
    color: #e8f5e9;
    border: 1px solid rgba(255, 255, 255, 0.28);
    border-radius: 10px;
    text-align: left;
    justify-content: flex-start;
    padding: 0.55rem 0.9rem;
    font-weight: 500;
    margin-bottom: 4px;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255, 255, 255, 0.14);
    color: #ffffff;
    border-color: #a5d6a7;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"],
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] {
    background: #a5d6a7;
    color: #14532d;
    border-color: #a5d6a7;
    font-weight: 700;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover,
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #c8e6c9;
    color: #14532d;
}

/* ---------- Main buttons ---------- */
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"] {
    background: #2e7d32;
    color: #ffffff;
    border: 1px solid #2e7d32;
    border-radius: 10px;
    font-weight: 600;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #1b5e20;
    border-color: #1b5e20;
    color: #ffffff;
}
.stButton > button[kind="secondary"],
.stButton > button[data-testid="stBaseButton-secondary"] {
    border-radius: 10px;
    border: 1px solid #2e7d32;
    color: #14532d;
    background: #ffffff;
    font-weight: 600;
}

/* ---------- Footer ---------- */
.footer {
    margin-top: 40px;
    padding-top: 18px;
    border-top: 1px solid #d7ecdc;
    text-align: center;
    font-size: 0.85rem;
    color: #6b7280;
}
</style>"""

st.markdown(CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 3. WASTE DATA  (predefined dictionaries and lists - no database needed)
# ---------------------------------------------------------------------------
CATEGORIES = {
    "Wet Waste": {
        "icon": "🥬",
        "subtitle": "Biodegradable kitchen and garden waste",
        "bin": "Green bin (wet waste)",
        "examples": ["Vegetable peels", "Fruit waste", "Leftover food", "Tea leaves"],
        "disposal": (
            "Collect wet waste in a green bin lined with a compostable bag. "
            "Drain the extra liquid, keep the bin covered and hand it to your local "
            "waste collector every day. At home you can also compost it in a compost "
            "pot or a vermicompost bin and use the compost for plants."
        ),
        "note": (
            "Never mix wet waste with dry waste. The moisture spoils paper and "
            "plastic, so they can no longer be recycled."
        ),
        "accent": "#2e7d32",
        "bg": "#e8f5e9",
    },
    "Dry Waste": {
        "icon": "♻️",
        "subtitle": "Clean, dry and recyclable materials",
        "bin": "Blue bin (dry waste)",
        "examples": [
            "Paper",
            "Plastic bottles",
            "Cardboard",
            "Glass bottles",
            "Metal cans",
        ],
        "disposal": (
            "Empty and rinse every container, let it dry, then flatten boxes and "
            "bottles to save space. Keep dry waste in a blue bin or a separate bag "
            "and give it to your local kabadiwala (scrap dealer) or the nearest "
            "recycling collection centre."
        ),
        "note": (
            "Only clean and dry material can be recycled. A greasy box or a wet "
            "newspaper is usually rejected by recyclers."
        ),
        "accent": "#1565c0",
        "bg": "#e3f2fd",
    },
    "Hazardous Waste": {
        "icon": "⚠️",
        "subtitle": "Waste that needs special, careful disposal",
        "bin": "Separate box, then a hazardous / e-waste collection point",
        "examples": [
            "Batteries",
            "Expired medicines",
            "Chemical containers",
            "CFL bulbs",
        ],
        "disposal": (
            "Never put hazardous waste in the normal household bin. Store it "
            "separately in a closed, labelled container. Tape the terminals of used "
            "batteries, keep bulbs and containers unbroken, and drop everything at a "
            "municipal e-waste or hazardous-waste collection point. Many pharmacies "
            "also accept expired medicines."
        ),
        "note": (
            "Batteries, bulbs and chemicals contain heavy metals and toxic material. "
            "If they reach a landfill or a water body, they pollute soil and "
            "groundwater for years."
        ),
        "accent": "#c62828",
        "bg": "#ffebee",
    },
}

WASTE_ITEMS = {
    "Banana peel": {
        "category": "Wet Waste",
        "disposal": "Put it in the green wet waste bin, or add it to your home compost pot.",
        "explanation": (
            "Fruit peels are soft, biodegradable kitchen waste. They break down in a "
            "few weeks and make excellent compost for plants."
        ),
    },
    "Vegetable peels": {
        "category": "Wet Waste",
        "disposal": "Collect in the green bin and hand it to the waste collector, or compost it at home.",
        "explanation": (
            "Vegetable peels are biodegradable and rich in nutrients. Composting them "
            "keeps them out of landfills, where they would otherwise release methane."
        ),
    },
    "Leftover food": {
        "category": "Wet Waste",
        "disposal": "Drain the extra liquid and put it in the green bin. Try to cook only what you can eat.",
        "explanation": (
            "Cooked food is biodegradable wet waste. Draining the liquid keeps the bin "
            "dry and stops smell and flies. Avoiding food waste is even better than "
            "composting it."
        ),
    },
    "Tea leaves": {
        "category": "Wet Waste",
        "disposal": "Empty the tea leaves into the green bin or straight into a compost pot.",
        "explanation": (
            "Tea leaves are plant material, so they decompose easily and add nitrogen "
            "to compost. Remove the plastic tea bag first if you use one."
        ),
    },
    "Eggshells": {
        "category": "Wet Waste",
        "disposal": "Crush them slightly and add them to the green bin or your compost.",
        "explanation": (
            "Eggshells are organic kitchen waste. Crushing them helps them break down "
            "faster and adds calcium to the compost."
        ),
    },
    "Newspaper": {
        "category": "Dry Waste",
        "disposal": "Keep it clean and dry, tie it in a bundle and give it to a scrap dealer or paper recycler.",
        "explanation": (
            "Newspaper is clean paper waste that can be recycled several times. Selling "
            "it to a kabadiwala also earns a little money and saves trees."
        ),
    },
    "Old notebook": {
        "category": "Dry Waste",
        "disposal": "Remove plastic covers and spiral binding, then put the paper in the dry waste bin.",
        "explanation": (
            "Writing paper is high-quality recyclable paper. Removing plastic and metal "
            "parts keeps the paper stream clean for the recycler."
        ),
    },
    "Cardboard box": {
        "category": "Dry Waste",
        "disposal": "Remove tape and plastic, flatten the box and keep it in the dry waste bin.",
        "explanation": (
            "Cardboard is recycled into new boxes and paper products. Flattening it "
            "saves a lot of space in the bin and in the collection truck."
        ),
    },
    "Plastic water bottle": {
        "category": "Dry Waste",
        "disposal": "Empty and rinse the bottle, remove the cap, crush it and put it in the dry waste bin.",
        "explanation": (
            "PET bottles are easily recycled into new bottles and fibres, but only if "
            "they are empty and clean. Rinsing stops liquid from spoiling other "
            "recyclables."
        ),
    },
    "Milk or juice carton": {
        "category": "Dry Waste",
        "disposal": "Rinse it, flatten it and put it in the dry waste bin. Check if your local centre accepts cartons.",
        "explanation": (
            "Tetra Pak style cartons are made of paper, plastic and foil. They are "
            "recyclable, but they must be rinsed and flattened, and they need a centre "
            "that accepts multi-layer packaging."
        ),
    },
    "Plastic carry bag": {
        "category": "Dry Waste",
        "disposal": "Collect thin plastic bags separately and drop them at a plastic collection point. Reuse them first.",
        "explanation": (
            "Thin plastic bags are hard to recycle and easily fly into drains. Reusing "
            "them many times, or carrying a cloth bag instead, is the best option."
        ),
    },
    "Glass bottle": {
        "category": "Dry Waste",
        "disposal": "Rinse it and keep it in a safe, separate bag so it does not break and injure waste workers.",
        "explanation": (
            "Glass can be recycled endlessly without losing quality. Broken glass is "
            "dangerous for the people who collect and sort waste, so wrap it carefully."
        ),
    },
    "Aluminium can": {
        "category": "Dry Waste",
        "disposal": "Rinse it, crush it and put it in the dry waste bin or give it to a scrap dealer.",
        "explanation": (
            "Metal cans are one of the most valuable recyclables. Recycling aluminium "
            "uses only about 5% of the energy needed to make new aluminium."
        ),
    },
    "Broken ceramic cup": {
        "category": "Dry Waste",
        "disposal": "Wrap the pieces in newspaper, label the packet, and put it in the dry waste bin. Do not mix with glass recycling.",
        "explanation": (
            "Ceramic is not easily recyclable and melts at a different temperature than "
            "glass. Wrapping it safely protects the waste collectors from cuts."
        ),
    },
    "Used battery": {
        "category": "Hazardous Waste",
        "disposal": "Tape the terminals, keep it in a closed box and drop it at an e-waste or hazardous-waste collection point.",
        "explanation": (
            "Batteries contain heavy metals such as mercury, cadmium and lead. If they "
            "break in a landfill, these metals leak into soil and groundwater."
        ),
    },
    "Expired medicines": {
        "category": "Hazardous Waste",
        "disposal": "Keep them in the original pack and hand them to a pharmacy take-back bin or a hazardous-waste centre.",
        "explanation": (
            "Medicines should never be flushed down the drain or thrown in a normal bin. "
            "Their chemicals can enter water sources and harm people and animals."
        ),
    },
    "CFL bulb": {
        "category": "Hazardous Waste",
        "disposal": "Store it unbroken in a padded box and give it to an e-waste collection centre.",
        "explanation": (
            "CFL bulbs contain a small amount of mercury. A broken bulb releases mercury "
            "vapour, so it must be handled and disposed of carefully."
        ),
    },
    "Chemical or paint container": {
        "category": "Hazardous Waste",
        "disposal": "Keep the lid closed, store it away from children and hand it to a hazardous-waste collection point.",
        "explanation": (
            "Leftover paint thinner, pesticides and cleaners are toxic. They can catch "
            "fire and pollute water, so they need a special collection point, not a "
            "household bin."
        ),
    },
    "Old mobile charger": {
        "category": "Hazardous Waste",
        "disposal": "Put it in an e-waste collection box or give it to a certified e-waste recycler.",
        "explanation": (
            "Chargers and cables contain copper and plastic plus small amounts of heavy "
            "metals. E-waste recyclers recover the metal safely instead of burning it."
        ),
    },
}

TIPS = [
    {
        "icon": "🗑️",
        "title": "Separate wet and dry waste",
        "text": "Keep two bins at home. Water-heavy food waste spoils paper and plastic, and mixed waste cannot be composted or recycled.",
    },
    {
        "icon": "🚫",
        "title": "Avoid single-use plastics",
        "text": "Say no to disposable straws, cutlery and thin carry bags. They are used for minutes and stay in the environment for centuries.",
    },
    {
        "icon": "🫙",
        "title": "Reuse plastic containers",
        "text": "Wash and reuse jars, bottles and boxes for storage instead of buying new ones. Reuse saves more resources than recycling.",
    },
    {
        "icon": "📰",
        "title": "Recycle newspapers and cardboard",
        "text": "Keep paper clean and dry, then sell it to a scrap dealer. One tonne of recycled paper saves around 17 trees.",
    },
    {
        "icon": "🛍️",
        "title": "Carry reusable shopping bags",
        "text": "Keep a cloth bag in your school bag or car. One cloth bag can replace hundreds of plastic bags in a single year.",
    },
    {
        "icon": "🌱",
        "title": "Compost kitchen waste",
        "text": "Convert peels and leftovers into compost in a pot or a vermicompost bin. The compost feeds your plants for free.",
    },
    {
        "icon": "🔋",
        "title": "Dispose of batteries safely",
        "text": "Never throw batteries in the household bin. Collect them and drop them at an e-waste or battery collection point.",
    },
    {
        "icon": "📝",
        "title": "Avoid wasting paper",
        "text": "Use both sides of a page, take notes digitally when you can, and reuse one-sided printouts as rough paper.",
    },
]

QUIZ_QUESTIONS = [
    {
        "question": "Which bin should vegetable peels and leftover food go into?",
        "options": [
            "The green wet waste bin",
            "The blue dry waste bin",
            "The red hazardous waste box",
            "Any bin, because food breaks down anywhere",
        ],
        "answer": 0,
        "explanation": (
            "Food peels and leftovers are biodegradable, so they go into the wet waste "
            "bin, where they can be composted or processed safely."
        ),
    },
    {
        "question": "Which of these is hazardous household waste?",
        "options": ["Newspaper", "A used battery", "A glass bottle", "Banana peel"],
        "answer": 1,
        "explanation": (
            "Used batteries contain heavy metals and must go to an e-waste or "
            "hazardous-waste collection point, never into the normal bin."
        ),
    },
    {
        "question": "What do the three Rs of waste management stand for?",
        "options": [
            "Read, Run, Rest",
            "Reduce, Reuse, Recycle",
            "Remove, Repair, Rebuild",
            "Recycle, Reject, Repeat",
        ],
        "answer": 1,
        "explanation": (
            "Reduce first (use less), then Reuse whatever you can, and Recycle only "
            "what is left over."
        ),
    },
    {
        "question": "What should you do before putting a plastic bottle into the dry waste bin?",
        "options": [
            "Fill it with water",
            "Rinse it, empty it and crush it",
            "Mix it with leftover food",
            "Burn it to make it smaller",
        ],
        "answer": 1,
        "explanation": (
            "A bottle is recyclable only when it is empty, clean and dry. Crushing it "
            "saves space in the bin."
        ),
    },
    {
        "question": "Why is it important to keep wet and dry waste separate?",
        "options": [
            "So the bins look neater",
            "Because wet waste is heavier",
            "So that waste can actually be composted or recycled",
            "It is not important at all",
        ],
        "answer": 2,
        "explanation": (
            "Mixing wet waste with paper and plastic spoils the recyclables. When they "
            "are separated, wet waste becomes compost and dry waste becomes new products."
        ),
    },
]


# ---------------------------------------------------------------------------
# 4. SMALL HTML HELPERS  (used to draw the cards)
# ---------------------------------------------------------------------------
def category_card(name, data):
    """Build the HTML of one waste category card."""
    examples = ", ".join(data["examples"])
    return (
        '<div class="eco-card" style="border-top:5px solid ' + data["accent"] + ';">'
        '<div class="card-icon" style="background:' + data["bg"] + ';">' + data["icon"] + "</div>"
        '<h3 class="card-title">' + name + "</h3>"
        '<p class="card-sub">' + data["subtitle"] + "</p>"
        "<p><strong>Examples:</strong> " + examples + "</p>"
        "<p><strong>Correct disposal:</strong> " + data["disposal"] + "</p>"
        '<div class="card-note">'
        "<strong>🗂️ Bin:</strong> " + data["bin"] + "<br>"
        "<strong>💡 Remember:</strong> " + data["note"] + "</div>"
        "</div>"
    )


def stat_card(icon, value, text):
    """Build the HTML of one statistics card."""
    return (
        '<div class="stat-card">'
        '<div class="stat-icon">' + icon + "</div>"
        '<div class="stat-value">' + value + "</div>"
        '<p class="stat-text">' + text + "</p>"
        "</div>"
    )


def tip_card(tip):
    """Build the HTML of one recycling tip card."""
    return (
        '<div class="tip-card">'
        '<span class="tip-icon">' + tip["icon"] + "</span>"
        '<span class="tip-title">' + tip["title"] + "</span>"
        '<p class="tip-text">' + tip["text"] + "</p>"
        "</div>"
    )


def footer():
    """Small footer shown on every page."""
    st.markdown(
        '<div class="footer">EcoSort ♻️ &nbsp;|&nbsp; Small Steps, Cleaner Planet. '
        "&nbsp;|&nbsp; An Environmental Studies (EVS) academic project built with "
        "Python and Streamlit.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 5. PAGE 1 - HOME
# ---------------------------------------------------------------------------
def page_home():
    st.markdown(
        '<div class="hero">'
        '<span class="hero-badge">Environmental Studies Project</span>'
        "<h1>♻️ EcoSort</h1>"
        '<p class="tagline">Small Steps, Cleaner Planet.</p>'
        '<p class="hero-text">Welcome to EcoSort, a simple website that helps you '
        "understand recycling and waste management. Every day our homes produce "
        "vegetable peels, plastic bottles, old newspapers and used batteries, and "
        "most of this waste is thrown away mixed together. When waste is separated "
        "correctly, food scraps become compost, paper and plastic become new "
        "products, and harmful items are disposed of safely.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### 🌍 Why waste management matters")
    st.write(
        "Waste management is the process of collecting, sorting, treating and "
        "disposing of waste in a way that is safe for people and for the environment. "
        "When waste is dumped in open grounds or burned, it pollutes the air, soil and "
        "water, harms animals and speeds up climate change. The good news is that a "
        "large part of household waste is not really waste at all: it is a resource. "
        "Segregating waste at home is the simplest and most powerful step, because "
        "mixed waste cannot be recycled while separated waste can."
    )

    st.markdown("### 📊 A few facts worth knowing")
    stats = [
        ("♻️", "9%", "Only about 9% of all the plastic ever produced in the world has actually been recycled."),
        ("🗑️", "1.7 lakh", "tonnes of solid waste are generated in India every single day, and a large part of it is household waste."),
        ("🌱", "80%", "Nearly 80% of what we throw away from home can be composted or recycled if it is separated properly."),
    ]
    columns = st.columns(3)
    for column, (icon, value, text) in zip(columns, stats):
        with column:
            st.markdown(stat_card(icon, value, text), unsafe_allow_html=True)

    st.markdown("### 🧭 Explore EcoSort")
    st.write("Pick a section to start learning, or use the menu in the sidebar.")

    buttons = [
        ("🗂️ Waste Categories", "Learn about wet, dry and hazardous waste", "🗂️ Waste Categories"),
        ("🔍 Waste Identifier", "Find out where a household item belongs", "🔍 Waste Identifier"),
        ("💡 Recycling Tips", "Simple habits that reduce waste every day", "💡 Recycling Tips"),
        ("🧠 Recycling Quiz", "Test your knowledge with five quick questions", "🧠 Recycling Quiz"),
    ]
    columns = st.columns(4)
    for column, (label, caption, page) in zip(columns, buttons):
        with column:
            if st.button(label, key="home_" + page, type="primary"):
                st.session_state.page = page
                st.rerun()
            st.caption(caption)

    footer()


# ---------------------------------------------------------------------------
# 6. PAGE 2 - WASTE CATEGORIES
# ---------------------------------------------------------------------------
def page_categories():
    st.markdown("## 🗂️ Waste Categories")
    st.write(
        "Household waste is usually divided into three groups. Knowing which group an "
        "item belongs to tells you the correct way to dispose of it. Click through the "
        "cards below to learn the examples, the right bin and the disposal method for "
        "each category."
    )

    columns = st.columns(3)
    for column, (name, data) in zip(columns, CATEGORIES.items()):
        with column:
            st.markdown(category_card(name, data), unsafe_allow_html=True)

    st.markdown("### 🪣 Quick segregation guide")
    guide_rows = [
        ("♻️ Wet Waste", "Green bin", "Food scraps, peels and garden waste that can be composted."),
        ("📦 Dry Waste", "Blue bin", "Clean paper, plastic, glass and metal that can be recycled."),
        ("⚠️ Hazardous Waste", "Separate labelled box", "Batteries, medicines, chemicals and bulbs collected for safe disposal."),
    ]
    for title, bin_name, meaning in guide_rows:
        st.markdown("**" + title + "** → " + bin_name + " · " + meaning)

    st.info(
        "Tip: if an item is both dirty and recyclable, clean it first. One greasy box "
        "can spoil a whole bag of recyclable paper."
    )
    footer()


# ---------------------------------------------------------------------------
# 7. PAGE 3 - WASTE IDENTIFIER
# ---------------------------------------------------------------------------
def page_identifier():
    st.markdown("## 🔍 Waste Identifier")
    st.write(
        "Choose a common household item from the list and EcoSort will tell you its "
        "waste category, the correct disposal method and a short explanation."
    )

    item = st.selectbox(
        "Select a household waste item:",
        sorted(WASTE_ITEMS.keys()),
        index=None,
        placeholder="Type or choose an item...",
    )

    if item is None:
        st.info("👆 Please select an item from the dropdown to see its result.")
        st.markdown("**Items available:** " + ", ".join(sorted(WASTE_ITEMS.keys())))
        footer()
        return

    data = WASTE_ITEMS[item]
    category_name = data["category"]
    category = CATEGORIES[category_name]

    st.markdown(
        '<div class="eco-card" style="border-top:5px solid ' + category["accent"] + ';">'
        '<div class="card-icon" style="background:' + category["bg"] + ';">'
        + category["icon"] + "</div>"
        '<h3 class="card-title">' + item + "</h3>"
        '<p class="card-sub">Waste category</p>'
        '<span class="result-badge" style="background:' + category["bg"] + ";color:" + category["accent"] + ';">'
        + category["icon"] + " " + category_name + "</span>"
        "<p style=\"margin-top:14px;\"><strong>Recommended disposal:</strong> "
        + data["disposal"] + "</p>"
        '<div class="card-note"><strong>Bin:</strong> ' + category["bin"] + "<br>"
        "<strong>Why:</strong> " + data["explanation"] + "</div>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "Note: these results come from the predefined waste list used in this project, "
        "not from image recognition or machine learning."
    )
    footer()


# ---------------------------------------------------------------------------
# 8. PAGE 4 - RECYCLING TIPS
# ---------------------------------------------------------------------------
def page_tips():
    st.markdown("## 💡 Recycling Tips")
    st.write(
        "Eight simple habits that any household, hostel or classroom can follow. Start "
        "with one or two of them and add more as they become routine."
    )

    for start in range(0, len(TIPS), 3):
        columns = st.columns(3)
        for column, tip in zip(columns, TIPS[start:start + 3]):
            with column:
                st.markdown(tip_card(tip), unsafe_allow_html=True)

    st.success(
        "Remember the 3Rs: Reduce what you buy, Reuse what you already have, and "
        "Recycle only what is left."
    )
    footer()


# ---------------------------------------------------------------------------
# 9. PAGE 5 - RECYCLING QUIZ
# ---------------------------------------------------------------------------
def encouraging_message(score, total):
    """Return a friendly message based on the quiz score."""
    if score == total:
        return "🌍 Perfect score! You are a true EcoSort champion. Share these ideas with your friends and family."
    if score >= total - 1:
        return "🌟 Excellent work! You know your waste categories very well. Just one small detail to revise."
    if score >= total - 2:
        return "👍 Good effort! You have the basics right. A quick look at the Waste Categories page will make you an expert."
    if score >= 1:
        return "🌱 A good start! Revisit the Waste Categories page and try the quiz again - every attempt teaches you something new."
    return "🌱 Everyone starts somewhere! Read the Recycling Tips and Waste Categories pages, then come back and try again."


def page_quiz():
    st.markdown("## 🧠 Recycling Quiz")
    st.write(
        "Five quick questions on recycling and waste management. Choose one answer for "
        "each question and press **Submit Answers** to see your score."
    )

    total = len(QUIZ_QUESTIONS)
    result = st.session_state.get("quiz_result")

    # ----- Quiz form: shown while there is no result yet -----
    if result is None:
        with st.form("quiz_form"):
            answers = []
            for number, question in enumerate(QUIZ_QUESTIONS, start=1):
                st.markdown("**Q" + str(number) + ". " + question["question"] + "**")
                choice = st.radio(
                    "Answer for question " + str(number),
                    question["options"],
                    index=None,
                    key="quiz_q" + str(number),
                    label_visibility="collapsed",
                )
                answers.append(choice)
                st.write("")

            submitted = st.form_submit_button("Submit Answers", type="primary")

        if submitted:
            score = 0
            unanswered = 0
            for answer, question in zip(answers, QUIZ_QUESTIONS):
                if answer is None:
                    unanswered += 1
                elif answer == question["options"][question["answer"]]:
                    score += 1
            st.session_state.quiz_result = {
                "answers": answers,
                "score": score,
                "unanswered": unanswered,
            }
            st.rerun()

    # ----- Result view: shown after submitting -----
    else:
        score = result["score"]
        answers = result["answers"]

        st.markdown(
            '<div class="result-card">'
            '<div class="result-score">' + str(score) + " / " + str(total) + "</div>"
            '<div class="result-msg">' + encouraging_message(score, total) + "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

        percent = int(round(score / total * 100))
        st.progress(score / total)
        st.write("You answered **" + str(percent) + "%** of the questions correctly.")
        if result["unanswered"] > 0:
            st.warning(
                "You left " + str(result["unanswered"]) + " question(s) unanswered. "
                "Unanswered questions are counted as incorrect."
            )

        st.markdown("### 📋 Answer review")
        for number, question in enumerate(QUIZ_QUESTIONS, start=1):
            correct_answer = question["options"][question["answer"]]
            user_answer = answers[number - 1]
            if user_answer == correct_answer:
                heading = "✅ Q" + str(number) + " - Correct"
            else:
                heading = "❌ Q" + str(number) + " - Incorrect"

            with st.expander(heading):
                st.write("**Question:** " + question["question"])
                st.write("**Your answer:** " + (user_answer if user_answer else "Not answered"))
                st.write("**Correct answer:** " + correct_answer)
                st.info(question["explanation"])

        if st.button("Try Again", type="primary"):
            st.session_state.quiz_result = None
            for number in range(1, total + 1):
                st.session_state.pop("quiz_q" + str(number), None)
            st.rerun()

    footer()


# ---------------------------------------------------------------------------
# 10. SIDEBAR NAVIGATION AND MAIN PROGRAM
# ---------------------------------------------------------------------------
PAGES = {
    "🏠 Home": page_home,
    "🗂️ Waste Categories": page_categories,
    "🔍 Waste Identifier": page_identifier,
    "💡 Recycling Tips": page_tips,
    "🧠 Recycling Quiz": page_quiz,
}

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if st.session_state.page not in PAGES:
    st.session_state.page = "🏠 Home"

with st.sidebar:
    st.markdown("### ♻️ EcoSort")
    st.caption("Small Steps, Cleaner Planet.")
    st.markdown("---")

    for name in PAGES:
        is_active = name == st.session_state.page
        if st.button(
            name,
            key="nav_" + name,
            type="primary" if is_active else "secondary",
            use_container_width=True,
        ):
            if not is_active:
                st.session_state.page = name
                st.rerun()

    st.markdown("---")
    st.caption("An Environmental Studies (EVS) project built with Python and Streamlit.")

# Draw the selected page
PAGES[st.session_state.page]()
