import logging
import unittest
import module_12_1

logging.basicConfig(level= logging.INFO,filemode='w',filename="runner_test.log",encoding="UTF-8",
                    format="%(levelname)s | %(message)s")
runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runner = unittest.TextTestRunner()
runner.run(runST)
