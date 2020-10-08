#!/usr/bin/python

import argparse
import importlib.util
import logging
import logging.handlers
import os.path
import sys
import time

root = logging.getLogger()
root.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
root.addHandler(logging.StreamHandler())


def main(n):
    problem_file = './problems/problem{0}.py'.format(n)
    if os.path.isfile(problem_file):
        answer_file = './answers/problem{0}.log'.format(n)
        handler = logging.handlers.WatchedFileHandler(os.environ.get('LOGFILE', answer_file))
        root.addHandler(handler)

        logging.info('Running: {0}'.format(problem_file))

        spec = importlib.util.spec_from_file_location('module.name', problem_file)
        problem = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(problem)

        t = time.time()
        a = problem.problem()

        logging.info('Answer: {0}'.format(a))
        logging.info('Time: {0}\n'.format(time.time() - t))
    else:
        _file = open(problem_file, 'a')
        _file.write('''#!/usr/bin/python\n\n\ndef problem():\n\treturn None''')
        _file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate Problem N')
    parser.add_argument('N', metavar='N', type=int, help='an integer for problem number')
    args = parser.parse_args()

    main(args.N)
