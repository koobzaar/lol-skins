# Contributing Guidelines

Thank you for your interest in contributing to our project! We value every contribution, whether it's fixing bugs, adding new skins, or improving documentation. This guide will help you understand how to contribute effectively and ensure your submissions align with our project standards.

## How to Contribute

### 1. Addressing Open Issues

We currently have a variety of skins, some of which may have bugs or be incomplete. Your expertise can significantly improve our collection:

- **Fix Existing Bugs**: If you notice any issues with current skins, such as crashing problems, model glitches, or animation errors, please help by submitting fixes.
- **Complete Missing Skins**: Some champions may have incomplete skin sets. If you can extract or create missing skins, your contributions are highly welcome.

### 2. Improving Existing Content

Even if you're not skilled in skin extraction or creation, you can still make valuable contributions:

- **Rename Mislabeled Skins**: Many skins may have incorrect or confusing names. Help by renaming them accurately according to their in-game counterparts.
- **Clean Up File Structure**: Remove any unnecessary files, folders, or metadata that don't belong in the skin packages.
- **Organize Skins**: Ensure skins are placed in the correct champion folders and follow our naming conventions.

### 3. Supporting the Project

- **Star the Repository**: This simple action helps increase the project's visibility and shows appreciation for the contributors' efforts.
- **Report Issues**: If you encounter problems but can't fix them yourself, creating detailed issue reports is extremely helpful.
- **Spread the Word**: Share the project with other League of Legends enthusiasts who might be interested in contributing or using custom skins.

## Submission Requirements

### 1. File Format

We exclusively accept skins in the .fantome format, which is compatible with both CSLOL and Fantome mod managers. Here's what you need to know:

- A .fantome file is essentially a .zip file with its extension renamed to .fantome.
- This format is specifically designed for League of Legends mods to be installed using the Fantome mod manager.
- Ensure your submission only includes .fantome files. We cannot accept other formats like .zip, .rar, or individual texture/model files.

### 2. Proper Attribution

- Always credit the original extractor of the skin, even if it's yourself.

### 3. Issue Reference

When your contribution addresses a specific issue:

- Mention the issue number in your pull request (e.g., "Fixes #123").
- Provide a brief description of how your submission resolves the issue.

### 4. Folder Structure

Maintaining a consistent folder structure is vital for the project's organization:

- Follow the existing folder hierarchy for all contributions.
- Place skins in their respective champion folders (e.g., `/Ahri/` for Ahri skins).
- If you believe a structural change would benefit the project, propose it comprehensively, showing how it would apply to ALL champions before implementation.

### 5. Pull Request Format

To ensure smooth integration of your contributions:

- Clone the repository to your local machine and make changes there.
- Create a new branch for your changes (e.g., `fix-ahri-star-guardian-skin`).
- Commit your changes with clear, descriptive commit messages.
- Push your branch to your fork and create a pull request from there.
- Provide a detailed description of your changes in the pull request.
- Do not upload single files directly through GitHub's web interface, as this can lead to integration issues.

## .fantome File Structure

Understanding the internal structure of a .fantome file is crucial for proper mod creation:

```
ModName.fantome
├── RAW/           # For porting legacy mods - avoid for new mods
│   └── (Legacy mod files, if any)
├── WAD/           # Main folder for mod files, mirrors LoL's structure
│   ├── DATA/      # Game data files
│   ├── Assets/    # Asset files (textures, models, etc.)
│   └── (Other LoL directories as needed)
└── META/          # Mod metadata
    ├── info.json  # Required: Contains mod info (name, author, version, etc.)
    └── image.png  # Optional: Preview image for the mod
```

Key points to remember:

1. The .fantome file is a renamed ZIP archive with a specific internal structure.
2. It must contain the standard folders: RAW (for legacy content), WAD (for main mod files), and META (for metadata).
3. The WAD folder should mirror League of Legends' file structure precisely for proper mod installation.
4. The META folder must include an info.json file with basic mod information such as name, author, and version.
5. Modern mods should primarily use the WAD folder structure for optimal performance and file size.
6. The RAW folder is mainly for backwards compatibility and should be avoided for new mods unless absolutely necessary.

## Converting .zip to .fantome

If you have skin mods in .zip format, follow these steps to convert them to .fantome:

1. **Enable File Extensions in Windows**
   - Open File Explorer (press Windows key + E)
   - Click on "View" in the top menu
   - In the "Show/hide" section, check the box for "File name extensions"

2. **Rename the File Extension**
   - Right-click on your mod's .zip file
   - Select "Rename" from the context menu
   - The file name will be highlighted, and you'll see ".zip" at the end
   - Carefully move your cursor to the end of the filename
   - Delete ".zip" and type ".fantome" instead
   - Press Enter to confirm
   - Windows will show a warning about changing file extensions; click "Yes" to proceed

3. **Verify the Internal Structure**
   - After renaming, open the .fantome file with a zip program like 7-Zip or WinRAR
   - Ensure the internal folder structure matches the required .fantome format (RAW, WAD, META folders)
   - If needed, reorganize the contents to comply with the structure outlined above

4. **Update Metadata**
   - In the META folder, create or update the info.json file with accurate mod information
   - Optionally, add a preview image named image.png in the META folder

By meticulously following these expanded guidelines, you'll help maintain the project's high standards of quality, organization, and usability. Your careful attention to detail in submissions will be greatly appreciated by both the maintainers and the community. Thank you for your valuable contributions to our custom skin collection!
