# Python Crash Course (3rd Edition) - Data Visualization

Practice exercises and projects from **Part II (Chapters 15–17)** of *Python Crash Course* by Eric Matthes.

---

## 📁 Projects & Exercises

### 1. [`mpl_squares.py`](file:///home/flcsezz/ai_tools/python_practice/Part2practice/ch15-17/mpl_squares.py)
- Introductory line and scatter plots using Matplotlib.
- Covers customizing line thickness, styles (`dark_background`), colormaps (`plt.cm.Reds`), and axis tick formatting.

### 2. [`mpl_ex15-1-2.py`](file:///home/flcsezz/ai_tools/python_practice/Part2practice/ch15-17/mpl_ex15-1-2.py)
- **Exercise 15-1 & 15-2: Cubes**:
  - Plots the first 5,000 cubic numbers.
  - Explores list comprehensions vs. generators, custom axis limits (`xlim`, `ylim`), and styling.

### 3. [`random_walk.py`](file:///home/flcsezz/ai_tools/python_practice/Part2practice/ch15-17/random_walk.py)
- **Random Walk Visualization**:
  - Object-oriented simulation of random particle movement in a 2D space.
  - Refactored with a dedicated `get_step()` method (**Exercise 15-5**).
  - Visualized with a continuous color gradient, highlighted start point (green) and endpoint (red), and hidden axis ticks.

---

## 🛠️ Setup & Requirements

Make sure you have Matplotlib installed:

```bash
pip install matplotlib
```

> **Note for Linux users:** If running into GDK/GTK display issues, set the Matplotlib backend to `TkAgg`:
> ```bash
> MPLBACKEND=TkAgg python random_walk.py
> ```
