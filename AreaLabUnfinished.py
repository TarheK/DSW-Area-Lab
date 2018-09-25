import math #lets us use the math module
import unittest #unnitest module helps us test small sections of code

def circleArea(radius): 
    return radius * radius *math.pi

def rectArea(base, height):
    return 1

def trapArea(base1, base2, height):
    return 1

def triArea(base,height):
    return 1
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi)
        self.assertAlmostEqual(circleArea(2), 4*math.pi) 
    def testRectArea(self):
        self.assertEqual(rectArea(10,20), 200)
        self.assertAlmostEqual(rectArea(5,7), 35)
    def testTrapArea(self):
        self.assertEqual(trapArea(5,6,2), 60)
        self.assertAlmostEqual(trapArea(3,11,2), 66)
    def testTriArea(self):
        self.assertEqual(triArea(8,7), 56)
        self.assertAlmostEqual(tritArea(3,5), 15)