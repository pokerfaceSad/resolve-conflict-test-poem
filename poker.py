import unittest

# 比较手牌大小
def compare(poker_str1, poker_str2):
    value_list1 = get_value(poker_str1)
    value_list2 = get_value(poker_str2)
    # print('value_list1: ' + str(value_list1))
    # print('value_list2: ' + str(value_list2))
    if value_list1[0] == value_list2[0]:
        for (val1, val2) in zip(value_list1, value_list2):
            if val1 > val2:
                return 1
            elif val1 < val2:
                return 2
        return 0
    elif value_list1[0] > value_list2[0]:
        return 1
    else:
        return 2

# 判断手牌模式
def get_mode(pokers_str):
    pokers_list = pokers_str.split(" ")
    
    pokers_nums_list = [ poker[0] for poker in pokers_list ]
    replace_dict = {'J':'11', 'Q':'12', 'K':'13', 'A':'14', 'T':'10'}
    pokers_nums_list = [ replace_dict[poker_num] if poker_num in replace_dict else poker_num for poker_num in pokers_nums_list ]
    pokers_nums_list = [int(poker_num) for poker_num in pokers_nums_list]
    
    pokers_suits_list = [ poker[1] for poker in pokers_list ]
    
    len_pokers_nums_set = len(set(pokers_nums_list))
    len_pokers_suits_set = len(set(pokers_suits_list))
    
    # print("pokers_nums_list:")
    # print(pokers_nums_list)
    # print("pokers_suits_list")
    # print(pokers_suits_list)
    # print("pokers_nums_set")
    # print(set(pokers_nums_list))
    # print("pokers_nums_set")
    # print(set(pokers_suits_list))

    # 同花顺 9
    if len_pokers_suits_set == 1 and \
       len_pokers_nums_set == len(pokers_nums_list) and \
       max(pokers_nums_list) - min(pokers_nums_list) == len(pokers_nums_list) - 1:
        return 9
    
    # 铁枝 8
    if max([pokers_nums_list.count(poker_num) for poker_num in pokers_nums_list]) == 4:
        return 8
    
    # 葫芦 7
    if len_pokers_nums_set == 2 and max([pokers_nums_list.count(poker_num) for poker_num in pokers_nums_list]) == 3:
        return 7
    
    # 同花 6
    if len_pokers_suits_set == 1:
        return 6
    
    # 顺子 5
    if len_pokers_nums_set == len(pokers_nums_list) and \
       max(pokers_nums_list) - min(pokers_nums_list) == len(pokers_nums_list) - 1:
        return 5

    # 三条 4
    if max([pokers_nums_list.count(poker_num) for poker_num in pokers_nums_list]) == 3:
        return 4
    
    # 两对 3
    if len_pokers_nums_set == 3 and max([pokers_nums_list.count(poker_num) for poker_num in pokers_nums_list]) == 2:
        return 3
    
    # 对子 2
    if max([pokers_nums_list.count(poker_num) for poker_num in pokers_nums_list]) == 2:
        return 2
    
    # 散牌
    return 1

# 获取手牌大小
def get_value(pokers_str):
    pokers_list = pokers_str.split(" ")
    
    pokers_nums_list = [ poker[0] for poker in pokers_list ]
    replace_dict = {'J':'11', 'Q':'12', 'K':'13', 'A':'14', 'T':'10'}
    pokers_nums_list = [ replace_dict[poker_num] if poker_num in replace_dict else poker_num for poker_num in pokers_nums_list ]
    pokers_nums_list = [int(poker_num) for poker_num in pokers_nums_list]
    
    pokers_suits_list = [ poker[1] for poker in pokers_list ]
    
    len_pokers_nums_set = len(set(pokers_nums_list))
    len_pokers_suits_set = len(set(pokers_suits_list))

    mode = get_mode(pokers_str)
    
    # 同花顺
    if mode == 9:
        max_num = max(pokers_nums_list)
        return [9, max_num]
    # 铁枝
    if mode == 8:
        for num in pokers_nums_list:
            if pokers_nums_list.count(num) == 4:
                return [8, num]
    # 葫芦
    if mode == 7:
        for num in pokers_nums_list:
            if pokers_nums_list.count(num) == 3:
                return [7, num]   
    # 同花
    if mode == 6:
        result = [6]
        result.extend(sorted(pokers_nums_list, reverse=True))
        return result
    # 顺子
    if mode == 5:
        max_num = max(pokers_nums_list)
        return [5, max_num]
    # 三条
    if mode == 4:
        for num in pokers_nums_list:
            if pokers_nums_list.count(num) == 3:
                return [4, num] 
    # 两对
    if mode == 3:
        double_nums_list = []
        single_num = None
        for num in pokers_nums_list:
            if pokers_nums_list.count(num) == 2 and num not in double_nums_list:
                double_nums_list.append(num)
            elif pokers_nums_list.count(num) == 1:
                single_num = num
        double_nums_list.sort(reverse=True)
        result = [3]
        result.extend(double_nums_list)
        result.append(single_num)
        return result
    # 对子
    if mode == 2:
        double_num = None
        single_nums_list = []
        for num in pokers_nums_list:
            if pokers_nums_list.count(num) == 2:
                double_num = num
            elif pokers_nums_list.count(num) == 1:
                single_nums_list.append(num)
        single_nums_list.sort(reverse=True)
        result = [2]
        result.append(double_num)
        result.extend(single_nums_list)
        return result
    # 散牌
    if mode==1:
        result = [1]
        result.extend(sorted(pokers_nums_list, reverse=True))
        return result

