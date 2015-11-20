import unittest, hw1

class APITest(unittest.TestCase):
	def testOne(self):
		res = hw1.APIcall()
		self.assertEqual(len(res),2)
		assert res[0] != None
		assert res[1] != None

def main():
	unittest.main()

if __name__ == '__main__':
	main()