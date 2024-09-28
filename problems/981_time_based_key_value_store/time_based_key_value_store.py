class TimeMap:
    def __init__(self):
        self.keys = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        left, right = 0, len(self.keys[key]) - 1
        res = ""
        while left <= right:
            middle = (left + right) // 2
            currentTimestamp = self.keys[key][middle][1]
            if currentTimestamp <= timestamp:
                left = middle + 1
                res = self.keys[key][middle][0]
            else:
                right = middle - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
