from typing import List

from myfunc import Data
from myfunc import generate_test_data, window_segmentation, show_results


left_limit = 0
right_limit = 30
span = 5
times = [0, 3, 4, 10, 11, 12, 17, 23, 25, 28, 29]

test_data_1 = generate_test_data(times)
segments_1 = window_segmentation(
    data_list=test_data_1,
    span=span,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_1, span, times, "test_data_1")

left_limit = 0
right_limit = 30
span = 10
times = [-5, -1, 0, 2, 8, 9, 11, 12, 29, 30, 31, 40]

test_data_2 = generate_test_data(times)
segments_2 = window_segmentation(
    data_list=test_data_2,
    span=span,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_2, span, times, "test_data_2")

left_limit = 10
right_limit = 30
span = 5
times = [0, 1, 2, 7, 9, 10, 15, 28, 45, 46, 50] 

test_data_3 = generate_test_data(times)
segments_3 = window_segmentation(
    data_list=test_data_3,
    span=span,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_3, span, times, "test_data_3")

left_limit = 0
right_limit = 52
span = 10
times = [0, 1, 2, 10, 11, 25, 26, 27, 40, 50, 51]

test_data_4 = generate_test_data(times)
segments_4 = window_segmentation(
    data_list=test_data_4,
    span=span,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_4, span, times, "test_data_4")

# 範例程式
test_data_5a = generate_test_data([])  # 空清單
segments_5a = window_segmentation(
    data_list=test_data_5a,
    span=5,
    left_limit=0,
    right_limit=10
)

show_results(segments_5a, 5, [], "test_data_5a")
