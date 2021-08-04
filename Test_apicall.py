import unittest
import apicall

class Testapicall(unittest.TestCase):
    def test_LookUpTicket(self):
        num = 1
        data = apicall.LookUpTicket(num)
        self.assertEqual(data['ticket']['id'], 1)
        self.assertEqual(data['ticket']['requester_id'], 1900308333544L)


if __name__ == "__main__":
    unittest.main()
