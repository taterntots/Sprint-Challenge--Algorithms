class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # # Swap items with index zero
        # self.swap_item()
        # print(f'STARTING ITEM', self._item)

        # # while self.compare_item() == -1 or self.compare_item() == None:
        
        # while self.can_move_right() == True:
        #     self.move_right()

        #     if self.compare_item() == 1:
        #         print(True)
        #         self.swap_item()
        #         print(f'HELD ITEM', self._item)
        #         print(f'CURRENT POSITION', self._position)
        # else:
        #     if self.can_move_right() == False:
        #         print(f'FINAL HELD ITEM', self._item)
        #         self.swap_item()

        # # while self.can_move_left() == True:
        # #     if self.can_move_right() == False:
        # #         if self.compare_item() == -1:
        # #             print(True)
        # #             self.swap_item()
        # #             self.move_left()
        # #             print(f'NEW CURRENT POSITION', self._position)
        
        # Turn the robot on to start a while loop
        while self.light_is_on() == False:
            self.set_light_on()

            # While robot can move right, swap item and move right
            while self.can_move_right():
                self.swap_item()
                self.move_right()
                print(f'HELD ITEM', self._item)

                # Compare and swap items if greater than current item
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.set_light_off()
                    print(f'HELD ITEM', self._item)
                    print(f'CURRENT POSITION', self._position)
                # If smaller than current item (or none)
                else:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            
            # Move back left to continue sorting
            while self.can_move_left():
                self.move_left()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# -------------------------------
# UNDERSTANDING THE PROBLEM
# -------------------------------

# We have a robot that can only move from left to right, 
# swapping out items (in this case integers) with the one it's currently
# holding to the one in front (to the right of it). We need to program
# the robot to sort a given list of items (again, integers) using the
# abilities given to us.

# By the look of things, the problem sounds very similar to bubble
# sorting. If we can get the robot to start from position 
# zero (the start of our list), we can have it move from left to right, 
# comparing the currently held item with the next in the list. Should it find
# something smaller, it will swap to items until everything is in the correct spot.

# -------------------------------
# PLANNING
# -------------------------------

# Have the robot start from the beginning of the list (index zero)
# If the current item is larger than the next item to the right:
    # Pick up the item
    # Move one space to the right
    # Swap for new item
# Keep swapping items until you get to the end of the array
# If the robot can no longer move to the right:
    # Swap the last integer with the smallest and send the robot back to the beginning of the list and re
# Repeate from the top