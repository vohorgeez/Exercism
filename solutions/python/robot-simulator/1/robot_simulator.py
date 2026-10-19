# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.direction = DIRECTIONS[(self.direction + 1) % len(DIRECTIONS)]
            elif instruction == "L":
                self.direction = DIRECTIONS[(self.direction - 1) % len(DIRECTIONS)]
            elif instruction == "A":
                if self.direction == EAST:
                    self.x_pos += 1
                    self.coordinates = (self.x_pos, self.y_pos)
                elif self.direction == NORTH:
                    self.y_pos += 1
                    self.coordinates = (self.x_pos, self.y_pos)
                elif self.direction == WEST:
                    self.x_pos -= 1
                    self.coordinates = (self.x_pos, self.y_pos)
                elif self.direction == SOUTH:
                    self.y_pos -= 1
                    self.coordinates = (self.x_pos, self.y_pos)