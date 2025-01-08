# truck.py
# Author: Christopher Powell
# Student ID: 001307071

from datetime import datetime, timedelta
from typing import List, Optional, Dict, Set
from package import Package

class TruckError(Exception):
    """Custom exception for truck-related errors"""
    pass

class Truck:
    """Truck class for WGUPS delivery management"""
    
    def __init__(self, truck_id: int, capacity: int = 16, speed: float = 18.0):
        if capacity < 1:
            raise TruckError("Capacity must be positive")
        if speed <= 0:
            raise TruckError("Speed must be positive")
            
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.packages: List[Package] = []
        self.mileage = 0.0
        self.current_location = "HUB"
        self.start_time: Optional[datetime] = None
        self.current_time: Optional[datetime] = None
        self.route: List[str] = []
        self.delivered_packages: Set[int] = set()

    def load_packages(self, package_list: List[Package], start_time: datetime) -> bool:
        """Load packages onto truck with constraint checking"""
        if len(package_list) > self.capacity:
            raise TruckError("Cannot exceed truck capacity")
            
        # Verify package constraints
        self._verify_package_constraints(package_list)
        
        # Load packages
        self.packages = package_list
        self.start_time = start_time
        self.current_time = start_time
        
        # Update package statuses
        for package in self.packages:
            package.update_status("En Route", start_time)
            package.truck = self.truck_id
            
        return True

    def _verify_package_constraints(self, packages: List[Package]) -> None:
        """Verify all package delivery constraints are met"""
        package_ids = {p.package_id for p in packages}
        
        # Check packages that must be delivered together
        grouped_packages = {13, 14, 15, 16, 19, 20}
        if any(pid in package_ids for pid in grouped_packages):
            if not grouped_packages.issubset(package_ids):
                raise TruckError("Packages 13, 14, 15, 16, 19, 20 must be delivered together")
                
        # Check truck 2 only packages
        truck2_only = {3, 18, 36, 38}
        if any(pid in package_ids for pid in truck2_only) and self.truck_id != 2:
            raise TruckError("Packages 3, 18, 36, 38 can only be on truck 2")
            
        # Check delayed packages
        delayed_packages = {6, 25, 28, 32}
        if any(pid in package_ids for pid in delayed_packages):
            if self.start_time.time() < datetime.strptime("9:05 AM", "%I:%M %p").time():
                raise TruckError("Delayed packages cannot leave before 9:05 AM")

    def optimize_route(self, distance_matrix: Dict[str, Dict[str, float]]) -> None:
        """Optimize delivery route using nearest neighbor algorithm"""
        if not self.packages:
            return
            
        unvisited = self.packages.copy()
        current_loc = self.current_location
        optimized_route = []
        
        while unvisited:
            next_package = min(unvisited, 
                key=lambda p: distance_matrix[current_loc][p.address])
            optimized_route.append(next_package)
            current_loc = next_package.address
            unvisited.remove(next_package)
            
        self.packages = optimized_route
        self.route = [p.address for p in optimized_route]

    def deliver_package(self, package: Package, distance: float) -> datetime:
        """Deliver a package and update truck status"""
        if package not in self.packages:
            raise TruckError("Package not on truck")
            
        self.mileage += distance
        travel_time = timedelta(hours=distance/self.speed)
        delivery_time = self.current_time + travel_time
        
        self.packages.remove(package)
        self.delivered_packages.add(package.package_id)
        self.current_time = delivery_time
        self.current_location = package.address
        
        return delivery_time

    def return_to_hub(self, distance: float) -> None:
        """Return truck to hub"""
        self.mileage += distance
        travel_time = timedelta(hours=distance/self.speed)
        self.current_time += travel_time
        self.current_location = "HUB"
        self.route.append("HUB")

    def get_status(self) -> dict:
        """Get current truck status"""
        return {
            'truck_id': self.truck_id,
            'packages_remaining': len(self.packages),
            'packages_delivered': len(self.delivered_packages),
            'current_location': self.current_location,
            'mileage': round(self.mileage, 1),
            'current_time': self.current_time.strftime("%I:%M %p") if self.current_time else "Not Started"
        }

    def __str__(self) -> str:
        return (f"Truck {self.truck_id}: {len(self.packages)} packages remaining, "
                f"{self.mileage:.1f} miles traveled")