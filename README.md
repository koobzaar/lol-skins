
# League of Legends Skins Database

> **If any skin crash / doesn't start your game, PLEASE, submit an issue to this repository. There's too many skins and we're not capable of testing everything.**

This repository aims to provide a centralized and easily accessible location for all in-game skins available for League of Legends. The skins are offered in formats compatible with custom skin applications.

The purpose of this project is not to undermine the custom skin scene within League of Legends. Instead, we aim to provide a solution for players who have been unable to afford skins since the introduction of Vanguard. Previously, these players relied on tools like LolSkin or R3nzSkin, which are no longer viable.

Using custom skins does not confer any competitive advantage, as they are only visible to the player utilizing them. 

The creator of this repository believes that with the implementation of predatory practices in skin sales — exemplified by exclusive skins like the Faker skin, which cost as much as three months' wages in some regions — Riot has restricted access to certain content for a significant portion of its player base. 

> We hold that gaming culture should be inclusive and accessible, not just a privilege for those who can afford it.

We currently have all skins.

## Contributing (read carefully before creating a PR)

We welcome contributions! If you would like to submit skins to this repository, please create a pull request. Ensure that your submission includes:

- The skin files in a format compatible with CSLOL or Fantome. We only accept .fantome files (basically .zip files renamed to .fantome).
- Proper attribution to the original creator of the skin.

You don't know how to extract skins? Don't worry! You can contribute by:

- Renaming all skins that has wrong names or some trash that was left in the way.
- Starring this repository.

### What is a .fantome file?

From [Fantome](https://github.com/LeagueToolkit/Fantome) developers:

A .fantome file is simply a .zip file that the extension has been renamed with the .fantome. It's a format used specifically for League of Legends mods that are meant to be installed using the Fantome mod manager.

The internal structure of a .fantome file must follow this specific organization:
```
ModName.fantome (renamed from .zip)
├── RAW/           # For porting legacy mods - avoid for new mods
├── WAD/           # Main folder for mod files, mirrors LoL's structure
└── META/          # Mod metadata
    ├── info.json  # Required: Contains mod info (name, author, version, etc.)
    └── image.png  # Optional: Preview image for the mod
```

Key points about .fantome files:
1. They are technically a renamed ZIP archive
2. They must contain the standard folders (RAW, WAD, META) and required metadata
3. The WAD folder should mirror League of Legends' file structure for proper mod installation
4. The META folder must include an info.json file with basic mod information
5. Modern mods should primarily use the WAD folder structure for best performance and file size

### I have some skins, but they're all in .zip and I don't know how to convert to .fantome 

**Step 1**: Enable File Extensions

1. Open File Explorer (Windows key + E)
2. Click on "View" at the top menu
3. Click on "Show" in the ribbon
4. Look for "File name extensions" checkbox
5. Check the box to show file extensions

Step 2: Change the File Extension

1. Right-click on your mod's .zip file
2. Select "Rename"
3. The file name will be highlighted, and you'll now see ".zip" at the end
4. Move your cursor to the end of the filename
5. Replace ".zip" with ".fantome"
6. Press Enter
7. Windows will show a warning about changing file extensions
8. Click "Yes" to confirm the change

## Downloading everything

Go to https://github.com/koobzaar/lol-skins/releases and download the most recent League of Legends Skins.7z. Extract it using 7zip/NanaZip or any other compressor that you like.


## How to Use

To use a skin in-game, simply download your desired skin from this repository. You can then apply it using of the following tool:

 - [CSLOL](https://github.com/LeagueToolkit/cslol-manager)
  - [Fantome](https://github.com/LeagueToolkit/fantome)

Follow the installation instructions provided with these tools to successfully implement the skins.

## Credits

All content available in this repository has been sourced from the r/LoLCustom community, with full credit given to its creators. Additionally, many skins have been contributed directly by community members. This repository is community-maintained.

## Donation

Pix: b2763e55-ac97-4963-83e9-d9827caed2de
Ko-Fi: https://ko-fi.com/koobzaar
## Disclaimer

This project is not endorsed by Riot Games and does not represent the views or opinions of Riot Games or any of its affiliates. Riot Games and all related properties are trademarks or registered trademarks of Riot Games, Inc. Additionally, this repository is not affiliated with the moderators of r/LoLCustom.

