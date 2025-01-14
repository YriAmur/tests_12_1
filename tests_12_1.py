import run
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = run.Runner("TestWalker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = run.Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = run.Runner("Runner1")
        runner_2 = run.Runner("Runner2")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()