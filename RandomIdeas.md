# Random Game Ideas

## Unassorted / Miscellaneous
* Normal 'map' display is top-down view of train on tracks. Each engine/car taking up one character normally.
* EVEN BETTER!!! You can move around the world on foot. But you can get on or off you train. I wouldn't suggest jumping off a train that's going 100 mph though. This is less to let the player explore the world as it is to provide the feeling of being a little character riding atop a large machine. And lets you throw switches manually. Basically you are Buster Keaton in "The General".
* You can set brakes on an individual cars
* Potentially have tracks with too tight if curves, requiring you to tow along a smaller engine for retrieving cars off of those branches.
* Can have height, where if the ground Is heigher it will be in another color, like a relief map.
* Violating signals and other restrictions, assuming they don't cause an accident, will get you fined by the host railroad.
* Most cars will be owned by other companies, and you just ferry stuff around. However, some companies will not own rolling stock, and instead you can purchase it (and keep it on your train) for which you make greater profits, since its using more of your equipment and less of theirs.
* Plenty of Onomatopoeia:
    * Whistle (if implements. Perhaps you can be fined if in a yard and failing to whistle before moving) *SQUEEEEE*
    * Piston pumping, longer the faster the train goes. *CHUG*  *CHUG-A-CHUG* *CHUH-A-CHUG-A-CHUG-A-CHUG*. You could hear these for distant trains and be able to tell his fast they're going.
* The right part of the screen shows your current controls. If you're on the locomotive, it shows its controls. If you're on another car, it'll show the brakes. This means you could indepently control multiple locomotives.
* Obviously if you stand on tracks with a train coming, you'll get hit. If its an NPC crew who has time to react, they'll try as hard as possible to stop the train before it hits you. If it’s a train owned by the map's Railroad, they'll start fining you for disruption of their operations (if you live by jumping out of the way, that is).
* Locomotive controls show the settings, when you press a button to modify one, the rest of the locomotive controls go grey or disappear entirely, showing you the necessary information to modify just that one. Thus when you go to modify a control, you get all the information you need, but otherwise the locomotive controls are mostly unimpared by keycommands and labels
* Definitely allow connecting to active NPC trains.Ownership should exist at the car level, not train level and being able to connect to opponent trains and have a tug of war of locomotives I'd a cool sandbox feature. Of course if its a railroad train you'll be fined...
* Sounds have volume affected by distance. If you are in a high speed locomotive, you wont hear a distant train over your own engine.
* Have a trail of smoke which gratis the background of surrounding tiles (when they have nothing else to color)
* RPG Elements (HA!) - Players would get more attached to their progress if they start accumultating a handful of cars they always bring with them. They may have certain boosts (Caboose saves on, um, hotel stays???), while others allow for certain missions, or more profitable missions (two passenger cars instead means making twice as much on a passenger mission?)
* Also possible is turning the game more into an arcade design. I worry that, since there is no amulet of Yendor to capture, it will be difficult coming up with a compelling end game. Thus maybe I should go down an arcade route. Each map should be relatively short amount of time on it (5 minutes at most?). And instead you are an Engineer for a company who keeps getting assigned around to different parts of the company to take care of things. So each map starts with you outside the company building, and you can pick from amongst one or more locomotives to use to accomplish your objectives for that map. Once you fail or succeed at them, you move on to the next map. Thus each map requires you analyzing your available resources and objectives, and attempt to succeed as much as possible (evauate enough civilians out of an area before something happens, etc)
* On some maps, you can attack rival engineers and steal their already running nicely locomotive.
* Fugitive mode: You are on the run from the law. You use horses and locomotives to escape the lawmen and bounty hunters that are always close behind. Would be a wacky Steampunk-ish GTA feel as you commandeer horses and locomotives to stay out of their reach as long as possible.

White - Owned train (cars)
Blue - Third party cars that you've been granted control over
Orange-red - Third party cars you are NOT given control over.



