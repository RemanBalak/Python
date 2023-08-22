# Exercise 1.2

## Task

- **name (str):** Contains the name of the recipe
- **cooking_time (int):** Contains the cooking time in minutes
- **ingredients (list):** Contains a number of ingredients, each of the str data type

I have decided to use dictionaries for storing the above data for each recipe because of the different data types needing to be stored and the flexibility of dictionaries. Dictionaries can store the recipe names as strings, the ingredients as lists, and the cooking time as integers and are also mutable so each recipe can be updated or added to in the future.

**all_recipes = [ ]**

I have used a list because the recipe data may need to be modified or expanded in the future. I want to use methods like append() to easily add new recipes and anticipate changes or updates to the recipe data over time.
