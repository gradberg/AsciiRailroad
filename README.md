# AsciiRailroad
AsciiRailroad

Theme - Capture the feel of operating a train, picking up cars, rearranging cars, and delivering cars to destinations, all while managing available track space and avoiding other trains.

Gameplay - Player represents the engineer, who both operates the locomotive and is the owner of the train line's company. As owner, the player chooses when to upgrade locomotives, what deliveries to take. As engineer, the player runs the locomotive's controls, controling the throttle, braking, and other special functions in the case of older engines.

Roguelike - 
* Permadeath - You are running a company. If you run out of cash, you're bankrupt and its all over. If you crash the train, the combined cost of replacing the locomotive and paying the injured parties for their lost rolling stock and cargo likely will put you out of business.
* Progression - Buy new locomotives. Hire additional crew? Any stats or abilities?

Ideas - 
* Normal 'map' display is top-down view of train on tracks. Each engine/car taking up one character normally.
* Side view of train shows slightly more artistic view of engine, showing player as engineer on one, and visually obvious cars behind (passenger versus steel versus coal versus boxcar, etc).
* Analogous to normal Roguelikes, each train line is equivalent to a single dungeon level, procedurally generated. Rail yards = large rooms while lines connecting yards are equivalent to corrodors. Each level, being a different company's track, may have different operating conditions (cost more per turn to use their track, more or less other trains running around (potentially picking up the cars that you want to pick up for cash), different track quality.
* To attach, detach cars, or throw brakes, on the side view you can move around the train.
* EVEN BETTER!!! You can move around the world on foot. But you can get on or off you train. I wouldn't suggest jumping off a train that's going 100 mph though. This is less to let the player explore the world as it is to provide the feeling of being a little character riding atop a large machine. And lets you throw switches manually. Basically you are Buster Keaton in "The General".
* Focus on steam locomotives, because that way you must manage steam pressure, firebox,etc. Avoid boiler explosions, keep fuel stocks, manipulate brakes
* You can set brakes on an individual cars
* Potentially have tracks with too tight if curves, requiring you to tow along a smaller engine for retrieving cars off of those branches.
* Can have height, where if the ground Is heigher it will be in another color, like a relief map.
* Different maps may have different themes, like a logging railroad or some such.
* Plot is you are an independent locomotive owner(like an owner operator semi truck driver) running on all these railroads, and you have to pay to use th`eir tracks.
* Certain lines can be serviced repeatedly, like passenger routes, but over time your earnings will decrease, and competitor reasons will move in forcing you to continue looking.
* Violating signals and other restrictions, assuming they don't cause an accident, will get you fined by the host railroad.
* Maybe the end goal is that you'll retire after certain number of maps or turns, and thus it's a race against to make enough money to retire comfortably.
* Locomotive factories exist here and there where you can buy new engines. Also, over time and poor use, your locomotives can be damaged, running worse, which you must get repaired at a depot.
* Certain cargos, especially passengers, require 
* Most cars will be owned by other companies, and you just ferry stuff around. However, some companies will not own rolling stock, and instead you can purchase it (and keep it on your train) for which you make greater profits, since its using more of your equipment and less of theirs.
* Plenty of Onomatopoeia:
** Whistle (if implements. Perhaps you can be fined if in a yard and failing to whistle before moving) *SQUEEEEE*
** Piston pumping, longer the faster the train goes. *CHUG*  *CHUG-A-CHUG* *CHUH-A-CHUG-A-CHUG-A-CHUG*. You could hear these for distant trains and be able to tell his fast they're going.
* Rare, random misfortune possibilities, like a car or some such on the tracks, and either you slam on the brakes, or you hit it. Broken tracks. Derailment up ahead. Other trains in the way. Cattle or wild animals on the tracks. Damsel in distress tied up on the tracks. Suddenly a river washing out a nearby bridge temporarily.
	
* The right part of the screw  shows your current controls. If you're on the locomotive, it shows its controls. If you're on another car, it'll show the brakes. This means you could indepently control multiple locomotives.
* Obviously if you stand on tracks with a train coming, you'll get hit. If its an NPC crew who has time to react, they'll try as hard as possible to stop the train before it hits you. If it’s a train owned by the map's Railroad, they'll start fining you for disruption of their operations (if you live by jumping out of the way, that is).
* Probably need a friendly brakeman NPC, because older trains without automatic air brakes would need someone putting the brakes on individual cars of a freight train, since the engine's brakes can only do so much.
* You could also hire, if you want, an NPC Fireman who shovels coal when needed. However, you do have to pay for such a person, so its up to you if you'd prefer the tradeoff of someone who knows what they're doing.
* Perhaps a much later version could allow you to even hire an engineer, and you become more of a passenger as you run around arranging deals and such.
* The brakeman could also be told to throw switches. It'd be awesome if you're the engineer, and you tell them what to do.
* Locomotives of the same design will all have every so slight differences in all their capacities, heat/power transfer rates, etc. When the Locomotive is instantiated in the game world, it will calculate all of these differences which will remain constant throughout its existance (minus any maintenance degredation). This should provide JUST enough variation that a player never gets into an exact routine of how the engine functions. Each time starting and stopping will act ever so slightly different.
* You will spin the driving wheels if you apply too much power and the locomotive has too much resistance, such as having way too many cars, or by having the brakes on all the cars. Spinning them too long damages the driving gear. At a certain point the damage both reduces power, and at higher speeds the gear will Continue to damage itself even with correct usage (because now that it is shaky, strain on it makes it worse), until eventually if its not fixed one side will snap, greatly reducing power.
* Power output is converted to acceleration. As your speed goes up, more power is required to achieve that acceleration (though maintaining speed is easier). That is why just starting out makes it easy to spin the wheels, because you have maximum acceleration, but as you increase speed it disappears as an issue.
* Locomotive controls show the settings, when you press a button to modify one, the rest of the locomotive controls go grey or disappear entirely, showing you the necessary information to modify just that one. Thus when you go to modify a control, you get all the information you need, but otherwise the locomotive controls are mostly unimpared by keycommands and labels
* Definitely allow connecting to active NPC trains.Ownership should exist at the car level, not train level and being able to connect to opponent trains and have a tug of war of locomotives I'd a cool sandbox feature. Of course of its a railroad train you'll be fined...
* Sounds have volume affected by distance. If you are in a high speed locomotive, you wont hear a distant train over your own engine.
* Have a trail of smoke which gratis the background of surrounding tiles (when they have nothing else to color)
* On foot, if you walk into someone, you can push them one square over. However, that will anger them, and they may injure you.
* RPG Elements (HA!) - Players would get more attached to their progress if they start accumultating a handful of cars they always bring with them. They may have certain boosts (Caboose saves on, um, hotel stays???), while others allow for certain missions, or more profitable missions (two passenger cars instead means making twice as much on a passenger mission?)
* Also possible is turning the game more into an arcade design. I worry that, since there is no amulet of Yendor to capture, it will be difficult coming up with a compelling end game. Thus maybe I should go down an arcade route. Each map should be relatively short amount of time on it (5 minutes at most?). And instead you are an Engineer for a company who keeps getting assigned around to different parts of the company to take care of things. So each map starts with you outside the company building, and you can pick from amongst one or more locomotives to use to accomplish your objectives for that map. Once you fail or succeed at them, you move on to the next map. Thus each map requires you analyzing your available resources and objectives, and attempt to succeed as much as possible (evauate enough civilians out of an area before something happens, etc)
* On some maps, you can attack rival engineers and steal their already running nicely locomotive.
* You are on the run from the law. You use horses and locomotives to escape
	
	
	
	
Locomotive Theory of Operation
http://www.trainorders.com/discussion/read.php?10,586430,nodelay=1
http://en.wikibooks.org/wiki/Steam_Locomotive_Operation
http://www.ovsrails.com/OVSTI/SteamLocoManual.htm

	• Starting / Accelerating
		○ Burn fuel (coal, fire, oil) in Firebox - _WILL_ be in the game. Player will need to do an action to fill the firebox up. It will burn fuel at a constant rate. It will impart heat to the water, and the burning fuel will (with a linear function) increase that temperature back up. I will not be modeling any other heat loss or efficincies, but if you're going to be stuck somewhere a bit, it may be advantageous to let the fire die down so that you're not wasting fuel, going into steam, that is then vented off or naturally cooled. (All the coal in the firebox is burnt up in 3 minutes.)
		○ Water injection into the boiler - _WILL_ be in the game. It must be be kepter higher than the top of the firebox (or the firebox will melt, or the fusible plug will put out the fire if you have one installed), but low enough that there is room for steam to be stored. (Too little room, and you may have high PSI, but it can disappear very quickly as you open up the throttle. Even worse, if its WAY too high, it could be pulled into the cylinders, which probably significantly impacts power, if not damaging them. This is done manually (as in, its not automatic feed, you must open and close the valve)
		○ Open the Cylinder Cocks - When the Cylinders are cold, they'll condense some of the water into steam. This water sitting in the cylinders would decrease their effectiveness and, probably, damage them if too much accumulated. Opening the cocks lets that water get drained/pushed out by steam as the cylinder runs. Once the cylinder is warmed up, and all the condensation is drained, you close them to get some extra strength from the cylinders. _WILL_ be in the game. But it will be somewhat optional, in that it won't damage the engine, but will affect power. So new players can skip this for a bit until they get more comfortable.
		○ Throttle - _WILL DO_. Not sure how technically this functions, but if the train is at a dead stop and you open the throttle too much, you can spin the drivers (wheels), which can damage the track or the wheels/drive gear. (If you do this too much, it will slowly degrade the maintenance condition of the locomotive). The chance of spinning them would be a combination of weight you're trying to pull versus driving force versus weight of the locomotive.
		○ Johnson Bar - As the engine accelerates, it uses up steam from the boiler. As it moves faster, it exceeds the steam generation of the boiler, so the Johnson Bar reduces the length of the piston stroke for which steam is injected, down from 100% to 90 or 80%. THIS IS THE SAME AS THE REVERSER. You set it full one direction or the other for maximum power, but as you speed up you can ease off of it to use less steam, and thus use less water and fuel. _DEFINITELY IMPLEMENT_
	• Stopping / Braking
		○ Throttle is shut off and opened a crack - Already implemented the throttle, but will not worry about the 'open a crack for lubrication'.
		○ Brakes - 
	
Milestones
	• 0.1.0 - Goals: Train controls with speed controls. Player can get on off train or move to other cars to detach them, or to throw switches. 
		○ 0.0.1 *DONE* - On a fixed locomotive that moves around a track. It moves one square per button press (forward vs back) from player. 
		○ 0.0.1.1 *DONE* - Add Switches. Have them display, with background colors?, which direction the switch is thrown? (Though for colorblind it would be better to be symbol changes, not color changes). Have a single keystroke flip all switches on the map for now.
		○ 0.0.2 - *DONE* Cars added to train that trail behind it.
		○ 0.0.3 - *DONE* Placeholder locomotive engine system, where you set the throttle to a given speed. This will cause it to move a certain number of spaces per 'tick' (Which will be it for now). This requires a first step of time, where the locomotive can move multiple spaces, and you can press a button to change through time.
		○ 0.0.4 - *DONE* Make player independent of train.
		○ 0.0.5 - *DONE* Add switches to go down different lines, On-foot can throw them.
		○ 0.0.6 - *DONE* Add attaching & detaching detaching of cars. (Player can move on train) This also includes car-specific UI and car -specific brakes
			§ Unit test collision logic.
			§ Absent a proper time system, the best movement and collision logic would be to queue all train movement into one step increments and check after each increment if any trains collided. This would allow disconnecting cars on a moving train properly.
			§ For now just stop both trains. Long term, would want to use car weight and speed to c associate momentum and user that to determine speed afterwards, in addition to crashing : P
		○ 0.0.7 - *DONE* Larger map world with scrolling? 
		○ 0.0.8 - *SKIPPING* Fancy GUI framing different sections
		○ 0.0.9 - *SKIPPING* Use similar Roguelike characters, like "#" being the walls of a building.
		○ 0.0.10 - *SKIPPING* Game lifecycle, with startup, playing, death, and scoretable and saves
		○ 0.0.11 - *SKIPPING* Revisit color usage, limit used colors, and avoid the clown like issue. Only use bold, notable colors to emphasize something that needs to be.
		○ Set-up Github or Mercurial for code. Put this document file up on there.
	• 0.2.0 - Gameplay: Now that some very basic structure is set up (tracks, switches, movement on and off of train, splitting and joining trains) its time to add SOME actually gameplay so that there is a reason to for some of the other infrastructure to exist (better GUI, game lifecycle)
		○ Add some basic objectives (a yard, move a car from one yard to the other) - This sets the stage for adding the Steam Locomotive mechanics as the challenge for accomplishing those basic objectives.
		○ Steam Locomotive mechanics and unit tests - Add this now, as it provides the more interesting movement aspect to playing the game (albeit I want some workaround so that for dev mode, I can easily move the train around)
		○ Time System - Not quite yet, there just are not enough game components to use it
		○ Objectives/Score - 
		
	• 0.3.0 - Game Lifecycle - Now that a number of actual gameplay features exist, add the infrastructure for proper game function, like title screen, save games, etc
		○ Title screen
		○ Saves
		○ Death, Retirement, and Game Over




	• 0.2.0 - Goals: Locomotive now behaves like an actual steam engine, requiring finnese with fire temperature, boiler temperature, etc. In order to stop/start it. 
		○ 0.1.1 - Implement proper time, with different actions taking time, and the engine moving that amount of time
		○ 0.1.2 - Implement message system
		○ 0.1.3 - Implement a separate class that isolates all of the steam engine mechanics. Write unit tests to verify the state of the engine.
		○ 0.1.4 - Losing / Damage - Trains smashing into each other too fast should crash?
	• 0.3.0 - NPCs: Third party trains that run along the lines
		○ Brakemen to throw switches
		○ Fireman to automate the water and fire intake
		○ NPC Trains with their own engineers
	• 0.4.0 - Map Objectives: Player can earn money by moving cars to destinations, and must use that money to buy fuel.
		○ Buildings/Businesses shown on map
		○ Interaction (on foot?) with those businesses
	• 
	• 0.5.0 - Random Maps: Maps are procedurally generated. Leaving one map generates another.
		○ Buildings - Eventually represent points of interest (add a building interaction system?)
		○ Bridges - Can walk over as a person… and can get hit.
		○ Rivers - Inhibit ground movement
		○ Trees
		○ Terrain / heightmaps
		○ Map themes: Depressed industrial town where good transportation can reopen businesses, city with lots of roads and cramped tracks, war zone with munitions where your delivery of munitions can help one side (but if you're not careful, you could be killed or your train confiscated or destroyed), logging call, mining town (with steep elevation to deal with). These could be implemented like dungeon crawl branches, though that requires some sort of greater reward at the end of them. (Special prestige car that elevates your ranking?)
		○ Look up model railroad layouts for this sort of stuff. I could even put Dad's layout in it...
		
		
		
	• 1.0.0 - Retirement: After a certain number of turns, you retire, getting a score.


White - Owned train (cars)
Blue - Third party cars that you've been granted control over
Orange-red - Third party cars you are NOT given control over.


