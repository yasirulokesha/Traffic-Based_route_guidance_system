
# Traffic-Based Route Guidance System (TBRGS)

**COS30019 – Intelligent Systems Assignment 2B**  
Team ID: Group 3

## 🧠 Project Overview

This project implements a **Traffic-Based Route Guidance System (TBRGS)** that uses machine learning models to forecast traffic volumes and estimate optimal travel paths through the City of Boroondara. By combining predictive modeling with graph search algorithms, the system dynamically guides users through the most efficient routes based on expected traffic conditions.

This system builds upon the foundational work from Assignment 2A and extends it with:
- Multiple time-series machine learning models (LSTM, GRU, and a simple RNN)
- Dynamic prediction of future traffic volume
- Travel time estimation based on predicted traffic
- A top-k shortest path route finder
- A user-friendly graphical interface for real-time interaction

---

## 📁 Project Structure

```
IntroToAI-Assignment-2B/
│
├── DataSet/
├── Resources/
│
├── TBRGS/
│   ├── data/
│   ├── notebooks/
│   └── src/
│       ├── algorithms/
│       │   └── yens_algorithm.py
│       │
│       ├── gui/
│       │   ├── route_maps/
│       │   ├── dashboard.py
│       │   ├── loading_gif.gif
│       │   ├── map.jpg
│       │   └── route_generator.py
│       │
│       ├── models/
│       │   ├── GRU_model/
│       │   │   ├── models/
│       │   │   └── scalers/
│       │   │
│       │   ├── LSTM_model/
│       │   │   ├── models/
│       │   │   └── scalers/
│       │   │
│       │   |── RNN_model/
│       │   |   ├── models/
│       │   |   └── scalers/
|       |   ├── GRU_model.py
│       │   ├── LSTM_model.py
│       │   └── RNN_model.py
│       │
│       ├── data_processing.py
│       ├── graph.py
│       ├── main.py
│       └── travel_time_estimator.py
│
├── tests/
│   ├── test_graph.py
│   └── test_main.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📊 Machine Learning Models

We implemented and compared the following time-series models:

- **LSTM (Long Short-Term Memory):** RNN variant effective for sequence prediction.
- **GRU (Gated Recurrent Unit):** Lightweight alternative to LSTM with fewer parameters.
- **[Third Model, e.g., Random Forest Regressor or Transformer]:** Chosen for baseline or hybrid performance.

Each model was trained on traffic volume data recorded from sensors across Boroondara in October 2006, predicting volume at 15-minute intervals for future times.

---

## 🧮 How It Works

### 1. **Data Preprocessing**
   - Load and clean time-series traffic sensor data
   - Normalize and reshape for training ML models

### 2. **Traffic Forecasting**
   - Train LSTM, GRU, and another model on historical data
   - Predict traffic volume for user-selected future times

### 3. **Travel Time Estimation**
   - Translate predicted volume into travel time using a regression-based mapping formula

### 4. **Route Finding**
   - Construct a graph where nodes = intersections and edges = road segments
   - Use Dijkstra’s algorithm or A* to calculate **top-k shortest paths** by predicted travel time

### 5. **Graphical User Interface**
   - Users select source, destination, and future time
   - GUI displays top-k recommended paths with estimated travel times and visual overlays

---

## 🚀 Getting Started

### Step 1: Clone the Repository
```bash
git clone 
```

### Step 2: Install Dependencies
Ensure you have Python 3.9+ installed, then:
Make an Anconda environment and install with followings
```bash
pip install -r requirements.txt
```

### Step 3: Launch the App
```bash
python TBRGS/src/main.py
```

This will open the GUI for route prediction and display.

---

## 🧪 Testing

To run all unit and integration tests:
```bash
python -m unittest discover -s tests
```

---

## 📷 Sample Screenshots

> - Add screenshots of:
> - Traffic volume prediction graph
> - Route visualization with top-k paths
> - GUI home screen

---

## 👨‍💻 Team Members

- Yasiru Lokesha  
- Prawud Rathnayake 
- Alex Vrsecky
- Justin Tran

---

## 📄 Final Report

All technical documentation, architecture diagrams, and evaluation metrics are available in:  
📁 `Main Report.pdf`

---

## 📌 Notes

- The dataset used is **City of Boroondara – Traffic Sensor Data (October 2006)**.
- The prediction models rely solely on the provided historical data without external sources.
- GUI developed using [Tkinter / Matplotlib / Networkx] – supports real-time input and route display.
- Graph-based pathfinding uses NetworkX.

---

## 📦 Dependencies

Here are the main Python libraries used:

```text
numpy
pandas
scikit-learn
matplotlib
seaborn
tensorflow
keras
torch
networkx
tkinter
PyQt5
```

All dependencies can be installed with:
```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is submitted for academic purposes only for COS30019.  
All content is original and not intended for commercial or distribution use.

---
