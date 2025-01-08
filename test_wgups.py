'''
test_wgups.py
Author: Christopher Powell
Student ID: 001307071
'''

import unittest
from datetime import datetime, time
import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import our modules
from main import DeliveryService
from package import Package
from hash_table import HashTable
from truck import Truck

class TestWGUPS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment once for all tests"""
        try:
            cls.service = DeliveryService()
            cls.service.load_packages('WGUPS Package File.xlsx')
            cls.service.load_distances('WGUPS Distance Table.xlsx')
            cls.service.optimize_deliveries()
        except Exception as e:
            print(f"Setup failed: {str(e)}")
            raise

    def test_1_hash_table_basic(self):
        """Test basic hash table operations"""
        hash_table = HashTable()
        test_package = Package(1, "Test Address", "Test City", "TS", "12345", "10:30 AM", 10)
        hash_table.insert(1, test_package)
        result = hash_table.lookup(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.package_id, 1)

    def test_2_package_loading(self):
        """Test package loading and lookup"""
        # Check if package 1 was loaded correctly
        package = self.service.package_table.lookup(1)
        self.assertIsNotNone(package)
        self.assertEqual(package.address, "195 W Oakland Ave")
        self.assertEqual(package.deadline.strftime("%I:%M %p"), "10:30 AM")

    def test_3_distance_loading(self):
        """Test distance table loading"""
        # Test a known distance from the table
        distance = self.service.distance_table.get_distance(
            "4001 South 700 East",  # Hub
            "195 W Oakland Ave"
        )
        self.assertIsNotNone(distance)
        self.assertIsInstance(distance, float)

    def test_4_truck_constraints(self):
        """Test truck loading constraints"""
        for truck in self.service.trucks:
            self.assertLessEqual(len(truck.packages), 16)

    def test_5_delivery_times(self):
        """Test delivery timing requirements"""
        check_time = datetime.combine(datetime.today(), time(10, 30))
        # Check package 1 (has 10:30 AM deadline)
        status = self.service.check_package_status(1, check_time)
        self.assertIsInstance(status, dict)
        self.assertTrue(
            status['status'].startswith("Delivered") or 
            status['status'] == "En Route"
        )

    def test_6_total_mileage(self):
        """Test total mileage requirement"""
        total_mileage = self.service.get_total_mileage()
        self.assertLess(total_mileage, 140)
        print(f"\nTotal mileage: {total_mileage:.1f}")

def print_test_banner():
    print("\n" + "=" * 70)
    print("WGUPS Delivery System Tests")
    print("=" * 70 + "\n")

if __name__ == '__main__':
    print_test_banner()
    unittest.main(verbosity=2)