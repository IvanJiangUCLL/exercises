# Write your code here
def cakes(eggs, butter, flour):
    recipe_eggs = eggs // 5
    recipe_butter = butter // 250
    recipe_flour = flour // 250
    return min(recipe_eggs, recipe_butter, recipe_flour)
