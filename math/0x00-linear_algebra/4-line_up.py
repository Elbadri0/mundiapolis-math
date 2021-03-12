#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        result = []
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
    return None
  
