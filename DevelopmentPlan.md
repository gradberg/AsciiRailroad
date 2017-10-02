	
* 0.0.x Goals: Train controls with speed controls. Player can get on off train or move to other cars to detach them, or to throw switches. 
  * 0.0.1 *DONE* - On a fixed locomotive that moves around a track. It moves one square per button press (forward vs back) from player. 
  * 0.0.1.1 *DONE* - Add Switches. Have them display, with background colors?, which direction the switch is thrown? (Though for colorblind it would be better to be symbol changes, not color changes). Have a single keystroke flip all switches on the map for now.
  * 0.0.2 - *DONE* Cars added to train that trail behind it.
  * 0.0.3 - *DONE* Placeholder locomotive engine system, where you set the throttle to a given speed. This will cause it to move a certain number of spaces per 'tick' (Which will be it for now). This requires a first step of time, where the locomotive can move multiple spaces, and you can press a button to change through time.
  * 0.0.4 - *DONE* Make player independent of train.
  * 0.0.5 - *DONE* Add switches to go down different lines, On-foot can throw them.
  * 0.0.6 - *DONE* Add attaching & detaching detaching of cars. (Player can move on train) This also includes car-specific UI and car -specific brakes
	§ Unit test collision logic.
	§ Absent a proper time system, the best movement and collision logic would be to queue all train movement into one step increments and check after each increment if any trains collided. This would allow disconnecting cars on a moving train properly.
	§ For now just stop both trains. Long term, would want to use car weight and speed to c associate momentum and user that to determine speed afterwards, in addition to crashing : P
  * 0.0.7 - *DONE* Larger map world with scrolling? 
  * 0.0.8 - *SKIPPING* Fancy GUI framing different sections
  * 0.0.9 - *SKIPPING* Use similar Roguelike characters, like "#" being the walls of a building.
  * 0.0.10 - *SKIPPING* Game lifecycle, with startup, playing, death, and scoretable and saves
  * 0.0.11 - *SKIPPING* Revisit color usage, limit used colors, and avoid the clown like issue. Only use bold, notable colors to emphasize something that needs to be.
  * *DONE* Set-up Github or Mercurial for code. Put this document file up on there.

* 0.1.x - Gameplay: Now that some very basic structure is set up (tracks, switches, movement on and off of train, splitting and joining trains) its time to add SOME actually gameplay so that there is a reason to for some of the other infrastructure to exist (better GUI, game lifecycle)
    * 0.1.1 - Add some basic objectives (a yard, move a car from one yard to the other) - This sets the stage for adding the Steam Locomotive mechanics as the challenge for accomplishing those basic objectives.
        * Add cash to player and display. Will just be for display now.
        * Add locations to the map (Rail Yards). They will have a different background color, have a name, which the user can see when they are over them.\    * Add missions, where the player must move a car from one yard to another. The user will have a mission browser (in the locomotive? caboose!).
        * Add checking and success/failure of the mission, with corresponding cash change.
    * 0.1.2 - Steam Locomotive mechanics and unit tests - Add this now, as it provides the more interesting movement aspect to playing the game (albeit I want some workaround so that for dev mode, I can easily move the train around)
        * Create a Push Cart, which the user presses a button to give it force (which it can save with momentum). Probably cannot pull a car
        * Create a Super Push Cart, which gives the user significant force to pull things. This would essentially be the dev-god-mode locomotive.
        * Create a basic steam locomotive itself  
    * 0.1.3 - NPC Crew - Should b efun to have them managing the engine 
    * 0.1.4 - NPC Trains - Other trains rolling around with their own goals
    * 0.1.? - Time System - Not quite yet, there just are not enough game components to use it
    * 0.1.? - Objectives/Score - 
		
* 0.2.x - Game Lifecycle - Now that a number of actual gameplay features exist, add the infrastructure for proper game function, like title screen, save games, etc
  * Title screen
  * Saves
  * Death, Retirement, and Game Over

_Implement proper time, with different actions taking time, and the engine moving that amount of time_
_Implement Message System_

* 0.3.x - NPCs: Third party trains that run along the lines
  * Brakemen to throw switches
  * Fireman to automate the water and fire intake
  * NPC Trains with their own engineers

* 0.4.x - More Map Objectives: Player can earn money by moving cars to destinations, and must use that money to buy fuel.
  * Buildings/Businesses shown on map
  * Interaction (on foot?) with those businesses

* 0.5.x - Random Maps: Maps are procedurally generated. Leaving one map generates another.
  * Buildings - Eventually represent points of interest (add a building interaction system?)
  * Bridges - Can walk over as a person… and can get hit.
  * Rivers - Inhibit ground movement
  * Trees
  * Terrain / heightmaps
  * Map themes: Depressed industrial town where good transportation can reopen businesses, city with lots of roads and cramped tracks, war zone with munitions where your delivery of munitions can help one side (but if you're not careful, you could be killed or your train confiscated or destroyed), logging call, mining town (with steep elevation to deal with). These could be implemented like dungeon crawl branches, though that requires some sort of greater reward at the end of them. (Special prestige car that elevates your ranking?)
  * Look up model railroad layouts for this sort of stuff. I could even put Dad's layout in it...
		
		
		
* 1.0.x - Retirement: After a certain number of turns, you retire, getting a score.
