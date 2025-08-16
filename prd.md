
Alpha Games — PRD

1. Vision
You were supposed to impress Chloe with your AlphaX project.
You didn’t.
Now, instead of graduating, you’ve been thrown into the deadly Alpha Games.
You are Contestant #67 with $67,000,000 of debt.
Survive three deadly school-themed challenges.
Win and claim $67,670,000, and your Alpha High School Diploma.
Lose once, and you get shot.

2. Core Pillars
School Satire is Deadly Serious — the setting is funny, the consequences are not.
One Mistake = Death — every round has an instant elimination state.
Simple and Readable — big bold text, clear instructions, no guessing.
Six-Seven Identity — 67 in timers, money, player identity.
Playable in <10 minutes — so failure makes you instantly want to retry.

3. Core Loop
Intro Scene → debt + expulsion story. 
Challenge → rules appear, player plays.
Fail → death (red flash, gunshot, “ELIMINATED”).
Success → proceed to next round.
Survive all 3 → prize screen.

4. Controls
Keyboard:
WASD / Arrow Keys → Move
Space → Jump (Glass Bridge only)
Mouse → Trace (Honeycomb)

5. Visual Theme
Environments: All levels feel like warped school settings. Chalk lines, gym floors, desks, banners.
Player Character: WHEN I SAY PLAYER, assume that it is player.png moving along the areas, facing toward the game so it's his backside. except for in Honeycomb game scene 02, it's just the cursor mouse, not the player doing it. 

UI: Large text banners, countdowns, elimination text.
Audio:
Tension music loops.
Gunshot sound for elimination.
Cracking/glass breaking SFX.

6. Scenes & Gameplay

Scene -01: Main Menu. 
Visuals:
Black background. Glitched Alpha School crest. Refer to Alphacrest.png
UI:
Title: “ALPHA GAMES”
Options: [START] [QUIT]
REFER TO FILE inro.md 

Scene 00: Intro
Visuals:
Screen fades from black.
A red counter ticks up until it shows: $67,000,000.
Text on Screen:
Your AlphaX project was not good enough for Chloe.  
You’ve spent four years doing absolute shit. You aren’t an expert, you have only 10 followers on TikTok, and you are NOT graduating dawg.  
 
Unless you survive the Alpha Games. Then, you will graduate. But if you lose… you will DIE!  

UI:
“You are Contestant #67.”
“Press any key to begin.”
Function: Key press → load RLGL.

Scene 01: Give Feedback, Receive Feedback (red light green light)
Visuals:
School hallway
Chloe Teacher at finish line. Faces away during green”give feedback”, turns during red, "receive feedback” 
Gameplay:
Timer: 67 seconds.
Green “giving” Phase: player can move.
Red "receiving" Phase: player must stop.
If player moves while red → death sequence:
Screen flash red.
Gunshot SFX coming from the teacher.
Text: “ELIMINATED — Moved during red. When it was time to receive feedback, you gave it instead.”
Fade to Game Over.
If the player reaches the finish line in time → “CLEARED — Proceed.” → load Honeycomb.
UI:
Top: “RED LIGHT GREEN LIGHT — Contestant 67.”
Timer countdown.
Banners: GREEN → “MOVE.” RED → “STOP.”

Scene 03: Honeycomb
Visuals:
Dark classroom. One desk under spotlight.
On desk: honeycomb cookie with random etched shape.
Gameplay:
Timer: 67 seconds.
Player traces shape with mouse cursor.
If cursor leaves path → cookie cracks → death sequence:
Crack sound.
Gunshot SFX.
Text: “ELIMINATED — Shape broken. You must not be an expert.”
If timer expires → same elimination.
Success → cookie glows gold. “CLEARED — Proceed.” → load Glass Bridge.
UI:
Top: “HONEYCOMB — Contestant 67.”
Timer circle around cookie.
Banner: “TRACE THE SHAPE.”

Scene 04: Glass Bridge
Visuals:
Suspended path with 7 rows of tiles (left/right). ½ tiles is tempered glass, the other is breakable glass. There is no visual indication, but every 5 seconds, light shines across the tiles so you can tell if it reflects a bit based on whether its tempered glass or not. 
Gameplay:
Timer: 67 seconds.
Player must jump from row to row.
Wrong tile → shatters → player falls → death sequence:
Glass break sound.
Gunshot SFX as screen flashes red.
Text: “ELIMINATED — Tile broke.”
Safe tiles → continue.
Final platform reached in time → “CLEARED — YOU SURVIVED.” → Win Screen.
UI:
Top: “GLASS BRIDGE — Contestant 67.”
Timer countdown.
Banner: “CROSS.”

Scene 05: Game Over
Visuals:
Blackboard wall with contestant numbers.
“67” is crossed out in red chalk.
UI:
Large: “ELIMINATED.”
Small: “Press any key to retry.”
Function: Reload current challenge.

Scene 06: Win Screen
Visuals:
Spotlight on piles of cash stacked on gym floor.
A diploma sits on top, stamped “67.”
Text:
YOU SURVIVED.  
Prize: $67,670,000  
Thank you for your participation, Contestant 67.  

Function: Any key → return to main menu.

