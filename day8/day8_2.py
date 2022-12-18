def count_trees_in_view(trees, current_tree):

    tree_count = 0
    blocked = False
    i=0

    while not blocked and i < len(trees):

        if trees[i] >= current_tree:
            blocked = True
        
        tree_count += 1
        i += 1    

    return tree_count


with open("input.txt", "r") as f:
    lines = f.readlines()

trees = [list(num) for line in lines for num in line.split()]

highest_score = 0

for row_idx in range(1, len(trees)-1): 

    row = trees[row_idx]
    
    for column_idx in range(1, len(row)-1):

        current_tree = trees[row_idx][column_idx]
        trees_in_row = row
        trees_in_column = [trees[idx][column_idx] for idx in range(len(trees))]
    
        north_trees = trees_in_column[:row_idx]
        north_trees.reverse()
        south_trees = trees_in_column[row_idx+1:]
        west_trees = trees_in_row[:column_idx]
        west_trees.reverse()
        east_trees = trees_in_row[column_idx+1:]

        score = ( 
            count_trees_in_view(south_trees, current_tree) *
            count_trees_in_view(north_trees, current_tree) *
            count_trees_in_view(west_trees, current_tree) *
            count_trees_in_view(east_trees, current_tree))
         
        if score > highest_score:
            highest_score = score

print(highest_score)

          
            
