#!/usr/bin/env python
"""Software to simulate a robot that lives on a planet
   Requires data that should be in a testdata.txt file
   Run with:
   python runme.py
"""
orientations = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
orientations_reverse = {'0': 'N', '90': 'E', '180':'S', '270':'W'}

class Grid:
    """Class that simultates a grid. Requires the grid directions"""
    def __init__(self, x, y):
        self.max_x = x if (x<=50) or (x>0) else 50
        self.max_y = y if (y<=50) or (y>0) else 50
        self.scent = []
    
    def add_scent(self, x, y, orientation):
        """Method that adds a scent in the grid"""
        self.scent.append({'x': x, 'y': y, 'orientation': orientation})
    
    def in_scent(self, x, y, orientation):
        """Method that checks if given coordinates and direction exist in a previous scent"""
        if ({'x': x, 'y': y, 'orientation': orientation} in self.scent):
            return True
        else:
            return False

class Robot:
    """Robot class that simulates a robot that lives on a planet.
       Requires a planet and the initial robot coordinates and direction  """
    def __init__(self, planet, x, y, orientation):
        self.planet = planet
        self.x = int(x) 
        self.y = int(y)
        self.orientation = orientation
        self.lost = False

    def _change_orientation(self, rotation):
        """Private class method that handles the robots rotation """
        self.orientation += rotation
        if (self.orientation == 360):
            self.orientation = 0
        if (self.orientation < 0):
            self.orientation = 360 + rotation
    
    def _move(self):
        """Private class method that handles the robot's movement """
        if not(self.planet.in_scent(self.x, self.y, self.orientation)): #Check if this move has already resulted in a lost robot
            new_x, new_y = self.x, self.y
            # Calculate next coordinates based on direction
            if (self.orientation == 0):
                new_y = self.y + 1
            if (self.orientation == 90):
                new_x = self.x + 1
            if (self.orientation == 180):
                new_y = self.y - 1
            if (self.orientation == 270):
                new_x = self.x - 1
            # Check if robot is lost
            if (new_x > self.planet.max_x) or (new_x < 0) or (new_y > self.planet.max_y) or (new_y < 0):
                self.planet.add_scent(self.x, self.y, self.orientation) # Add a new scent if robot is lost
                self.lost = True
            else:
                self.x = new_x
                self.y = new_y

    def _execute_instruction(self, instruction):
        """Private class method that executes one instruction at a time """
        if (instruction == 'R'):
            self._change_orientation(90)
        elif (instruction == 'L'):
            self._change_orientation(-90)
        elif (instruction == 'F'):
            self._move()
        
    def instruct(self, instructions):
        """Class method that gets one line instructions and returns the instruction result """
        for instruction in instructions:
            self._execute_instruction(instruction)
            if self.lost:
                break
        # Format the response to match the specified output
        response = ' '.join([str(self.x), str(self.y), orientations_reverse[str(self.orientation)]])
        if self.lost:
            response += ' LOST'
        return response

def process_input(input):
    """Function that processes input for creating a planet and moving robots. Returns results in a list """
    input_lines = input.splitlines()
    mars_x, mars_y = (int(x) for x in input_lines[0].split(' '))
    mars = Grid(mars_x, mars_y)
    line = 1 # First line for robot initial position
    response = []
    while True:
        if (line == len(input_lines)):
            break
        robot_x, robot_y, robot_orientation = (s for s in input_lines[line].split(' '))    
        robot = Robot(mars, robot_x, robot_y, orientations[robot_orientation])
        line += 1 # move to next line for instructions
        response.append(robot.instruct(input_lines[line]))
        
        line += 1 # move to next robot
        
    return response



