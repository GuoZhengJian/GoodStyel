# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

# =============================================================================
# import unittest
# 
# class Unittest_demo(unittest.TestCase):
#     def setUp(self):
#         Demo_methods = ['back_str', 'back_nums', 'back_list',]
#         for method in Demo_methods:
#             if not hasattr(Demo, method):
#                 raise AttributeError('%s Not Found' % method) 
#     
#     def tearDown(self):
#         pass
#     
#     def test_back_str(self):
#         self.assertIs(Demo('Hello Word').back_str(), 'Hello Word')
#     
#     def test_back_nums(self):
#         for num in range(5):
#             self.assertEqual(Demo(num).back_nums(), num)
#     
#     def test_back_list(self):
#         self.assertEqual(Demo(5).back_list(), [0, 1, 2, 3, 4])
#             
#         with self.assertRaisesRegex(ValueError, 'number must be > 10'):
#             Demo(20).back_list()
#         
# if __name__ == '__main__':
#     unittest.main()
# =============================================================================
    

# =============================================================================
# # doctest demo
# if __name__ == '__main__':
#     import Unit
#     import doctest
#     doctest.testmod(Unit)
#     
#     import doctest
#     doctest.testfile('TestUnit.txt')
# =============================================================================
