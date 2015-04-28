import unittest
import GameState
import Map
import Train

class TestClass (unittest.TestCase):
    def setUp(self):
        self.gs = GameState.GameState()
        
    def tearDown(self):
        pass
        
    def splitTrainTestSetup(self):
        train = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train.Speed = 1.5 # Both segments of a split train should have the same speed        
        train.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        train.AppendCar(Train.TrainCar("Boxcar3", 'B', None, 7, 5, 'E', None))
        train.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 6, 5, 'E', None))        
        self.gs.AppendTrain(train)
        return train
    
    def test_SplitTrainAfterCar_Middle(self):
        train = self.splitTrainTestSetup()
        
        frontTrain, rearTrain = self.gs.SplitTrainAfterCar(train, 1)
        
        self.assertIsNotNone(frontTrain, "Front Train is None")
        self.assertEqual(2, len(frontTrain.Cars), "Front Train should have two cars")
        self.assertEqual("Boxcar1", frontTrain.Cars[0].Name)
        self.assertEqual("Boxcar2", frontTrain.Cars[1].Name)
        self.assertEqual(frontTrain, frontTrain.Cars[0].ParentTrain)
        self.assertEqual(frontTrain, frontTrain.Cars[1].ParentTrain)
        self.assertEqual(1.5, frontTrain.Speed)
                
        self.assertIsNotNone(rearTrain, "Rear Train is None")
        self.assertEqual(2, len(rearTrain.Cars), "Rear Train should have two cars")
        self.assertEqual("Boxcar3", rearTrain.Cars[0].Name)
        self.assertEqual("Boxcar4", rearTrain.Cars[1].Name)
        self.assertEqual(rearTrain, rearTrain.Cars[0].ParentTrain)
        self.assertEqual(rearTrain, rearTrain.Cars[1].ParentTrain)
        self.assertEqual(1.5, rearTrain.Speed)
        
    def test_SplitTrainAfterCar_End(self):
        train = self.splitTrainTestSetup()
        
        frontTrain, rearTrain = self.gs.SplitTrainAfterCar(train, 4)
        self.assertIsNotNone(frontTrain, "Front Train is None")
        self.assertIsNone(rearTrain, "Rear Train should be None")
        
    def test_SplitTrainAfterCar_Front(self):
        train = self.splitTrainTestSetup()
        
        frontTrain, rearTrain = self.gs.SplitTrainAfterCar(train, -1)
        self.assertIsNone(frontTrain, "Front Train should be None")
        self.assertIsNotNone(rearTrain, "Rear Train is None")

        
    def test_MergeTrains_Trailing(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 5, 'E', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 6, 5, 'E', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertEqual(train1, mergedTrain, "Merge should have returned train1")
        self.assertEqual(4, len(mergedTrain.Cars), "Merged train should have all cars")
        self.assertEqual(0, len(train2.Cars), "'Victim' train should be empty")
        self.assertEqual("Boxcar1", mergedTrain.Cars[0].Name, "Wrong car name/order")
        self.assertEqual("Boxcar2", mergedTrain.Cars[1].Name, "Wrong car name/order")
        self.assertEqual("Boxcar3", mergedTrain.Cars[2].Name, "Wrong car name/order")
        self.assertEqual("Boxcar4", mergedTrain.Cars[3].Name, "Wrong car name/order")
        
    def test_MergeTrains_HeadOn(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 10, 5, 'W', None))
        train2.Speed = 0.5
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 11, 5, 'W', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertEqual(train1, mergedTrain, "Merge should have returned train1")
        self.assertEqual(4, len(mergedTrain.Cars), "Merged train should have all cars")
        self.assertEqual(0, len(train2.Cars), "'Victim' train should be empty")
        self.assertEqual("Boxcar4", mergedTrain.Cars[0].Name, "Wrong car name/order")
        self.assertEqual("Boxcar3", mergedTrain.Cars[1].Name, "Wrong car name/order")
        self.assertEqual("Boxcar1", mergedTrain.Cars[2].Name, "Wrong car name/order")
        self.assertEqual("Boxcar2", mergedTrain.Cars[3].Name, "Wrong car name/order")
        
    def test_MergeTrains_MovingAway(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 6, 5, 'W', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 5, 'W', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertEqual(train1, mergedTrain, "Merge should have returned train1")
        self.assertEqual(4, len(mergedTrain.Cars), "Merged train should have all cars")
        self.assertEqual(0, len(train2.Cars), "'Victim' train should be empty")
        self.assertEqual("Boxcar1", mergedTrain.Cars[0].Name, "Wrong car name/order")
        self.assertEqual("Boxcar2", mergedTrain.Cars[1].Name, "Wrong car name/order")
        self.assertEqual("Boxcar4", mergedTrain.Cars[2].Name, "Wrong car name/order")
        self.assertEqual("Boxcar3", mergedTrain.Cars[3].Name, "Wrong car name/order")
        
    def test_MergeTrains_TrailingAngle(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 6, 'NE', None))
        train2.Speed = 0.5
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 6, 7, 'NE', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertEqual(train1, mergedTrain, "Merge should have returned train1")
        self.assertEqual(4, len(mergedTrain.Cars), "Merged train should have all cars")
        self.assertEqual(0, len(train2.Cars), "'Victim' train should be empty")
        self.assertEqual("Boxcar1", mergedTrain.Cars[0].Name, "Wrong car name/order")
        self.assertEqual("Boxcar2", mergedTrain.Cars[1].Name, "Wrong car name/order")
        self.assertEqual("Boxcar3", mergedTrain.Cars[2].Name, "Wrong car name/order")
        self.assertEqual("Boxcar4", mergedTrain.Cars[3].Name, "Wrong car name/order")
        
    def test_MergeTrains_Trailing90Degree(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'NE', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 6, 'N', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 7, 'NW', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertEqual(train1, mergedTrain, "Merge should have returned train1")
        self.assertEqual(4, len(mergedTrain.Cars), "Merged train should have all cars")
        self.assertEqual(0, len(train2.Cars), "'Victim' train should be empty")
        self.assertEqual("Boxcar1", mergedTrain.Cars[0].Name, "Wrong car name/order")
        self.assertEqual("Boxcar2", mergedTrain.Cars[1].Name, "Wrong car name/order")
        self.assertEqual("Boxcar3", mergedTrain.Cars[2].Name, "Wrong car name/order")
        self.assertEqual("Boxcar4", mergedTrain.Cars[3].Name, "Wrong car name/order")
        
    def test_MergeTrains_NotConnected(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 6, 5, 'E', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 5, 5, 'E', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertIsNone(mergedTrain)
        
    def test_MergeTrains_WrongOrientation(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 6, 'N', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 7, 'NE', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertIsNone(mergedTrain)
        
    # This one is important because it tests that the front/back car can only connect in
    # one direction, not both.
    def test_MergeTrains_CrossingTheT(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        train1.AppendCar(Train.TrainCar("Boxcar3", 'B', None, 7, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar4", 'B', None, 8, 6, 'NE', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar5", 'B', None, 8, 7, 'E', None))
        self.gs.AppendTrain(train2)
        
        mergedTrain = self.gs.MergeTrains(train1, train2)
        self.assertIsNone(mergedTrain)
    
    
        
        
    def test_CanTrainsMerge_UnadjacentTrains(self):    
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 6, 6, 'N', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 6, 7, 'N', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNone(car1, "Trains should not be able to merge")
        self.assertIsNone(car2, "Trains should not be able to merge")
        
    def test_CanTrainsMerge_WrongDirections(self):        
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 6, 'N', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 7, 'N', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNone(car1, "Trains should not be able to merge")
        self.assertIsNone(car2, "Trains should not be able to merge")
        
    def test_CanTrainsMerge_AdjacentCarsNotOnEnd(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 4, 'NE', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 5, 'N', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNone(car1, "Trains should not be able to merge")
        self.assertIsNone(car2, "Trains should not be able to merge")
        
    def test_CanTrainsMerge_SameDirection(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 7, 6, 'NE', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 7, 'N', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNotNone(car1, "Trains should be able to merge")
        self.assertIsNotNone(car2, "Trains should be able to merge")
        
    def test_CanTrainsMerge_OppositeDirection(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar3", 'B', None, 6, 5, 'W', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar4", 'B', None, 7, 5, 'W', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNotNone(car1, "Trains should be able to merge")
        self.assertIsNotNone(car2, "Trains should be able to merge")
        
        

    # This one is important because it tests that the front/back car can only connect in
    # one direction, not both.
    def test_CanTrainsMerge_CrossingTheT(self):
        train1 = Train.Train(Train.TrainCar("Boxcar1", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.5        
        train1.AppendCar(Train.TrainCar("Boxcar2", 'B', None, 8, 5, 'E', None))
        train1.AppendCar(Train.TrainCar("Boxcar3", 'B', None, 7, 5, 'E', None))
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar4", 'B', None, 8, 6, 'NE', None))
        train2.Speed = 0.5        
        train2.AppendCar(Train.TrainCar("Boxcar5", 'B', None, 8, 7, 'E', None))
        self.gs.AppendTrain(train2)
        
        car1, car2 = self.gs.CanTrainsMerge(train1, train2)
        self.assertIsNone(car1)
        self.assertIsNone(car2)
    
    def createTestCars(self, x1, y1, d1, x2, y2, d2):
        return (Train.TrainCar("Car", 'C', None, x1, y1, d1, None), 
            Train.TrainCar("Car", 'C', None, x2, y2, d2, None)
        )
        
    def check_CarInValidDirection(self, x1, y1, d1, x2, y2, d2, expectedResult):
        car1, car2 = self.createTestCars(x1, y1, d1, x2, y2, d2)
        result = GameState.CarInValidDirection(car1, d1, car2)
        self.assertEqual(expectedResult, result, "Incorrect result from CarInValidDirection")
    
    # This only tests that one car is in the correct orientationt to connect to another,
    # regardless of that car's orientation
    def test_CarInValidDirection(self):
        self.check_CarInValidDirection(10, 10, 'N' , 10, 9, 'S', True)
        
        self.check_CarInValidDirection(10, 10, 'N' , 10, 9, 'E', True)
        self.check_CarInValidDirection(10, 10, 'NE', 10, 9, 'E', True)
        self.check_CarInValidDirection(10, 10, 'E' , 10, 9, 'E', False)
        self.check_CarInValidDirection(10, 10, 'SE', 10, 9, 'E', False)
        self.check_CarInValidDirection(10, 10, 'S' , 10, 9, 'E', False)
        self.check_CarInValidDirection(10, 10, 'SW', 10, 9, 'E', False)
        self.check_CarInValidDirection(10, 10, 'W' , 10, 9, 'E', False)
        self.check_CarInValidDirection(10, 10, 'NW', 10, 9, 'E', True)
        
        self.check_CarInValidDirection(10, 10, 'N' , 11, 11, 'E', False)
        self.check_CarInValidDirection(10, 10, 'NE', 11, 11, 'E', False)
        self.check_CarInValidDirection(10, 10, 'E' , 11, 11, 'E', True)
        self.check_CarInValidDirection(10, 10, 'SE', 11, 11, 'E', True)
        self.check_CarInValidDirection(10, 10, 'S' , 11, 11, 'E', True)
        self.check_CarInValidDirection(10, 10, 'SW', 11, 11, 'E', False)
        self.check_CarInValidDirection(10, 10, 'W' , 11, 11, 'E', False)
        self.check_CarInValidDirection(10, 10, 'NW', 11, 11, 'E', False)
        
    def check_AreCarsCorrectlyOriented(self, x1, y1, d1, x2, y2, d2, expectedResult):
        car1, car2 = self.createTestCars(x1, y1, d1, x2, y2, d2)
        result = GameState.AreCarsCorrectlyOriented(car1, car1.Direction, car2, car2.Direction)
        self.assertEqual(expectedResult, result, "Incorrect result from AreCarsCorrectlyOriented")

    def test_AreCarsCorrectlyOriented(self):
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 10, 8, 'S', False)
        
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'N' , False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'NE', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'E' , False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'SE', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'S' , False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'SW', True)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'W' , False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 9, 'NW', False)
        
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'NE', 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'E' , 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'SE', 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'S' , 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'SW', 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'W' , 10, 9, 'E', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'NW', 10, 9, 'E', False)
        
        self.check_AreCarsCorrectlyOriented(10, 10, 'N' , 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'NE', 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'E' , 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'SE', 11, 11, 'W', True)
        self.check_AreCarsCorrectlyOriented(10, 10, 'S' , 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'SW', 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'W' , 11, 11, 'W', False)
        self.check_AreCarsCorrectlyOriented(10, 10, 'NW', 11, 11, 'W', False)
    

    def test_CreateMovementTurns(self):
        train1 = Train.Train(Train.TrainCar("Boxcar", 'B', None, 9, 5, 'E', None))
        train1.Speed = 1.6                
        self.gs.AppendTrain(train1)
                
        train2 = Train.Train(Train.TrainCar("Boxcar", 'B', None, 6, 5, 'W', None))
        train2.Speed = 1.4
        self.gs.AppendTrain(train2)
        
        train3 = Train.Train(Train.TrainCar("Boxcar", 'B', None, 10, 10, 'S', None))
        train3.Speed = -2.6
        self.gs.AppendTrain(train3)
        
        mt = self.gs.CreateMovementTurns()
        
        self.assertEqual(3, len(mt))
        
        t = mt[0]
        self.assertEqual(3, len(t.Trains), "Expected 3 trains in turn 0")
        self.assertIs(train1, t.Trains[0])
        self.assertIs(train2, t.Trains[1])
        self.assertIs(train3, t.Trains[2])
        
        t = mt[1]
        self.assertEqual(2, len(t.Trains), "Expected 2 trains in turn 1")
        self.assertIs(train1, t.Trains[0])
        self.assertIs(train3, t.Trains[1])
        
        t = mt[2]
        self.assertEqual(1, len(t.Trains), "Expected 1 train in turn 2")
        self.assertIs(train3, t.Trains[0])
        
        
                
    #def test_CheckForCollision(self):
        
    
        
if __name__ == '__main__':
    unittest.main()
    