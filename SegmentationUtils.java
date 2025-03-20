import java.util.ArrayList;
import java.util.List;

public class SegmentationUtils {
    public static class Data {
        private int time;
        private boolean state;

        public Data(int time, boolean state) {
            this.time = time;
            this.state = state;
        }

        public int getTime() {
            return time;
        }

        public boolean isState() {
            return state;
        }
    }

    public static List<List<Data>> windowSegmentation(
            List<Data> dataList,
            int windowSize,
            int leftLimit,
            int rightLimit
    ) {
        // 基本條件檢查
        if (dataList == null || dataList.isEmpty() || windowSize <= 0 || rightLimit <= leftLimit) {
            return new ArrayList<>();  // 回傳空的清單
        }

        List<List<Data>> segments = new ArrayList<>();
        int n = dataList.size();
        int i = 0;

        // 略過小於 leftLimit 的資料
        while (i < n && dataList.get(i).getTime() < leftLimit) {
            i++;
        }

        // 以 leftLimit 為起點開始分段
        int tStart = leftLimit;

        while (tStart < rightLimit) {
            int tEnd = tStart + windowSize;
            if (tEnd > rightLimit) {
                tEnd = rightLimit; // 最後一段不足 windowSize 時截斷
            }

            List<Data> segment = new ArrayList<>();
            // 收集 [tStart, tEnd) 內的資料
            while (i < n && dataList.get(i).getTime() < tEnd) {
                // 因為前面已略過 time < leftLimit 的資料，
                // 所以這裡理論上都 >= tStart
                segment.add(dataList.get(i));
                i++;
            }
            segments.add(segment);

            tStart += windowSize;
        }

        return segments;
    }
    
    // 後面再放 secondSegmentation
    public static List<List<Data>> secondSegmentation(
        List<Data> dataList,
        int second,
        int leftLimit,
        int rightLimit
    ) {
        // 檢查基本條件
        if (dataList == null || dataList.isEmpty() || second <= 0 || rightLimit <= leftLimit) {
            return new ArrayList<>();
        }

        List<List<Data>> segments = new ArrayList<>();
        int n = dataList.size();
        int i = 0;

        // 略過小於 leftLimit 的資料（不納入任何 segment）
        while (i < n && dataList.get(i).getTime() < leftLimit) {
            i++;
        }

        // 只要還有資料，就繼續切 segment
        while (i < n) {
            int tStart = dataList.get(i).getTime();

            // 若新的 tStart 已超過 rightLimit，就不再切割
            if (tStart >= rightLimit) {
                break;
            }

            // 計算此段的結束時間
            int tEnd = tStart + second;
            if (tEnd > rightLimit) {
                tEnd = rightLimit; // 不足 second 時，截到 rightLimit
            }

            List<Data> segment = new ArrayList<>();
            // 收集 [tStart, tEnd) 內的資料
            while (i < n && dataList.get(i).getTime() < tEnd) {
                segment.add(dataList.get(i));
                i++;
            }

            segments.add(segment);
        }

        return segments;
    }
    
}
