from typing import List

def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    res = []

    inserted = 0 # flag
    for interval in intervals:
        print("*"*10)
        print(f"res = {res}")
        print("in interval :", interval, "inserted: ", inserted)
        if not res:
            if newInterval[0] <= interval[0]:
              res.append([newInterval[0], max(interval[1], newInterval[1])])
              inserted = 1
            else:
              res.append(interval)
            print("added first interval now continue")
            continue

        else:
          if not inserted:
            prev = res[-1]
            if newInterval[0] <= prev[1]:
              prev[1] = max(newInterval[1], prev[1])
              inserted = 1
            else:
              res.append(interval)

          else:
              print("in else")
              if inserted:
                  prev = res[-1]
                  if interval[0] <= prev[1]:
                      prev[1] = max(interval[1], prev[1])
                  else:
                      res.append(interval)
              else:
                  res.append(interval)
    print(res)
    return res


insert([[1,3],[6,9]], [2,5])




# insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])



