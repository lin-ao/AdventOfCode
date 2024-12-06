from copy import deepcopy
from enum import Enum


def load_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(_input: str) -> list[list[str]]:
    return [list(row.strip("\n")) for row in _input.strip("\n").split("\n")]


class Direction(Enum):
    North = (-1, 0)
    East = (0, 1)
    South = (1, 0)
    West = (0, -1)


def get_guard_location(patrol_map: list[list[str]]) -> tuple[tuple[int, int], Direction]:
    for i, row in enumerate(patrol_map):
        if '^' in row:
            return (i, row.index('^')), Direction.North
        elif '>' in row:
            return (i, row.index('>')), Direction.East
        elif 'v' in row:
            return (i, row.index('v')), Direction.South
        elif '<' in row:
            return (i, row.index('<')), Direction.West


class Guard:
    def __init__(self, patrol_map: list[list[str]], starting_position: tuple[int, int], starting_direction: Direction) -> None:
        self.patrol_map = patrol_map
        self.position = starting_position
        self.direction = starting_direction
        self.visited_squares = [(self.position, self.direction)]
        self.at_border = self._check_border()
        self.stuck_in_loop = False
        self._patrol()

    def _check_obstacle(self) -> bool:
        square = tuple(a + b for a, b in zip(self.position, self.direction.value))
        return self.patrol_map[square[0]][square[1]] == '#'
    
    def _check_border(self) -> bool:
        if 0 < self.position[0] < len(self.patrol_map[self.position[0]]) - 1 and 0 < self.position[1] < len(self.patrol_map) - 1:
            return False
        else:
            return True

    def _walk(self) -> None:
        self.position = tuple(a + b for a, b in zip(self.position, self.direction.value))
        self._check_for_loop()
        self.visited_squares.append((self.position, self.direction))

    def _turn(self) -> None:
        if self.direction == Direction.North:
            self.direction = Direction.East
        elif self.direction == Direction.East:
            self.direction = Direction.South
        elif self.direction == Direction.South:
            self.direction = Direction.West
        elif self.direction == Direction.West:
            self.direction = Direction.North
    
    def _patrol(self) -> None:
        while not self.at_border and not self.stuck_in_loop:
            if self._check_border():
                self.at_border = True
                break
            if self._check_obstacle():
                self._turn()
                continue
            self._walk()

    def _check_for_loop(self) -> None:
        if (self.position, self.direction) in self.visited_squares:
            self.stuck_in_loop = True
        
    def get_visited_squares(self) -> list[tuple[int, int]]:
        return [visited_square[0] for visited_square in self.visited_squares]
    
    def get_stuck_in_loop(self) -> bool:
        return self.stuck_in_loop
    

def add_obstacle(patrol_map: list[list[str]], index: tuple[int, int]) -> list[list[str]]:
    if patrol_map[index[0]][index[1]] == '.':
        patrol_map[index[0]][index[1]] = '#'
    return patrol_map


def count_possible_loops(patrol_map:list[list[str]], starting_position: tuple[int, int], starting_direction: Direction) -> int:
    possible_loops = 0
    for i, _ in enumerate(patrol_map):
        for j, _ in enumerate(patrol_map[i]):
            current_map = add_obstacle(patrol_map=deepcopy(patrol_map), index=(i, j))
            current_guard = Guard(patrol_map=current_map, starting_position=starting_position, starting_direction=starting_direction)
            if current_guard.get_stuck_in_loop():
                possible_loops += 1
    return possible_loops    


def main() -> None:
    test_data: list[list[str]] = [
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ]
    test_starting_position, test_starting_direction = get_guard_location(test_data)
    test_guard = Guard(patrol_map=test_data, starting_position=test_starting_position, starting_direction=test_starting_direction)
    assert len(set(test_guard.get_visited_squares())) == 41
    assert count_possible_loops(patrol_map=test_data, starting_position=test_starting_position, starting_direction=test_starting_direction) == 6
    patrol_map = parse_input(_input=load_input(filename="day_06_input.txt"))
    starting_position, starting_direction = get_guard_location(patrol_map=patrol_map)
    guard = Guard(patrol_map=patrol_map, starting_position=starting_position, starting_direction=starting_direction)
    answer_part_one = len(set(guard.get_visited_squares()))
    answer_part_two = count_possible_loops(patrol_map=patrol_map, starting_position=starting_position, starting_direction=starting_direction)
    print(f"Answer for part one: {answer_part_one}")
    print(f"Answer for part two: {answer_part_two}")


if __name__ == "__main__":
    main()
