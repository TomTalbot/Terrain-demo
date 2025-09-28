# Terrain-demo

***Press space when running to change the generation***

This is a project demonstrating a terrain generation algorithm from a project i worked on previously. The previous algorithm made use of perlin noise to generate terrain based on random values given by said perlin noise. Since then the perlin noise python library has stopped working, so the algorithm has been adapted making use of the random library instead. 

The algorithm makes use of the pygame library to draw and render the terrain. 

The algorithm starts with a base height and randomly changes the given height values with a range of (-32 - +32) pixels whilst keeping the terrain itself within the confines of the screen (In this instance 1/3 of the screen to its base). The algorithm ensures that the top tiles are generated as the grass sprite and all subsequent tiles below it as the dirt sprite. 

The display is being constantly updated within the game loop itself so that the terrain can be regenerated on the press of the spacebar. 

This algorithm is free to use in project should you see fit. 
