class ConveyorBelt:
    def __init__(self):
        self.items_on_belt = []
    
    def start_belt(self):
        self.items_on_belt = ["Item1", "Item2", "Item3"]
        print("Conveyor belt started with items:", self.items_on_belt)
    
    def stop_belt(self):
        self.items_on_belt.clear()
        print("Stopping conveyor belt. Remaining items:", self.items_on_belt)


class RoboticArm:
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt
        self.picked_item = None
    
    def pick_item(self):
        if self.conveyor_belt.items_on_belt:
            self.picked_item = self.conveyor_belt.items_on_belt.pop(0)
            print(f"Robotic arm picked: {self.picked_item}")
        else:
            print("No items left to pick.")
    
    def place_item(self):
        if self.picked_item:
            processed_item = self.picked_item + " (Processed)"
            self.conveyor_belt.items_on_belt.append(processed_item)
            print(f"Robotic arm placed: {processed_item}")
            self.picked_item = None
        else:
            print("No item to place.")


class QualityControlSystem:
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt
    
    def inspect_items(self):
        if all("Processed" in item for item in self.conveyor_belt.items_on_belt):
            print("Quality Check Passed: All items are processed.")
        else:
            print("Quality Check Failed: Some items are not processed.")


class SmartFactory:
    def __init__(self):
        self.conveyor_belt = ConveyorBelt()
        self.robotic_arm = RoboticArm(self.conveyor_belt)
        self.quality_control = QualityControlSystem(self.conveyor_belt)
    
    def start_factory(self):
        print("Starting Smart Factory...")
        self.conveyor_belt.start_belt()
        self.robotic_arm.pick_item()
    
    def stop_factory(self):
        print("Stopping Smart Factory...")
        self.robotic_arm.place_item()
        self.conveyor_belt.stop_belt()
    
    def quality_check(self):
        print("Performing Quality Check...")
        self.quality_control.inspect_items()


# Example usage
factory = SmartFactory()
factory.start_factory()
factory.stop_factory()
factory.quality_check()
