from myfunc import generate_test_data, second_segmentation, show_results


left_limit = 0
right_limit = 40
window_size = 10
times = [0, 1, 5, 10, 15, 16, 17, 25, 26, 30, 31, 39]  # 不等距 & 已排好序
test_data_1 = generate_test_data(times)
segments_1 = second_segmentation(
    data_list=test_data_1,
    window_size=window_size,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_1, window_size, times, "test_data_1")

left_limit = 10
right_limit = 30
window_size = 5
times = [5, 9, 10, 11, 12, 17, 18, 22, 29, 30, 35, 40]
# 其中 5,9 < 10; 35,40 > 30
test_data_2 = generate_test_data(times)
segments_2 = second_segmentation(
    data_list=test_data_2,
    window_size=window_size,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_2, window_size, times, "test_data_2")


left_limit = 10
right_limit = 30
window_size = 5
times = [8, 9, 10, 10, 10, 10, 11, 11, 11, 12, 13, 29, 30]
# 其中有多筆重複或接近的時間(10,10,10,10,11,11,11...)
# 也有一些 < left_limit(8,9) 與 = right_limit(30) 
test_data_3 = generate_test_data(times)
segments_3 = second_segmentation(
    data_list=test_data_3,
    window_size=window_size,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_3, window_size, times, "test_data_3")

# (A) 資料清單為空
test_data_4a = generate_test_data([])
segments_4a = second_segmentation(
    data_list=test_data_4a,
    window_size=10,
    left_limit=0,
    right_limit=10
)
show_results(segments_4a, 10, [], "test_data_4a")

# (B) window_size <= 0
test_data_4b = generate_test_data([0, 1, 2])
segments_4b = second_segmentation(
    data_list=test_data_4b,
    window_size=0,
    left_limit=0,
    right_limit=10
)
show_results(segments_4b, 0, [], "test_data_4b")

# (C) right_limit <= left_limit
test_data_4c = generate_test_data([0, 5, 10])
segments_4c = second_segmentation(
    data_list=test_data_4c,
    window_size=5,
    left_limit=10,
    right_limit=5
)
show_results(segments_4c, 5, [], "test_data_4c")

left_limit = 0
right_limit = 12
window_size = 10
times = [0, 1, 2, 10, 11, 11, 50]  # 50 已經超過 right_limit
test_data_5 = generate_test_data(times)
segments_5 = second_segmentation(
    data_list=test_data_5,
    window_size=window_size,
    left_limit=left_limit,
    right_limit=right_limit
)

show_results(segments_5, window_size, times, "test_data_5")