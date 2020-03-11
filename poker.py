import unittest

class poker_test(unittest.TestCase):
    def setUp(self):
        print("Test Start...")
    
    def tearDown(self):
        print("Teast End...")

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
    def test_get_mode_4(self):
        # 同花 6
        self.assertEqual(get_mode("2H 8H 4H 5H 6H"), 6)
    
    # 判断手牌的模式
    def test_get_mode_4(self):
        # 葫芦 7
        self.assertEqual(get_mode("2H 2D 2S 3C 3D"), 7)
    
    # 判断手牌的模式
    def test_get_mode_4(self):
        # 铁枝 8
        self.assertEqual(get_mode("2H 2D 2S 2C 3D"), 8)
    
    # 判断手牌的模式
    def test_get_mode_4(self):
        # 同花顺 9
        self.assertEqual(get_mode("2D 3D 4D 5D 6D"), 9)
    
    
    
    
    
    