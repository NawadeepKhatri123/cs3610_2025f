# Q21 – Final Submission  
**Course:** CS3610 – Software Engineering  

Name : Nawadeep Khatri
SID : 5086950

## Solution Overview

### Answer to Q1 – task1.txt
---

### Answer to Q2 – final.drawio.png / final.drawio.pdf

---

### Answer to Q3 – Implementation
The implementation of the selected design pattern is located in the `observer_pattern` directory.

#### How to Run the Program
```bash
cd observer_pattern
python main.py

#### Output
```bash
Student_A followed Dr. Hanna
Student_B followed Dr. Hanna
Student_C followed Dr. Hanna

 Dr. Hanna posted: Midterm grades are out
notifying followers...
 -> Student_A got update from Dr. Hanna : Midterm grades are out
 -> Student_B got update from Dr. Hanna : Midterm grades are out
 -> Student_C got update from Dr. Hanna : Midterm grades are out
Student_B unfollowed Dr. Hanna

 Dr. Hanna posted: Final exams just ended !!!!
notifying followers...
 -> Student_A got update from Dr. Hanna : Final exams just ended !!!!
 -> Student_C got update from Dr. Hanna : Final exams just ended !!!!
Dr. Hanna removed Student_C
Student_C unfollowed Dr. Hanna

 Dr. Hanna posted: !!! Happy Holidays !!!
notifying followers...
 -> Student_A got update from Dr. Hanna : !!! Happy Holidays !!!



