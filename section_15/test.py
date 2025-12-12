import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        # can be used to setup thing before each test is run
        print("about to test a function")

    def test_do_stuff(self):
        # You can use docstrings to add comments to tests. These show up with python -m unittest -v
        """
        Most important test
        """
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "jahsdlf"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        testParam = None
        result = main.do_stuff(testParam)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        testParam = ""
        result = main.do_stuff(testParam)
        self.assertEqual(result, "please enter number")

    def test_do_stuff5(self):
        testParam = 0
        result = main.do_stuff(testParam)
        self.assertEqual(result, "please enter number")

    def tearDown(self):
        # can be used to cleanup after each test: remove test variables, maybe files etc
        print('cleaning up')


if __name__ == "__main__":
    unittest.main()

# python test.py    ## Run a single tes file
# python -m unittest -v     ## Run all unittest files (verbose)
