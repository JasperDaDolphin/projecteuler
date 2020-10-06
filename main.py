import sys
import importlib.util
import os.path
import time

def main(n):
    _file = "./problems/problem{0}.py".format(n)
    if os.path.isfile(_file):
        print("Running: ", _file)
        spec = importlib.util.spec_from_file_location("module.name", _file)
        problem = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(problem)

        t = time.time()
        a = problem.problem()
        print("Awnser: ", a)
        print("Time: ", time.time() - t)

if __name__ == "__main__":
   main(sys.argv[1])