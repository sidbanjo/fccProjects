import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")

    num_arr = np.array(nums)
    num_mat = num_arr.reshape(3,3)

    calculations = {
        'mean': [list(num_mat.mean(axis=0)), list(num_mat.mean(axis=1)), num_arr.mean()],
        'variance': [list(num_mat.var(axis=0)), list(num_mat.var(axis=1)), num_arr.var()],
        'standard deviation': [list(num_mat.std(axis=0)), list(num_mat.std(axis=1)), num_arr.std()],
        'max': [list(num_mat.max(axis=0)), list(num_mat.max(axis=1)), num_arr.max()],
        'min': [list(num_mat.min(axis=0)), list(num_mat.min(axis=1)), num_arr.min()],
        'sum': [list(num_mat.sum(axis=0)), list(num_mat.sum(axis=1)), num_arr.sum()]
    }


    return calculations