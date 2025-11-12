# Intelligent Systems Seminar 1 — Mill Game AI

---

## Setup

Install the required package in your Python environment:

```bash
pip install famnit_gym@git+https://github.com/DomenSoberlFamnit/famnit-gym
```

For test_speed.py you also need:

```bash
pip install matplotlib
```
---

## Running the Examples

### 1. Play Human vs AI
Play interactively in a graphical window:

```bash
python human_vs_ai.py
```

You’ll control **Player 1 (Human)**.  
The AI difficulty can be set to `"easy"`, `"medium"`, or `"hard"`.  
(Default is `"hard"`, you can modify it inside the file.)

---

### 2. Run AI vs AI Matches
Let two AIs of different difficulties play against each other:

```bash
python main.py
```

You can modify difficulty and enable rendering in code:
```python
run_game("easy", "hard", render=True)
```

---

### 3. Run a Tournament
Compare AI levels automatically across multiple rounds:

```bash
python tournament.py
```

You can change the number of rounds:
```python
tournament(rounds=20)
```

---

### 4. Test Minimax Speed
Measure computation time vs search depth:

```bash
python test_speed.py
```

A plot will appear showing performance scaling.

---

## AI Logic Summary

- **Algorithm:** Minimax with Alpha-Beta Pruning  
- **Evaluation:**  
  `score = 100 * (pieces_difference) + (legal_moves_difference)`  
- **Difficulty Levels:**  
  - `easy` → depth 1  
  - `medium` → depth 2  
  - `hard` → depth 3  

---
