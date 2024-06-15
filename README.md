# megascan_houdini19.5_USD_plugin (Windows)

This is a modification to the Houdini Megascans plugin (Windows) so that you can import varients and assets using the component builder method (Solaris).
You will need to install Quixel Bridge to use this mod

## Megascans 4.6 Installation for Houdini 19.5 
1. Open Quixel Bridge and download the houdini plugin by going to Edit > Manage Plugins > Houdini 4.6 and download the plugin
2. As this is not a vaild version for 19.5 you will have to mannually point to the plugin in you houdini 19.5 .env file or copy the old MegascansPlugin.json (might be in documents > Houdini19.0 > packages if you install for a previous version) into your packages folder in documents > Houdini19.5
3. If you do not have any of these manually create a packages folder and add the MegascansPlugin.json
4. Modify the .json file to point to the install location for your MSLiveLink
5. Launch Houdini 19.5 and check that Megascans is available the upper tabs
6. import an asset to check if the plugin works

## Mod Installation
1. Create a orig folder and create a backup of all the files you will modify
2. in C:\MegaScan\Library\support\plugins\houdini\4.6\MSLiveLink\scripts\python\MSPlugin\Utilities (or where-ever you installed) replace USDVarient.py
3. in C:\MegaScan\Library\support\plugins\houdini\4.6\MSLiveLink\scripts\python\MSPlugin\AssetImporters replace Import3D.py
4. if you also want the atlas splitter to work with geometry in solaris you can replace AtlasSplitter.py in C:\MegaScan\Library\support\plugins\houdini\4.6\MSLiveLink\scripts\python\MSPlugin\Utilities However this quite janky. This will only work when using "Use Atlas Splitter" on the plugin. If you check import Asset to USD stage it will only import the material node.
I suggest not to copy this if you only want the splitter to make node in the /obj context

This should now create extra component builder nodes with all the variants connected.
