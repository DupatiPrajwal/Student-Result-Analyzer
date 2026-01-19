# Student-Result-Analyzer

## 📝 Project Overview
**Student Result Analyzer** is a Python-based console application designed to calculate and display a student's academic performance. It allows teachers or students to input marks for five subjects and automatically computes the total, percentage, class, and grade. The program also handles multiple students efficiently.

---

## 💡 Features
- Input marks for **English, Maths, Physics, Chemistry, and Computer Science**.  
- Automatically calculates **total marks** and **percentage**.  
- Determines **pass/fail status** based on individual subject marks.  
- Assigns **class**: Distinction, First Class, Pass.  
- Assigns **grade**: +A, A, B, C, F.  
- Supports **multiple student entries** in one run.  
- Ensures that **failing in any subject results in overall fail**, regardless of percentage.

---

## ⚙️ Functionality
1. **Input Section:**  
   - Enter student name and roll number.  
   - Enter marks for all five subjects.  

2. **Validation & Calculation:**  
   - Checks if marks in each subject are passing (>=35).  
   - Calculates total marks and percentage.  
   - Determines pass/fail status.  

3. **Result & Grade Assignment:**  
   - Assigns class based on percentage:  
     - `Distinction` for ≥75%  
     - `First Class` for ≥60%  
     - `Pass` for ≥40%  
     - `Fail` for <40% or failing any subject  
   - Assigns grade based on percentage:  
     - `+A` ≥90%, `A` ≥75%, `B` ≥60%, `C` ≥40%, `F` <40%  

4. **Loop for Multiple Students:**  
   - Program asks after each student whether you want to enter another.  

---


---

## 🛠️ How to Run
1. Clone the repository:
```bash
git clone https://github.com/DupatiPrajwal/Student-Result-Analyzer.git
python student_result_analyzer.py




