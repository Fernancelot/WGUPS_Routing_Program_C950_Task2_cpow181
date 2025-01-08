# package.py
# Author: Christopher Powell
# Student ID: 001307071

from datetime import datetime, time
from typing import Optional

class PackageError(Exception):
    """Custom exception for package-related errors"""
    pass

class Package:
    """Package class for WGUPS delivery management"""
    
    def __init__(self, package_id: int, address: str, city: str, state: str, 
                 zip_code: str, deadline: str, weight: float, notes: str = ""):
        self.validate_inputs(package_id, weight)
        
        self.package_id = int(package_id)
        self.address = str(address).strip()
        self.city = str(city).strip()
        self.state = str(state).strip()
        self.zip_code = str(zip_code).strip()
        self.weight = float(weight)
        self.notes = str(notes).strip()
        self.status = "At Hub"
        self.delivery_time: Optional[datetime] = None
        self.departure_time: Optional[datetime] = None
        self.truck = None
        self.deadline = self.parse_deadline(deadline)
        
        # Special handling for wrong address package
        self.original_address = self.address
        if self.package_id == 9:
            self.correct_address = "410 S State St"
            self.address_correction_time = time(10, 20)

    @staticmethod
    def validate_inputs(package_id: int, weight: float):
        """Validate package inputs"""
        if not isinstance(package_id, (int, str)) or int(package_id) < 1:
            raise PackageError("Invalid package ID")
        try:
            weight_val = float(str(weight).replace(' KILO', ''))
            if weight_val <= 0:
                raise PackageError("Weight must be positive")
        except ValueError:
            raise PackageError("Invalid weight format")

    @staticmethod
    def parse_deadline(deadline: str) -> time:
        """Parse deadline string to time object"""
        if isinstance(deadline, str):
            deadline = deadline.strip().upper()
            if deadline == "EOD":
                return time(17, 0)
            
            time_formats = [
                "%H:%M:%S",
                "%I:%M %p",
                "%H:%M",
                "%I:%M%p",
            ]
            
            for fmt in time_formats:
                try:
                    return datetime.strptime(deadline, fmt).time()
                except ValueError:
                    continue
                    
            raise PackageError(f"Invalid deadline format: {deadline}")
        return time(17, 0)

    def update_status(self, status: str, timestamp: Optional[datetime] = None):
        """Update package status and timestamps"""
        valid_statuses = {"At Hub", "En Route", "Delivered"}
        if status not in valid_statuses:
            raise PackageError(f"Invalid status: {status}")
            
        self.status = status
        if status == "En Route":
            self.departure_time = timestamp
        elif status == "Delivered":
            self.delivery_time = timestamp

    def get_status_at_time(self, check_time: datetime) -> dict:
        """Get package status at specific time"""
        # Handle address correction for package 9
        current_address = self.address
        if self.package_id == 9:
            if check_time.time() < self.address_correction_time:
                current_address = self.original_address
            else:
                current_address = self.correct_address

        # Determine status based on timestamps
        if not self.departure_time or check_time < self.departure_time:
            status = "At Hub"
        elif not self.delivery_time or check_time < self.delivery_time:
            status = "En Route"
        else:
            status = f"Delivered at {self.delivery_time.strftime('%I:%M %p')}"

        return {
            'id': self.package_id,
            'address': current_address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip_code,
            'deadline': "EOD" if self.deadline == time(17, 0) else 
                       self.deadline.strftime("%I:%M %p"),
            'weight': self.weight,
            'status': status,
            'notes': self.notes
        }

    def __str__(self) -> str:
        return f"Package {self.package_id}: {self.status} - {self.address}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Package):
            return False
        return self.package_id == other.package_id