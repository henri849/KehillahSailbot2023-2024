import unittest, tests

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromModule(tests)
	unittest.TextTestRunner(verbosity=2).run(suite)