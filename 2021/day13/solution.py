# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/14 00:16:55 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/14 22:44:31 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 13 – Advent of Code 2021

def parser(fileName):
    with open(fileName) as f:
        dots_coordinates, fold_instructions = f.read().strip().split('\n\n')
        dots_coordinates = [[int(n) for n in line.split(',')] for line in dots_coordinates.splitlines()]
        fold_instructions = [[left[-1], int(right)] for left, right in (line.split('=') for line in fold_instructions.splitlines())]
        return dots_coordinates, fold_instructions
    
def create_paper(dots_coordinates, max_x, max_y):
    
    paper = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for coord in dots_coordinates:
        x, y = coord
        paper[y][x] = '#'
    return paper

def fold_paper(fold_instructions, max_x, max_y, paper):
    for (axis, pos) in fold_instructions:
        old_max_x = max_x
        old_max_y = max_y
        if axis == 'x':
            max_x = pos
        elif axis == 'y':
            max_y = pos
        folded_paper = [['.' for _ in range(max_x)] for _ in range(max_y)]
        for i in range(max_y):
            for j in range(max_x):
                # Always keep the unfolded side
                if i < len(paper) and j < len(paper[0]) and paper[i][j] == '#':
                    folded_paper[i][j] = '#'
                # Merge the folded side by mirroring
                if axis == 'y':
                    mirror_i = 2 * pos - i
                    if mirror_i < len(paper) and j < len(paper[0]) and paper[mirror_i][j] == '#':
                        folded_paper[i][j] = '#'
                elif axis == 'x':
                    mirror_j = 2 * pos - j
                    if i < len(paper) and mirror_j < len(paper[0]) and paper[i][mirror_j] == '#':
                        folded_paper[i][j] = '#'
        paper = folded_paper
    return paper

def main():
    dots_coordinates, fold_instructions = parser("input.txt")
    max_x = max(line[0] for line in dots_coordinates) + 1
    max_y = max(line[1] for line in dots_coordinates) + 1
    paper = create_paper(dots_coordinates, max_x, max_y)
    paper = fold_paper(fold_instructions, max_x, max_y, paper)
    for row in paper:
        for c in row:
            if c == '#':
                print('█', end='')
            else:
                print(' ',end='')
        print()


if __name__ == "__main__":
    main()
