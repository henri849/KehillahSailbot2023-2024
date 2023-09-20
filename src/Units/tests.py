import unittest
import Unit


class Testing(unittest.TestCase):
    def test_angle_constructor(self):
        self.assertAlmostEqual(Unit.Angle(0, 'radians').value, 0)
        self.assertAlmostEqual(Unit.Angle(2, 'radians').value, 2)
        self.assertAlmostEqual(Unit.Angle(9, 'radians').value, 9)
        self.assertAlmostEqual(Unit.Angle(10, 'degrees').value, 0.17453292519943295)
        self.assertAlmostEqual(Unit.Angle(0, 'degrees').value, 0)
        self.assertAlmostEqual(Unit.Angle(8, 'gradians').value, 0.12566370614359174)
        self.assertAlmostEqual(Unit.Angle(-1, 'radians').value, -1)

    def test_distance_constructor(self):
        self.assertAlmostEqual(Unit.Distance(0, 'meters').value, 0)
        self.assertAlmostEqual(Unit.Distance(2, 'feet').value, 0.6096)
        self.assertAlmostEqual(Unit.Distance(9, 'cubits').value, 4.1148)
        self.assertAlmostEqual(Unit.Distance(10, 'inches').value, 0.254)
        self.assertAlmostEqual(Unit.Distance(0, 'inches').value, 0)
        self.assertAlmostEqual(Unit.Distance(8, 'inches').value, 0.2032)
        self.assertAlmostEqual(Unit.Distance(-1, 'meters').value, -1)

    def test_duration_constructor(self):
        self.assertAlmostEqual(Unit.Duration(0, 'seconds').value, 0)
        self.assertAlmostEqual(Unit.Duration(2, 'minutes').value, 120)
        self.assertAlmostEqual(Unit.Duration(9, 'seconds').value, 9)
        self.assertAlmostEqual(Unit.Duration(10.5, 'minutes').value, 630)
        self.assertAlmostEqual(Unit.Duration(0, 'seconds').value, 0)
        self.assertAlmostEqual(Unit.Duration(8, 'minutes').value, 480)
        self.assertAlmostEqual(Unit.Duration(-1, 'seconds').value, -1)

if __name__ == "__main__":
    unittest.main()
