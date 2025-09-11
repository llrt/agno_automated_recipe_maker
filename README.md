# agno_automated_recipe_maker
This is an experimental AI/agentic automated recipe maker, made with Agno. It is mostly a port of [my CrewAI one](https://github.com/llrt/crewai_automated_recipe_maker), just learn Agno framework.

The work is done by 4 agents:

- chef: the one that crafts the initial recipe, focusing in a beautiful and visually appealing dish
- food_critic: the one that critics the recipe, assessing if it is too complex or less tasteful
- nutritionist: the one that compiles the nutrition facts about the recipe, assessing if it is too fatty or caloric
- writer: the one that writes the final recipe, in the desired language

Note:

The recipes created consider only ingredients found in the given location
The recipes are created in the given language