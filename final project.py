# Food application 

is_running = True
items = []


def match(items):
    recipes = [lok_lak_beef, cha_khgney_chicken]
    for recipe in recipes:
        recipe_data = recipe()
        recipe_ingredients = recipe_data["ingredients"]
        matches = [ing for ing in items if ing in recipe_ingredients]
        
        print(f"{recipe_data['name']}:")
        print(f"  Matches: {len(matches)} out of {len(recipe_ingredients)} ingredients")
        print(f"  Matched items: {matches}")
        print("-" * 40)
            

def f_ingredients(ingredient):
    meat = ["fish", "chicken", "pork", "beef"]
    diary = ["egg", "fresh milk", "condensed milk"]
    vegetable = ["salad", "tomato", "cucumber",]
    other = ["galanga", "ginger", "garlic", "oyster sauce", "fish sauce", "water", "sweet dark soy sauce"]
    return meat + diary + vegetable + other

def lok_lak_beef():
    ingredients = ["beef", "oyster sauce", "fish sauce", "sweet dark soy sauce", "sugar",
                "corn starch", "water", "black pepper", "salt", "black pepper",
                "lime juice"]
    
    def recipe():
        return ("1. Slice the chunk of beef into thin slices. \n"
            "2. Marinating the beef; use oyster sauce, fish sauce, sweet dark soy sauce, sugar, mince garlic and corn starch to lock the juices. Let it marinate for 30 minutes. \n"
            "3. Gravy sauce for meat; water, oyster sauce, fish sauce, sweet dark soy sauce, sugar, black pepper, corn starch. Mix well. \n\n"
            "4. Dipping sauce; salt, black pepper and lime juice. \n"
            "5. Cooking the meat; on medium-high heat, sear and stir the meat about 85 percent done. \n"
            "6. Cooking gravy sauce; on medium-high heat, pour in and cook the gravy sauce till thickened. \n\n"
            "7. Cook meat & sauce; put the meat in the thickened gravy sauce and cook to your desired preference. \n"
            "8. Fry 1 or 2 eggs. \n"
            "9. Slices up cucumber, tomatoes and lettuces to thin layers. \n\n"
            "10. Last step; put everything together and it's done. \n")
        
    return {"name": "lok lak beef", "ingredients": ingredients, "cook": recipe}

def cha_khgney_chicken():
    ingredients = ["ginger", "chicken", "garlic", "green onion", "oyster sauce",
                          "sugar", "fish sauce", "black pepper"]
    
    def recipe():
        return ("1. Cut and mince the garlic into tiny pieces. Slit the green onions to thin layers. \n"
                  "2. Peel the ginger, wash it, cut it into thin mini strips. \n"
                  "3. Cut chicken into smaller chunks. \n\n"
                  "4. Marinate the chicken with sugar, black pepper, fish sauce and oyster sauce. Mix well. \n"
                  "5. Skillet on high-heat, add in oil and ginger. Let it sizzle for abit. Then add in the garlic till brown. \n"
                  "6. Add in the chicken and cook till done. And garnish the meal with green onion. \n"
                  "7. Bon appetit. \n\n")
        
    return {"name": "cha khgney chicken", "ingredients": ingredients, "cook": recipe}

while is_running:
    ingredient = input("Enter your available ingredient (q to quit): ").lower()

    if ingredient == "q":
        is_running = False
        print(f"Your list: {items}")
        match(items)


    elif ingredient in f_ingredients(ingredient):
        items.append(ingredient)

    elif ingredient not in f_ingredients(ingredient):
        print("Sorry, we don't have item yet.")
         
    
        
                
    

 

    