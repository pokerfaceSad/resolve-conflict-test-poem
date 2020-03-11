import unittest

def get_mode(pokers_str):
    pokers_list = pokers_str.split(" ")
    
    pokers_nums_list = [ poker[0] for poker in pokers_list ]
    replace_dict = {'J':'11', 'Q':'12', 'K':'13', 'A':'1', 'T':'10'}
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
    
    
if __name__ == "__main__":
    unittest.main(verbosity=3)
    
    
    