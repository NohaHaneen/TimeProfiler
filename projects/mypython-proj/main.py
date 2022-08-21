import sys
sys.path.append(r"C:\Users\nohah\simple-profiler-NohaHaneen")
import time_profiler

@time_profiler.profiler
def display1(msg):
    print(msg)


@time_profiler.profiler
def display2(num):
    print("i = ", num)


@time_profiler.profiler
def main():
    display1("start")
    for i in range(5):
        display2(i)
    display1("end")


main()
