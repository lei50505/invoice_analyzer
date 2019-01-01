#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""doc"""

import time
import os
from functools import wraps

def singleton(cls):
    """doc"""
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

def fn_time(func):
    """doc"""
    @wraps(func)
    def function_time(*args, **kw):
        """doc"""
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print("[%s]:[%s seconds]" \
            % (func.__name__, str(end_time - start_time)))
        return result
    return function_time

@singleton
class Data():
    """doc"""
    def __init__(self):
        self.data = {}
    def set(self, key, val):
        """doc"""
        self.data[key] = val
    def get(self, key):
        """doc"""
        return self.data.get(key)

def to_float(val):
    """doc"""
    # pylint:disable=broad-except
    try:
        return float(val)
    except Exception:
        return None

def to_str(val):
    """doc"""
    # pylint:disable=broad-except
    if val is None:
        return None
    try:
        return str(val)
    except Exception:
        return None

def line_sep():
    """doc"""
    return os.linesep

def sep():
    """doc"""
    return os.sep

def is_dir(path):
    """doc"""
    return os.path.isdir(path)

def is_file(path):
    """doc"""
    return os.path.isfile(path)
def abs_path(path):
    """doc"""
    return os.path.abspath(path)
def base_name(path):
    """doc"""
    return os.path.basename(path)
def split_ext(path):
    """doc"""
    return os.path.splitext(path)[1]

def main():
    """doc"""

    print(base_name("b/a.txt"))
    time.sleep(2)


if __name__ == '__main__':
    main()
