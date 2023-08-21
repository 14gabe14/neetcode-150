class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append((timestamp, value))
        else:
            self.dictionary[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary or timestamp < self.dictionary[key][0][0]:
            return ""
        
        if timestamp > self.dictionary[key][-1][0]:
            return self.dictionary[key][-1][1]

        l = 0
        h = len(self.dictionary[key]) - 1

        while(l < h):
            m = (l+h)//2 

            if self.dictionary[key][m][0] < timestamp:
                if timestamp < self.dictionary[key][m+1][0]:
                    return self.dictionary[key][m][1]
                l = m + 1 
                    
            elif self.dictionary[key][m][0] > timestamp:
                h = m - 1
            else:
                return self.dictionary[key][m][1]

        return self.dictionary[key][h][1]