class poker_test(unittest.TestCase):
    def setUp(self):
        print("Test Start...")
    
    def tearDown(self):
        print("Test End...")

    # 判断手牌的模式
    def test_get_mode_1(self):
        # 散牌 1
        self.assertEqual(get_mode("2H 3D 5S 9C KD"), 1)
        
    # 判断手牌的模式
    def test_get_mode_2(self):
        # 对子 2
        self.assertEqual(get_mode("2H 2D 5S 9C KD"), 2)
    
    # 判断手牌的模式
    def test_get_mode_3(self):
        # 两对 3
        self.assertEqual(get_mode("2H 2D 5S 5C KD"), 3)
    
    # 判断手牌的模式
    def test_get_mode_4(self):
        # 三条 4
        self.assertEqual(get_mode("2H 2D 2S 5C KD"), 4)
    
    # 判断手牌的模式
    def test_get_mode_5(self):
        # 顺子 5
        self.assertEqual(get_mode("2H 3D 4S 5C 6D"), 5)
    
    # 判断手牌的模式
    def test_get_mode_6(self):
        # 同花 6
        self.assertEqual(get_mode("2H 8H 4H 5H 6H"), 6)
    
    # 判断手牌的模式
    def test_get_mode_7(self):
        # 葫芦 7
        self.assertEqual(get_mode("2H 2D 2S 3C 3D"), 7)
    
    # 判断手牌的模式
    def test_get_mode_8(self):
        # 铁枝 8
        self.assertEqual(get_mode("2H 2D 2S 2C 3D"), 8)
    
    # 判断手牌的模式
    def test_get_mode_9(self):
        # 同花顺 9
        self.assertEqual(get_mode("2D 3D 4D 5D 6D"), 9)
    
    # 获取手牌大小
    def test_get_value_1(self):
        # 散牌 1
        self.assertEqual(get_value("2H 3D 5S 9C KD"), [1, 13, 9, 5, 3, 2])
    
    # 获取手牌大小
    def test_get_value_2(self):
        # 对子 2
        self.assertEqual(get_value("2H 2D 5S 9C KD"), [2, 2, 13, 9, 5])
    
    # 获取手牌大小
    def test_get_value_3(self):
        # 两对 3
        self.assertEqual(get_value("2H 2D 5S 5C KD"), [3, 5, 2, 13])
    
    # 获取手牌大小
    def test_get_value_4(self):
        # 三条 4
        self.assertEqual(get_value("2H 2D 2S 5C KD"), [4, 2])
    
    # 获取手牌大小
    def test_get_value_5(self):
        # 顺子 5
        self.assertEqual(get_value("2H 3D 4S 5C 6D"), [5, 6])
    
    # 获取手牌大小
    def test_get_value_6(self):
        # 同花 6
        self.assertEqual(get_value("2H 8H 4H 5H 6H"), [6, 8, 6, 5, 4, 2])
    
    # 获取手牌大小
    def test_get_value_7(self):
        # 葫芦 7
        self.assertEqual(get_value("2H 2D 2S 3C 3D"), [7, 2])
    
    # 获取手牌大小
    def test_get_value_8(self):
        # 铁枝 8
        self.assertEqual(get_value("2H 2D 2S 2C 3D"), [8, 2])
    
    # 获取手牌大小
    def test_get_value_9(self):
        # 同花顺 9
        self.assertEqual(get_value("TH JH QH KH AH"), [9, 14])
    
    # 比较手牌大小
    def test_compare_1(self):
        self.assertEqual(compare("TH JH QH KH AH", "2H 2D 2S 2C 3D"), 1)
    
    # 比较手牌大小
    def test_compare_2(self):
        self.assertEqual(compare("TH JH QH KH AH", "TD JD QD KD AD"), 0)
    
    # 比较手牌大小
    def test_compare_3(self):
        self.assertEqual(compare("2H 2D 2S 2C 3D", "3H 3D 3S 3C AD"), 2)
    
    
if __name__ == "__main__":
    unittest.main(verbosity=3)
    
    
    