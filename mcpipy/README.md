mcpipy
======

https://www.stuffaboutcode.com/2013/11/coding-shapes-in-minecraft.html

https://wiki.vg/Minecraft_Pi_Protocol

https://www.stuffaboutcode.com/p/minecraft-api-reference.html

https://github.com/zhuowei/RaspberryJuice

https://github.com/GitHub-User228/mcpi2/blob/master/src/example.py



Python scripts for controlling Minecraft Pi Edition on Raspberry Pi, many of them as highlighted at mcpipy.com

This is a collection of python scripts that can be used to control Minecraft Pi Edition running on Raspberry Pi, 
or alternatively on a CraftBukkit server using the RaspberryJuice plugin, or RaspberryJamMod (some only work
on RaspberryJamMod).

Most (if not all) of the scripts are NOT of my own creation, but rather were created by others and collected to 
make it easy for others to enjoy them.  The scripts are unmodified with a few exceptions:

1. A comment was added near the top of each file noting the author and original URL where it was posted.
2. The mcpi python libraries are assumed to be in the "mcpi" folder and require this as a prefix to import.  
   As needed, scripts are updated to comply with this.
3. Minor formatting/bug fixing may be done to make the script run under both Python 2.7 and 3.x.
4. Minor compatibility updates. 


        67: cobblestone_stairs
            - 0, 8: ascending x+
            - 1, 9: ascending x-
            - 2, 10: ascending z-
            - 3, 11: ascending z+
            - 4, 12: ascending x+, upside down
            - 5, 13: ascending x-, upside down
            - 6, 14: ascending z-, upside down
            - 7, 15: ascending z+, upside down