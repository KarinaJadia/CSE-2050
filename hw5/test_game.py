import unittest
import game
import maze

class TestGame(unittest.TestCase):
    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        end = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1])

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])
    
    #############################################
    # TODO - add the rest of your test cases here

    """ I couldn't get my code to work but if I did these would be the tests """

    def test_normal(self):

        # tests a normal maze
        grid = maze.Maze(3, 3)
        grid._set_maze([[5, 1,"*"],
                        [3, 2, 1],
                        [5, 1, 3,] ])
        start = (0,0)
        end = (2,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1])
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)])

    def test_no_solution(self):

        # tests a maze with no solution
        grid = maze.Maze(3, 3)
        grid._set_maze([[5, 1,"*"],
                        [3,'*', 1],
                        ['*',1, 3,] ])
        start = (0,0)
        end = (2,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score = testgame.find_route(start[0])
        self.assertEqual(score, 0) # should be zero because there is no solution
    

if __name__ == '__main__':
    unittest.main()