## Steam Engine Mechanics
* Starting / Accelerating
  * Burn fuel (coal, fire, oil) in Firebox - _WILL_ be in the game. Player will need to do an action to fill the firebox up. It will burn fuel at a constant rate. It will impart heat to the water, and the burning fuel will (with a linear function) increase that temperature back up. I will not be modeling any other heat loss or efficincies, but if you're going to be stuck somewhere a bit, it may be advantageous to let the fire die down so that you're not wasting fuel, going into steam, that is then vented off or naturally cooled. (All the coal in the firebox is burnt up in 3 minutes.)
  * Water injection into the boiler - _WILL_ be in the game. It must be be kepter higher than the top of the firebox (or the firebox will melt, or the fusible plug will put out the fire if you have one installed), but low enough that there is room for steam to be stored. (Too little room, and you may have high PSI, but it can disappear very quickly as you open up the throttle. Even worse, if its WAY too high, it could be pulled into the cylinders, which probably significantly impacts power, if not damaging them. This is done manually (as in, its not automatic feed, you must open and close the valve)
  * Open the Cylinder Cocks - When the Cylinders are cold, they'll condense some of the water into steam. This water sitting in the cylinders would decrease their effectiveness and, probably, damage them if too much accumulated. Opening the cocks lets that water get drained/pushed out by steam as the cylinder runs. Once the cylinder is warmed up, and all the condensation is drained, you close them to get some extra strength from the cylinders. _WILL_ be in the game. But it will be somewhat optional, in that it won't damage the engine, but will affect power. So new players can skip this for a bit until they get more comfortable.
  * Throttle - _WILL DO_. Not sure how technically this functions, but if the train is at a dead stop and you open the throttle too much, you can spin the drivers (wheels), which can damage the track or the wheels/drive gear. (If you do this too much, it will slowly degrade the maintenance condition of the locomotive). The chance of spinning them would be a combination of weight you're trying to pull versus driving force versus weight of the locomotive. Done to an extreme it could cause a derailment (not sure the physics reason for this, but I read it in regards to Double-Heading.)
  * Johnson Bar - As the engine accelerates, it uses up steam from the boiler. As it moves faster, it exceeds the steam generation of the boiler, so the Johnson Bar reduces the length of the piston stroke for which steam is injected, down from 100% to 90 or 80%. THIS IS THE SAME AS THE REVERSER. You set it full one direction or the other for maximum power, but as you speed up you can ease off of it to use less steam, and thus use less water and fuel. _DEFINITELY IMPLEMENT_
• Stopping / Braking
  * Throttle is shut off and opened a crack - Already implemented the throttle, but will not worry about the 'open a crack for lubrication'.
  * Brakes - 


* Focus on steam locomotives, because that way you must manage steam pressure, firebox,etc. Avoid boiler explosions, keep fuel stocks, manipulate brakes
* Locomotives of the same design will all have every so slight differences in all their capacities, heat/power transfer rates, etc. When the Locomotive is instantiated in the game world, it will calculate all of these differences which will remain constant throughout its existance (minus any maintenance degredation). This should provide JUST enough variation that a player never gets into an exact routine of how the engine functions. Each time starting and stopping will act ever so slightly different.
* You will spin the driving wheels if you apply too much power and the locomotive has too much resistance, such as having way too many cars, or by having the brakes on all the cars. Spinning them too long damages the driving gear. At a certain point the damage both reduces power, and at higher speeds the gear will Continue to damage itself even with correct usage (because now that it is shaky, strain on it makes it worse), until eventually if its not fixed one side will snap, greatly reducing power.
* Power output is converted to acceleration. As your speed goes up, more power is required to achieve that acceleration (though maintaining speed is easier). That is why just starting out makes it easy to spin the wheels, because you have maximum acceleration, but as you increase speed it disappears as an issue.
* I saw reference to "Throttle Valve" which implies that the throttle is indeed a valve which controls the rate at which steam can be put into the um, throttle tube area (from which is flows into an open piston based on the johsnon bar setting.) The main point of this is that there is an intermediate steam area here. There is the water in the boiler, steam in the boiler, and steam in the throttle pipe. If the engine is going very fast with full throttle, and full johnson bar forward, then the steam likely cannot enter the throttle pipe as fast as it is exiting to the pistons, losing motive force due to reduced are pressure. Reducing the Johnson bar back means only part (the majority though) of the piston stroke pull from the throttle pipe, keeping pressure in the throttle pipe up.
* Fuel efficiency: Too much coal in the firebox means it only partially combusts, causing black smoke. Too little and firebox temperature drops.
* Classic Boiler explosion is when the firebox crown sheet overheats (not enough water). I'm guessing the sudden water hitting the fire causes the fire and water to flash explode into steam, causing the propulsion to fly the boiler hundreds of feet.
* The steam engine simulation should have one (or more) efficiency ratings, based on certain conditions. For example, steam engines have many lubrication points that should be periodically (daily I think) lubricated to insure maximal efficiency. The implication there is that not doing so, aside from wearing out the equipment faster, forces the equipment to work harder (loss of available power) to accomplish the same task when various surfaces have more friction happening to them. Thus, as one example, if the player does not lubricate the engine frequently enough, the engine's efficiency slowly drops. The player can do this, or they can hire a hostler to do the job for them frequently. (Which will also be the guy responsible for filling the tender with water and fuel
* Sand -> Could be an optional thing, to add a sander to increase speeding up and slowing down friction for the engine. The Hostler keeps it filled at a depot?
* All steam engine calculations have a random multiplier. Better engines are less affected by this.




## NPCs
* NPCs have different responsbilities depending on which ones you have, and which activities are optional or required:
    * Player only: Must run the engine, keep up steam pressure, do all filling of sand and such, and manage switches and brakes.
    * With Engineer: Player gives the engineer simple orders (rough speed directive, and stop), manages filling of fuel, and switches and brakes. Engineer runs the engine and keeps up steam pressure
    * With Engineer and Fireman: Fireman keeps up steam pressure, Engineer runs the engine, and the player does the rest.
    * With Engineer, Fireman, and Hostler: Fireman keeps up steam pressure, Engineer runs the engine, Hostler does lubrication and fuel filling (which no one else but the player would ever do), and the Player directs the engineer and throws switches/brakes.
    * With Engineer, Fireman, Hostler, and Brakeman: Fireman keeps up steam pressure, Engineer runs the engine, Hostler does lubrication and fuel filling, Brakeman activates car brakes and flips switches, and Player directs the engineer. (If this is crew not associated with the player, some outside force/directive/AI will be responsible for directiong the Engineer).
* It will be awesome to see an NPC locomotive going about its business... speeding up, stopping for the brakeman to get off and throw a switch, the Hostler to fill up the engine and lubricate it while stopped.
* Player vocal commands, to the NPC crew that is, would have a maximum range (a couple tiles). If the player is out of range of some but not all crew, the crew would echo it to the rest of the crew.
* Might be a cool thing to implement sooner rather than later.... an NPC crew whose job is to shuffle around a handful of cars while I do other things. Great part of an early demo version. Would be a good intro screen, where trains move around in the background with crews manning them appropriately.
* If the steam locomotive is annoying, then have the game start you with an engineer but thus less starting cash.
* I could see a scenario where players got annoyed with having to run a steam engine and its complexity. Thus if you want to, when you have the money, you can hire an engineer to run the engine for you, and he will listen to your commands. Of course he costs a salary, and is not as efficient as good player.
* This also functions to serve as an aspect of player advancement. Once financially successful, they can hire crew to run various aspects for them as a sorry of leveling up their train (or running multiple locomotives)? (called "Double Heading") Apparently that is risky, due to slippage causing damage or derailment
* Probably need a friendly brakeman NPC, because older trains without automatic air brakes would need someone putting the brakes on individual cars of a freight train, since the engine's brakes can only do so much.
* You could also hire, if you want, an NPC Fireman who shovels coal when needed. However, you do have to pay for such a person, so its up to you if you'd prefer the tradeoff of someone who knows what they're doing.
* Perhaps a much later version could allow you to even hire an engineer, and you become more of a passenger as you run around arranging deals and such.
* The brakeman could also be told to throw switches. It'd be awesome if you're the engineer, and you tell them what to do.
* On foot, if you walk into someone, you can push them one square over. However, that will anger them, and they may injure you.



## Maps, Missions, and Goals
* Analogous to normal Roguelikes, each train line is equivalent to a single dungeon level, procedurally generated. Rail yards = large rooms while lines connecting yards are equivalent to corrodors. Each level, being a different company's track, may have different operating conditions (cost more per turn to use their track, more or less other trains running around (potentially picking up the cars that you want to pick up for cash), different track quality.
* Different maps may have different themes, like a logging railroad or some such.
* Plot is you are an independent locomotive owner(like an owner operator semi truck driver) running on all these railroads, and you have to pay to use th`eir tracks.
* Certain lines can be serviced repeatedly, like passenger routes, but over time your earnings will decrease, and competitor reasons will move in forcing you to continue looking.
* Maybe the end goal is that you'll retire after certain number of maps or turns, and thus it's a race against to make enough money to retire comfortably.
* Locomotive factories exist here and there where you can buy new engines. Also, over time and poor use, your locomotives can be damaged, running worse, which you must get repaired at a depot.
* Certain cargos, especially passengers, require that you already own your own correct transportation car.
* Rare, random misfortune possibilities, like a car or some such on the tracks, and either you slam on the brakes, or you hit it. Broken tracks. Derailment up ahead. Other trains in the way. Cattle or wild animals on the tracks. Damsel in distress tied up on the tracks. Suddenly a river washing out a nearby bridge temporarily.
* Missions would not span maps. Once you leave one map, it will never exist again. If you fail to leave cars or cargo owned by someone else on the map before leaving it, you will be charged with the price of those cars and cargo. For each one, you can agree to pay it then or force them to sue you. Forcing them to sue you postpones having to pay immediately, but costs additional court and lawyer fees to fuel the postponement. This would not be something that the user would have direct control over; instead they would just be informed of the result when it happens. Plus, there is the slight risk that:
    * You do not know how long the lawsuit will last. It could end at a very inopportune moment. 
    * The judge could hand down punitive damages, further increasing the cost. 
    * The judge could dismiss the case (realllll lucky) and you pay only the court/lawyer fees.
