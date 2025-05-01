# 🐍 Python Problem Series

Welcome to the **Python Problem Series** — a dedicated repository where I solve two Python programming challenges daily to build consistency, sharpen logic, and improve problem-solving skills.

---

## 📌 About This Repository

This project is a **daily Python coding streak** I started as part of my learning journey. It features small, focused problems designed to reinforce Python fundamentals and logic-building through consistent hands-on practice.

Each day includes:

- ✅ 2 new Python problems  
- 🧠 A focus on core concepts (e.g., lists, strings, conditionals, loops, functions)  
- 📈 Clean, readable, and beginner-friendly code  
- 🔁 Continuous GitHub contributions to maintain learning momentum  

---

## 🛠 Structure

Each file in the repository typically follows this structure:

- **Problem statement** (as a comment or docstring)
- **Well-documented solution**
- **Proper error handling**
- **Readable variable names**
- **Input/output interaction through terminal**

---

## 📂 Example Problem
Task: Take a list of integers (space-separated) from the user. Keep only the numbers that are greater than 10. Square each of those numbers. Print the final list. Also, print how many numbers were squared. If no number is greater than 10, show: "No numbers greater than 10."


```python
def filter_and_square(numbers: list) -> tuple:
    """Returns list of squares of numbers > 10 and their count."""
    filtered = [n ** 2 for n in numbers if n > 10]
    return filtered, len(filtered)

```

## 🎯 Goals
- 🧩 Build a daily coding habit

- 📚 Strengthen understanding of Python basics

- 🧠 Improve logical thinking

- ⏱ Prepare for real-world software problem solving

- 🌱 Grow gradually towards larger projects

## 🔥 Streak Commitment
I’ve made a personal commitment to contribute at least one solution per day for life — building discipline and showcasing consistent growth as a developer.

## 🚀 How to Run
**Clone the repository:**

git clone https://github.com/code-with-shahzaib/python-problem-series.git

**cd python-problem-series**

Run a problem file using:
**python problem_filename.py**

# 🧾 License
This repository is open-sourced under the MIT License.

## 🙌 Let’s Connect
Feel free to connect with me:

**🌐 GitHub: code-with-shahzaib**

**💡 Always open to feedback and collaboration!**
