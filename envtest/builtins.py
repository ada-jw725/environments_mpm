import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc  # 注：新 SciPy 版本 misc 已精简，课程示例保留此行
import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv() * b


def summarize_csv(file_path):
    """
    使用 Pandas 读取 CSV 文件并输出基本统计信息
    :param file_path: CSV 文件路径
    :return: DataFrame 的描述性统计结果
    """
    df = pd.read_csv(file_path)
    summary = df.describe(include="all")  # 包括数值和非数值列
    return summary
