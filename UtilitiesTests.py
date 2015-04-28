import unittest
import Utilities

class TestClass (unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def check_Norm(self, currentDirection, newDirection, expectedDirection):
        self.assertEqual(expectedDirection, Utilities.NormalizeDirection(currentDirection, newDirection))
        
    def test_NormalizeDirection(self):
        self.check_Norm('N' ,'N' ,'N' )
        self.check_Norm('N' ,'NE','NE' )
        self.check_Norm('N' ,'E' ,'X' )
        self.check_Norm('N' ,'SE','NW' )
        self.check_Norm('N' ,'S' ,'N' )
        self.check_Norm('N' ,'SW','NE' )
        self.check_Norm('N' ,'W' ,'X' )
        self.check_Norm('N' ,'NW','NW' )
        
        #SE
        self.check_Norm('SE' ,'N' ,'S' )
        self.check_Norm('SE' ,'NE','X') 
        self.check_Norm('SE' ,'E' ,'E' )
        self.check_Norm('SE' ,'SE','SE' )
        self.check_Norm('SE' ,'S' ,'S' )
        self.check_Norm('SE' ,'SW','X' )
        self.check_Norm('SE' ,'W' ,'E' )
        self.check_Norm('SE' ,'NW','SE' )
        
        

        
if __name__ == '__main__':
    unittest.main()
    