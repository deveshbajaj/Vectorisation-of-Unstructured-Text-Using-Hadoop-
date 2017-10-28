import pandas
df = pandas.read_json("out.json")
rec = df["recipe_name"]
matrix = pandas.DataFrame()
recipes = rec.tolist()
matrix["recipe_name"] = recipes
matrix = matrix.set_index("recipe_name")
all_ingredients = df.loc[:,"ingredients"].tolist()
for ingredients, recipe_name in zip(all_ingredients, recipes):
    for item in ingredients:
        item = item.lower()
        if item in matrix.columns:
            matrix.loc[recipe_name,item] = 1
        else:
            matrix[item] = 0
            matrix.loc[recipe_name,item] = 1
print(matrix)
matrix.to_csv("vector.csv")
print("Hakuna Matata!")