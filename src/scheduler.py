# scheduler.py
from truck import Truck
from package import Package

def schedule_packages(packages, num_trucks=2, capacity=16):
    """
    Sorts / schedules packages according to deadlines and prioritizes
    earlier-deadline packages first. Splits packages into runs if needed.

    :param packages: List of Package objects
    :param num_trucks: Number of trucks (default 2)
    :param capacity: Capacity per truck
    :return: A list of lists, where each sub-list is a "run" with assigned trucks
             and their packages. For example:
             [
               {
                 'truck_id': 1,
                 'packages': [... up to 16 ...]
               },
               {
                 'truck_id': 2,
                 'packages': [... up to 16 ...]
               }
             ],
             [
               ... # Next run
             ]
    """

    # 1) Filter packages by deadlines or priority if indicated.
    # Convert deadlines to a sortable form. For instance, we assume deadlines are strings like "10:30 AM" or "EOD".
    # We will place EOD packages last, or interpret them as a large time.
    # For simplicity, treat "EOD" as a large number so they end up last in sorting.

    def parse_deadline(deadline_str):
        if deadline_str.upper() == "EOD":
            return 9999  # Large placeholder for end-of-day
        # Otherwise, parse "HH:MM" or "HH:MM AM/PM"
        # You can refine logic for actual datetime if needed
        parts = deadline_str.replace("AM", "").replace("PM", "").strip().split(":")
        hour = int(parts[0])
        minute = int(parts[1])
        return hour * 60 + minute  # Convert to total minutes

    packages_sorted = sorted(packages, key=lambda p: parse_deadline(p.deadline))

    # 2) Fill trucks in order of earliest deadlines first
    # Create a queue of runs: each run can have up to num_trucks trucks. Each truck up to capacity.

    runs = []
    current_run = []
    for truck_id in range(1, num_trucks + 1):
        current_run.append({
            'truck_id': truck_id,
            'packages': []
        })

    run_index = 0
    current_truck_index = 0

    for pkg in packages_sorted:
        # Try to place pkg in the current truck if capacity is not exceeded
        if len(current_run[current_truck_index]['packages']) < capacity:
            current_run[current_truck_index]['packages'].append(pkg)
        else:
            # Move to next truck
            current_truck_index += 1
            if current_truck_index >= num_trucks:
                # We've assigned packages to all trucks in this run
                # Next run
                runs.append(current_run)
                current_run = []
                for tid in range(1, num_trucks + 1):
                    current_run.append({
                        'truck_id': tid,
                        'packages': []
                    })
                current_truck_index = 0
            current_run[current_truck_index]['packages'].append(pkg)

    # Append the last run if it has at least one package
    runs.append(current_run)

    return runs

def create_trucks_for_run(run_data, hub_address='4001 South 700 East', speed=18):
    """
    Creates Truck objects for a single run from the run_data structure.
    :param run_data: e.g. [{'truck_id': 1, 'packages': [pkg1, pkg2,...]}, ...]
    :param hub_address: Hub address
    :param speed: Truck speed, default 18 mph
    :return: list of Truck objects
    """
    trucks = []
    for truck_info in run_data:
        truck_id = truck_info['truck_id']
        t = Truck(truck_id, speed=speed, hub_address=hub_address)
        for pkg in truck_info['packages']:
            t.load_package(pkg)
        trucks.append(t)
    return trucks