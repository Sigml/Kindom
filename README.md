Kindom
This repository implements a Django-based game system where users can create, manage, and interact with fictional worlds. The core functionality revolves around managing resources, factories, technologies, alliances, trade, and ecology, while progressing through different historical eras.

Key Features:
World Creation: Players can create their own "NewWorld" by choosing a country, age, and initial resources. They are provided with options to manage the resources, factories, and technologies associated with their world.

Game Flow: The game features real-time progression, where the world time increments every 15 seconds, with each day represented as a new entry in the game. The time system aligns with the start and end dates of each era.

Resource Management: The system allows for the allocation and tracking of resources for each world. Players can collect resources, trade them, and use them to build and improve factories, technologies, and armies.

Technologies: Players can unlock new technologies to advance in the game. Each technology requires specific resources, and some are locked behind prerequisites, adding a layer of strategy to resource management.

Social and Ecological Impact: The game includes an ecology system, where factors like air quality, water pollution, forest coverage, and wildlife population affect the gameplay. Players must balance industrial growth with environmental concerns.

Trade and Alliances: Players can form alliances with other nations, establish trade agreements, and even create peace treaties. These diplomatic systems play an essential role in shaping the outcome of the game.

War and Army Management: Players can build and manage armies, engaging in wars with other countries. The outcomes of these conflicts are influenced by military strength, resources, and technologies.

Key Models and Their Relationships:
NewWorld: Represents a unique world created by the user, including country, age, resources, factories, ecology, and trade agreements.
NewWorldResource: Tracks the quantity of resources in the player's world.
NewWorldFactory: Keeps track of factories within the world and their quantities.
Technology: Allows players to unlock technologies that require resources.
Ecology: Represents the environmental factors like air quality, water pollution, etc., affecting the world.
Trade, Alliance, TradeAgreement, PeaceTreaty: Handle the diplomatic and trade interactions between different worlds.
War, Army: Enable conflict and military strategy.
Game Views:
Create New World: A form to create a new world by selecting a country, age, and initializing basic resources and ecology.
Select Game: A list of worlds the user has created, where they can choose which world to manage.
In-Game View: Displays resources, ecology, and technologies. Players can progress the day, unlock technologies, and manage their world.
Delete Game: Allows users to delete a world they no longer wish to play.
Technologies and Features Implemented:
Resource Management: Resources are tied to specific factories, countries, and technologies, requiring strategic planning.
Progression System: The game simulates the passage of time, allowing users to track progress and unlock new features as they advance through eras.
Ecology: Managing the environment becomes crucial, as neglecting it can lead to problems like pollution and deforestation.
This game offers an immersive strategic experience where players must balance resource management, technological progress, and diplomacy to succeed. The combination of time progression, resource management, and diplomacy provides a deep and engaging gameplay experience.


