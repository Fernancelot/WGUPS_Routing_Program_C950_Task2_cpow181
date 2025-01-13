# package.py

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline  # e.g. "10:30 AM" or "EOD"
        self.weight = weight
        self.notes = notes
        self.status = "At Hub"

    def __repr__(self):
        return f"Package({self.package_id}, deadline={self.deadline})"