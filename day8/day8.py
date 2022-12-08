with open("input.txt", "r") as f:
    lines = f.readlines()

trees = [list(num) for line in lines for num in line.split()]

visible = 0

for row_idx in range(1, len(trees)-1): 
    row = trees[row_idx]
    for column_idx in range(1, len(row)-1):

        current_tree = trees[row_idx][column_idx]
        
        trees_in_same_row = trees[row_idx]
        trees_in_same_column = [trees[idx][column_idx] for idx in range(len(trees))]
    
        north_trees = trees_in_same_column[:row_idx]
        south_trees = trees_in_same_column[row_idx+1:]
        west_trees = trees_in_same_row[:column_idx]
        east_trees = trees_in_same_row[column_idx+1:]

        visible_in_row = max(west_trees) < current_tree or max(east_trees) < current_tree
        visible_in_column = max(north_trees) < current_tree or max(south_trees) < current_tree

        if visible_in_row or visible_in_column:
            visible += 1

outer_trees_num = 2 * (len(trees)+len(trees[0])) - 4
visible += outer_trees_num 

print(visible)
            
          
            