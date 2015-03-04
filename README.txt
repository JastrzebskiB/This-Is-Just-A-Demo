0) To start the game, use the RUNME.py file.

1) Requirements:
    Python 2.7.x (can be downloaded at https://www.python.org/downloads/release/python-278/)
    PyGame 1.9.1 (can be downloaded at http://www.pygame.org/download.shtml)
    
    PyGame is a Python implementation of the SDL library and should not cause any problems
    if you already have your own Python setup. If you are worried it would interfere or cause
    any issues, I strongly recommend using virtualenv to install PyGame and run the game.

2) Possible errors:
    In Windows environment, you might receive the following error message:
    
    "‘python’ is not recognized as an internal or external command"

   To resolve it, please follow these steps:
        * Click on the "Start" button
        * Type "PowerShell" in the "Search programs and files" field
        * Type "[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")" 
          (no quotes at beginning and end of the line) in the PowerShell
        * Close PowerShell, try running RUNME.py again.
        * If it does not help, reboot the computer and try running RUNME.py one more time.
    
    I DID NOT have a chance to test if/how the game runs in a OSX environment. Can not guarantee
    stability when running under that system, though I also do not expect there to be any 
    significant issues.
        
3) Graphics disclaimer:
    Due to the fact that the graphic designer I contracted to get original visual assets for the game
    delayed the deadline by a month and in the end backed out of the contract, part of the current 
    graphics are images that were found on the internet and modified heavily in an attempt to create
    a "minimalistic" (as opposed to going full-on "pixel-art" style) feeling about the game. 

    I am not fully satisfied with the graphics - I will play around with it and add/modify/replace 
    the assets. Please treat it as a "placeholder" for now - it's there to allow me to show you the 
    game itself and will be improved.
    
    The visuals will get changed either to open domain assets or (more likely) to ones created specifically
    for the game, pending my finding of a fitting graphics designer.
    
4) Why "release" in current state?
    As it is now, the code would suffice as an engine to support a game with play-through time limited only
    by how much content I would want to create.
    List of features that I intend to implement in the game over time (in a leisurely pace) includes:
        * adding more maps, quests, characters, kingdoms, humour and - last but not least - plot
        * adding a second row of units to accomodate archers, mages or support units (healers, bards etc.)
        * corollary of the above: add a "range" characteristic to units (i.e. archers can attack any enemy 
          units, melee units can attack only adjacent ones)
        * adding mana (or some other resource) and a set of skills that units could select from,
          instead of only a basic attack
        * adding a resource system and items
        * adding random encounters while travelling on the map (source of experience, chance to drop resources or items)
        
    The current version is basically a tutorial. Adding more content would likely do nothing to make me a better developer 
    (which is currently my priority over finishing the game), nor prove my ability to code - just my ability to create content.

5) Why use a game as a part of the portfolio?
    It started as a project I did for fun (and to learn) in my free time - originally all played out in the console, with no 
    graphics. Over time it grew and as of now it presents my ability to: learn new frameworks (PyGame); use OOP; deliver 
    well-written and thoroughly tested code (even if it's just manual testing...); plan and develop software from scratch.

6) Contact information:
    Błażej Jastrzębski
    jastrzebskib@gmail.com
