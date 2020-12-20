from math import prod


def load_input(file_path: str) -> dict[int, list[str]]:
    with open(file_path, "r") as file:
        tile_dict = {}
        for block in file.read().split("\n\n"):
            number = int(block.split("\n")[0].split(" ")[1].rstrip(":"))
            tile = block.rstrip("\n").split("\n")[1:]
            first_row = tile[0]
            last_row = tile[-1]
            left_side = "".join(list(zip(*tile))[0])
            right_side = "".join(list(zip(*tile))[-1])
            tile_dict[number] = [first_row, first_row[::-1], last_row, last_row[::-1], left_side, left_side[::-1],
                                 right_side, right_side[::-1]]
    return tile_dict


def is_corner(tile: int, tile_dict: dict[int, list[str]]) -> bool:
    unique_side = 0
    for side in tile_dict[tile]:
        if not any(side == other_side for other in tile_dict for other_side in tile_dict[other] if tile != other):
            unique_side += 1
    if unique_side >= 4:
        return True
    else:
        return False


def search_corners(tile_dict: dict[int, list[str]]) -> list[int, int, int, int]:
    corners = [tile for tile in tile_dict if is_corner(tile, tile_dict)]
    return corners


def main() -> None:
    tiles = load_input("day_20_input.txt")
    corners = search_corners(tiles)
    answer = prod(corners)
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
