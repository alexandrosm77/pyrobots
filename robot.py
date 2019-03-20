#!/usr/bin/env python

orientations = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
orientations_reverse = {'0': 'N', '90': 'E', '180':'S', '270':'W'}

class Grid:
    def __init__(self, x, y):
        self.max_x = x if (x<=50) or (x>0) else 50
        self.max_y = y if (y<=50) or (y>0) else 50
        self.scent = []
    
    def add_scent(self, x, y, orientation):
        self.scent.append({'x': x, 'y': y, 'orientation': orientation})
    
    def in_scent(self, x, y, orientation):
        if ({'x': x, 'y': y, 'orientation': orientation} in self.scent):
            return True
        else:
            return False

class Robot:
    def __init__(self, planet, x, y, orientation):
        self.planet = planet
        self.x = int(x) 
        self.y = int(y)
        self.orientation = orientation
        self.lost = False

    def _change_orientation(self, rotation):
        self.orientation += rotation
        if (self.orientation == 360):
            self.orientation = 0
        if (self.orientation < 0):
            self.orientation = 360 + rotation
    
    def _move(self):
        if not(self.planet.in_scent(self.x, self.y, self.orientation)):
            new_x, new_y = self.x, self.y
            if (self.orientation == 0):
                new_y = self.y + 1
            if (self.orientation == 90):
                new_x = self.x + 1
            if (self.orientation == 180):
                new_y = self.y - 1
            if (self.orientation == 270):
                new_x = self.x - 1
            if (new_x > self.planet.max_x) or (new_x < 0) or (new_y > self.planet.max_y) or (new_y < 0):
                self.planet.add_scent(self.x, self.y, self.orientation)
                self.lost = True
            else:
                self.x = new_x
                self.y = new_y
    
    def _check_off_grid(self):
        if (self.x > self.planet.max_x) or (self.x < 0) or (self.y > self.planet.max_y) or (self.y < 0):
            self.planet.add_scent(self.x, self.y, self.orientation)
            return True
        return False

    def _execute_instruction(self, instruction):
        if (instruction == 'R'):
            self._change_orientation(90)
        elif (instruction == 'L'):
            self._change_orientation(-90)
        elif (instruction == 'F'):
            self._move()
        
    def instruct(self, instructions):
        for instruction in instructions:
            self._execute_instruction(instruction)
            if self.lost:
                break
        response = ' '.join([str(self.x), str(self.y), orientations_reverse[str(self.orientation)]])
        if self.lost:
            response += ' LOST'
        return response

def process_input(input):
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

file = open('testdata.txt', 'r')
input = file.read() 

for line in process_input(input):
    print line

