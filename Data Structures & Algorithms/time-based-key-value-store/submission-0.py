class TimeMap:

    def __init__(self):
        
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.t_map:
            self.t_map[key] = []

        self.t_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.t_map:
            return ""
        
        else:
            result = ""
            req_list = self.t_map[key]

            left = 0 
            right = len(req_list) - 1

            while left <= right:

                mid = (left + right) // 2

                if req_list[mid][0] <= timestamp:

                    result = req_list[mid][1]
                    left = mid + 1
                else:

                    right = mid - 1

            return result


