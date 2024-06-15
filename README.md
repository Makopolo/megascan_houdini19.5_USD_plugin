# megascan_houdini19.5_USD_plugin (Windows)

This is a modification to the Houdini Megascans plugin (Windows) so that you can import variants and assets using the component builder method (Solaris).
You will need to install Quixel Bridge to use this mod

## Megascans 4.6 Installation for Houdini 19.5 
1. Open Quixel Bridge and download the Houdini plugin by going to Edit > Manage Plugins > Houdini 4.6 and download the plugin
2. As this is not a valid version for 19.5 you will have to manually point to the plugin in your houdini 19.5 .env file or copy the old MegascansPlugin.json (might be in documents > Houdini19.0 > packages if you install for a previous version) into your packages folder in documents > Houdini19.5
3. If you do not have any of these manually create a packages folder and add the MegascansPlugin.json
4. Modify the .json file to point to the install location for your MSLiveLink
5. Launch Houdini 19.5 and check that Megascans is available in the upper tabs
6. import an asset to check if the plugin works

## Mod Installation
Create an orig folder and create a backup of all the files you will modify
in C:\MegaScan\Library\support\plugins\houdini\4.6\MSLiveLink\scripts\python\MSPlugin and **REPLACE** the files I have added in the repo.
 
**DO NOT** just copy and paste the whole folder as I have left out the python files that I haven't modified.
This should now create extra component builder nodes with all the variants connected as well as create mtlx materials in Solaris.
All Redshift materials have been updated for standard shader and USD. Also, make textures visible in the viewport.

If you are still confused you can watch this [video](https://supafried.com/technical-blog) on how to install 
