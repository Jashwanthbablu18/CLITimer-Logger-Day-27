# 🧩 Day 27 - Chaining Decorators (Timer + Logger)

Hey there! 👋  
Welcome to **Day 27** of my **#30DaysOfPythonChallenge**. Today, I explored **chaining decorators** to supercharge function behavior — adding both **timing** and **logging** in one go!

---

## 📌 What’s This About?
Today’s focus:
- Applying **multiple decorators** on a function
- Understanding **execution order** of decorators
- Profiling and logging function performance

---

## 💭 Why Is This Useful?
Combining decorators is a **clean way to stack reusable behavior**:
- 🕵️ Log function usage for monitoring/debugging
- ⏱️ Profile performance to identify bottlenecks

---

## 🔧 What It Does

- 🧠 `@logger`: Logs function name, arguments, and return value
- ⏱️ `@timer`: Measures execution time
- 📊 Used on a **Bubble Sort** function to:
  - Sort data
  - Log details
  - Profile time taken


## 🧪 Sample Output

- 🚀 Running 'bubble_sort' with args: ([64, 34, 25, 12, 22, 11, 90],) kwargs: {}
- ✅ Finished 'bubble_sort', returned: [11, 12, 22, 25, 34, 64, 90]
- ⏱️ Execution Time of 'bubble_sort': 0.0001 seconds

## 🚀 Run the Program

```bash
python Day-27Code.py

---
