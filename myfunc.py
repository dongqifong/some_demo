from dataclasses import dataclass
from typing import List
import random

@dataclass
class Data:
    time: int
    state: bool
    
def generate_test_data(times: List[int]) -> List[Data]:
    """
    根據給定的時間清單 times，產生 Data 資料並且確保時間是有序的。
    state 依據 random 或者固定邏輯設定。這裡為了觀察方便，可以直接用 random。
    """
    data_list = []
    for t in times:
        # 為了示範，這裡的 state 直接用 random
        state = random.choice([True, False])
        data_list.append(Data(time=t, state=state))
    return data_list

def window_segmentation(data_list: List[Data], window_size: int, left_limit: int, right_limit: int) -> List[List[Data]]:
    # 檢查基本條件
    if not data_list or window_size <= 0 or right_limit <= left_limit:
        return []
    
    segments = []
    n = len(data_list)
    i = 0

    # 略過小於 left_limit 的資料
    while i < n and data_list[i].time < left_limit:
        i += 1

    # 以 left_limit 為起點開始分段
    t_start = left_limit
    while t_start < right_limit:
        t_end = t_start + window_size
        if t_end > right_limit:
            t_end = right_limit  # 最後一段可能不足 window_size 秒
        segment = []
        # 收集時間在 [t_start, t_end) 內的資料
        while i < n and data_list[i].time < t_end:
            # 因為前面的迴圈已經排除了小於 left_limit 的資料，
            # 此處的資料理論上都滿足 data_list[i].time >= t_start
            segment.append(data_list[i])
            i += 1
        segments.append(segment)
        t_start += window_size

    return segments


def second_segmentation(data_list: List[Data], second: int, left_limit: int, right_limit: int) -> List[List[Data]]:
    # 檢查基本條件
    if not data_list or second <= 0 or right_limit <= left_limit:
        return []
    
    segments = []
    n = len(data_list)
    i = 0

    # 略過小於 left_limit 的資料（不納入任何 segment）
    while i < n and data_list[i].time < left_limit:
        i += 1

    # 只要還有資料點，就一直嘗試切 segment
    while i < n:
        # 以當前 data_list[i] 的時間作為新 segment 的起點
        t_start = data_list[i].time
        
        # 如果 t_start 已經超過 right_limit，就沒有必要再切割
        if t_start >= right_limit:
            break
        
        # 計算此段的終點（window_size 寬度，若超過 right_limit 就截斷）
        t_end = t_start + second
        if t_end > right_limit:
            t_end = right_limit
        
        # 收集 [t_start, t_end) 之間的資料
        segment = []
        while i < n and data_list[i].time < t_end:
            segment.append(data_list[i])
            i += 1
        
        segments.append(segment)
    
    return segments

def show_results(segments: List[List[Data]], window_size:int, times:List[int], test_case:str):
    print(f"==============================={test_case}================================\nwindow_size = {window_size}\ntimes = {times}\n")
    for segment in segments:
        print(" ", segment)