def find_minimum_construction(source, target):
    current_index= 0
    dp = []
    dp.append(1)
    for ele in target:
        found = False
        for i in range(current_index, len(source)):
            if source[i] == ele:
                dp.append(dp[-1])
                current_index = i
                found = True
        for i in range(current_index):
            if source[i] == ele:
                dp.append(dp[-1] + 1)
                current_index = i
                found = True
        if found is False:  return -1
    return dp[-1]

if __name__ == "__main__":
    res = find_minimum_construction("abc", "abcbc")
    print(res)