import unittest
import Unit
import math


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
        self.assertAlmostEqual(Unit.Distance(10, 'miles').value, 16093.440000064373)
        self.assertAlmostEqual(Unit.Distance(0, 'nautical miles').value, 0)
        self.assertAlmostEqual(Unit.Distance(8, 'inches').value, 0.2032)

    def test_duration_constructor(self):
        self.assertAlmostEqual(Unit.Duration(0, 'seconds').value, 0)
        self.assertAlmostEqual(Unit.Duration(2, 'minutes').value, 120)
        self.assertAlmostEqual(Unit.Duration(9, 'seconds').value, 9)
        self.assertAlmostEqual(Unit.Duration(10.5, 'minutes').value, 630)
        self.assertAlmostEqual(Unit.Duration(0, 'seconds').value, 0)
        self.assertAlmostEqual(Unit.Duration(8, 'minutes').value, 480)
        self.assertAlmostEqual(Unit.Duration(-1, 'seconds').value, -1)

    def test_velocity_constructor(self):
        self.assertAlmostEqual(Unit.Velocity(1, 'meters/second').value, 1)
        self.assertAlmostEqual(Unit.Velocity(1, 'nautical miles/second').value, 1852)
        self.assertAlmostEqual(Unit.Velocity(3.280839895, 'feet/second').value, 1)
        self.assertAlmostEqual(Unit.Velocity(10, 'inches/second').value, 0.254)
        self.assertAlmostEqual(Unit.Velocity(10, 'cubits/minute').value, 0.0762)

    def test_measurement_comparison(self):
        self.assertTrue(Unit.Duration(0, 'seconds') == Unit.Duration(0, 'seconds'))
        self.assertRaises(AssertionError, Unit.Duration(0, 'seconds').__eq__, Unit.Angle(0, 'gradians'))  # duration - angle, eq
        self.assertRaises(AssertionError, Unit.Angle(0, 'radians').__gt__, Unit.Duration(0, 'minutes'))  # angle - duration , gt
        self.assertRaises(AssertionError, Unit.Duration(0, 'seconds').__lt__, Unit.Distance(0, 'feet'))  # duration - distance, lt
        self.assertRaises(AssertionError, Unit.Distance(0, 'cubits').__ge__, Unit.Duration(0, 'seconds'))  # distance - duration, ge
        self.assertRaises(AssertionError, Unit.Distance(0, 'miles').__le__, Unit.Angle(0, 'degrees'))  # distance - angle, le
        self.assertFalse(Unit.Distance(10, 'meters') > Unit.Distance(20, 'meters'))
        self.assertTrue(Unit.Angle(10, 'gradians') <= Unit.Angle(10, 'degrees'))
        self.assertTrue(Unit.Duration(10, 'minutes') >= Unit.Duration(10, 'seconds'))

    def test_angle_get_as(self):
        self.assertAlmostEqual(Unit.Angle(0, 'radians').get_as('radians'), 0)
        self.assertAlmostEqual(Unit.Angle(3, 'radians').get_as('radians'), 3)
        self.assertAlmostEqual(Unit.Angle(0.17453292519943295, 'radians').get_as('degrees'), 10)
        self.assertAlmostEqual(Unit.Angle(30, 'gradians').get_as('gradians'), 30)
        self.assertAlmostEqual(Unit.Angle(-1, 'radians').get_as('radians'), -1)

    def test_distance_get_as(self):
        self.assertEqual(Unit.Distance(0, 'meters').get_as('meters'), 0)
        self.assertEqual(Unit.Distance(10, 'meters').get_as('meters'), 10)
        self.assertAlmostEqual(Unit.Distance(0.6096, 'meters').get_as('feet'), 2)
        self.assertAlmostEqual(Unit.Distance(0, 'meters').get_as('meters'), 0)
        self.assertAlmostEqual(Unit.Distance(100, 'inches').get_as('meters'), 2.54)
        self.assertAlmostEqual(Unit.Distance(2.54, 'meters').get_as('inches'), 100)
        self.assertAlmostEqual(Unit.Distance(4.1148, 'meters').get_as('cubits'), 9)
        self.assertAlmostEqual(Unit.Distance(-1, 'meters').get_as('meters'), -1)

    def test_duration_get_as(self):
        self.assertEqual(Unit.Duration(0, 'seconds').get_as('seconds'), 0)
        self.assertAlmostEqual(Unit.Duration(72, 'seconds').get_as('seconds'), 72)
        self.assertEqual(Unit.Duration(60, 'seconds').get_as('minutes'), 1)
        self.assertEqual(Unit.Duration(1.5, 'minutes').get_as('seconds'), 90)
        self.assertEqual(Unit.Duration(-1, 'seconds').get_as('seconds'), -1)

    def test_mass_get_as(self):
        self.assertEqual(Unit.Mass(0, 'pounds').get_as('kilograms'), 0)
        self.assertEqual(Unit.Mass(1, 'kilograms').get_as('grams'), 1000)

    def test_global_position_constructor(self):
        self.assertEqual(Unit.GlobalPosition(Unit.Angle(0, 'degrees'), Unit.Angle(0, 'radians')),
                         Unit.GlobalPosition(Unit.Angle(0, 'gradians'), Unit.Angle(0, 'radians')))
        self.assertEqual(Unit.GlobalPosition(Unit.Angle(1, 'degrees'), Unit.Angle(0, 'radians')),
                         Unit.GlobalPosition(Unit.Angle(1, 'degrees'), Unit.Angle(0, 'radians')))

    def test_cartesian_system_constructor(self):
        self.assertEqual(Unit.CartesianSystem(Unit.GlobalPosition(Unit.Angle(2.54, 'radians'), Unit.Angle(2.54, 'radians'))),
                         Unit.CartesianSystem(Unit.GlobalPosition(Unit.Angle(2.54, 'radians'), Unit.Angle(2.54, 'radians'))))

    def test_relative_position_constructor(self):
        sys = Unit.CartesianSystem(Unit.GlobalPosition(Unit.Angle(0, 'radians'), Unit.Angle(0, 'gradians')))
        self.assertEqual(Unit.RelativePosition(sys, Unit.Distance(2, 'meters'), Unit.Distance(0, 'cubits')),
                         Unit.RelativePosition(sys, Unit.Distance(2, 'meters'), Unit.Distance(0, 'nautical miles')))

    def test_cartesian_system_point(self):
        sys = Unit.CartesianSystem(Unit.GlobalPosition(Unit.Angle(0, 'radians'), Unit.Angle(0, 'gradians')))
        self.assertEqual(sys.point(Unit.Distance(0, 'cubits'), Unit.Distance(3, 'meters')),
                         sys.point(Unit.Distance(0, 'cubits'), Unit.Distance(3, 'meters')))

    def test_relative_position_distance_to(self):
        sys = Unit.CartesianSystem(Unit.GlobalPosition(Unit.Angle(0, 'radians'), Unit.Angle(0, 'gradians')))
        p1 = sys.point(Unit.Distance(1, 'meters'), Unit.Distance(1, 'meters'))
        p2 = sys.point(Unit.Distance(0, 'meters'), Unit.Distance(0, 'meters'))
        self.assertAlmostEqual(p1.distance_to(p2).value, math.sqrt(2))

    def test_measurement_arithmetic_operators(self):
        self.assertEqual((Unit.Distance(1, "meters") + Unit.Distance(1, "meters")).get_as("meters"), 2)
        self.assertEqual((Unit.Duration(20, "seconds") + Unit.Duration(40, "seconds")).get_as("minutes"), 1)
        self.assertAlmostEqual((Unit.Angle(5, "radians") + Unit.Angle(2, "radians")).get_as("radians"), 7)
        self.assertEqual((Unit.Distance(1, "meters") + Unit.Distance(1, "meters") + Unit.Distance(1, "meters")).get_as("meters"), 3)
        self.assertEqual((Unit.Distance(1, "meters") - Unit.Distance(1, "meters")).get_as("meters"), 0)
        self.assertEqual((Unit.Duration(20, "seconds") - Unit.Duration(40, "seconds")).get_as("seconds"), -20)
        self.assertAlmostEqual((Unit.Angle(5, "radians") - Unit.Angle(2, "radians")).get_as("radians"), 3)
        self.assertEqual((Unit.Distance(1, "meters") - Unit.Distance(1, "meters") + Unit.Distance(1, "meters")).get_as("meters"), 1)


if __name__ == "__main__":
    unittest.main()