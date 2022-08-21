# template-simple-profiler
Simple profiler

---

Implement a simple profiler named `time-profiler.py` that given a python project, it modifies the code to calculate and store the execution time of methods in a file named `exec-time.log` during execution. This file should contain name of the methods (including path to .py file) and total elapsed time in milliseconds. Note that a method can be invoked multiple times, therefore the profiler should report the total time the program spent in that method.  

Execution scenario:  
Suppose the python project is in directory "/projects/mypython-proj" and "/projects/mypython-proj/main.py" contains a `main` method.  

$ python time-profiler.py /projects/mypython-proj  
$ cd /projects/mypython-proj  
$ python main.py  
$ cat exec-time.log  

Tip: Implement a wrapper method for timing, and annotate the methods with that wrapper.



Sample Input: (main.py)
```
def display1(msg):
  print(msg)

def display2(num):
  print("i = ", num)

def main():
  display1("start")
  for i in range(5):
    display2(i)
  display1("end")
```

Sample Output: (exec-time.log)
```
path, method, time
/projects/mypython-proj/main.py, display1, 0.002 ms
/projects/mypython-proj/main.py, display2, 0.005 ms
/projects/mypython-proj/main.py, main, 0.007 ms
```

No worries if you see different timing values in your machine in different runs, that's totally fine.




Submission: Return the assignment via Teams with the URL of your repository (i.e., https://github.com/UHSETeaching/simple-profiler-YOURID).

Grading: No auto-grading, we will grade manually this assignment.

Late policy: You are only allowed one 48 hour late submission. 20 points will be deducted for each additional day.
