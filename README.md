# Social Savoring
---
## Overview: 
In this Django web app, I plan on making a recipe creation social media website where users can create recipes, upload videos/photos, and post their creations online. Other users can see these posts, rate the recipe, add comments, and submit an amendment to fix or enhance the recipe (think a pull request). Users can also branch off a recipe to create a more specific recipe with changes (think fork in git). There will be tags so users creating recipes can add tags which will allow other users to filter all recipes by that tag. Some tags include “vegan”, “gluten free”, “keto”, “kosher”, “vegetarian”, “lent”, “Christmas”, “thanksgiving”, “Hanukah”, etc. I also plan on adding specific categories that users creating recipes an pick so that other users searching can filter. Categories like “breakfast”, “lunch”, “dessert”, “dinner”, “snacks”, “healthy”.  I would also like to add an option for users who are creating recipes to include serving sizes and nutritional facts. I plan on adding a feature where the user creating a recipe can have an option to 1, add all the nutritional facts themselves or 2, search for the ingredient by the brand name and type to have all the nutritional facts be entered that way. I would also like to add an option to download the recipe PDF which will be generated on the fly.  There will be five nav pages: Home, Categories, Search, Create, Profile. More details on each in Details section.

## Details:
- Nav
  - Home: The home page of the website which includes featured posts from other users and posts from followed users.
    - Following section: (left of the home page) lists out all of the profiles you are following. (can hide)
    - Featured section: This section is displayed in the center which shows all the current trending recipes and all the newly created recipes from users that are being followed. (displayed as following: Recipe title, recipe image/short video, and (likes count and number of comments))
  - Categories: This page lets the user filter all recipes based on two fields of categories. 
    - Categories: These parameters are things like “breakfast”, “lunch”, “dinner”, “snacks”, “dessert”, “healthy”
    - Tags: These are specifics about the recipe that can be searched for. (“vegan”, “gluten free”, “keto”, “kosher”, “vegetarian”, “lent”, “Christmas”, “thanksgiving”, “Hanukah”, etc.)
  - Search: (search bar in nav) Lets the user search specifically for a recipe by recipe title.
  - Create: This page lets the user create a new recipe. The parameters to create a new recipe are as follows:
    - Recipe Title: The name of the recipe. (text)
    - Recipe Image upload: (plans for adding short video format) (image)
    - Optional oven temp setting: This will be a radial button saying, “Include oven temp and preheat?”. If user clicks on yes, a text box appears with the option to add oven temp.
    - Serving size: How many servings the recipe makes.
    - Category options.
    - Tag options.
    - Ingredient list: List of ingredients for recipe.
      - Name of ingredient (text)
      - Quantity of ingredient (number)
      - Measurement of ingredient (text)
    - Recipe instructions: The step-by-step instructions on how to make the recipe. (text)
    - Nutritional values calculator: (plan to add an automatic calculator based on ingredients added.)
  - Profile: (indicated by profile picture) once clicked on, a side bar shows and lists the options.
    - My profile: This page lets you edit your profile like profile information like avatar photo, email, and passwords. 
    - My recipes: This page lets you edit your recipes and show all of them.
    - Following: This page lets you edit who you are following and lists all of them.