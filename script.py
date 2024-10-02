import os
import shutil
import sys

def get_folders(path):
    """Get all folders in the specified path"""
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def get_fantome_files(path):
    """Get all .fantome files in the specified path"""
    return [f for f in os.listdir(path) if f.endswith('.fantome')]

def main():
    # Get current directory folders
    current_folders = get_folders('.')
    
    # Get the path for .fantome files from user
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_fantome_files>")
        sys.exit(1)
        
    fantome_path = sys.argv[1]
    
    # Check if path exists
    if not os.path.exists(fantome_path):
        print(f"Error: Path '{fantome_path}' does not exist")
        sys.exit(1)
    
    # Get all .fantome files
    fantome_files = get_fantome_files(fantome_path)
    
    # Counter for moved files
    moved_files = 0
    
    # Check each .fantome file against folders
    for file in fantome_files:
        file_name = os.path.splitext(file)[0]  # Remove .fantome extension
        
        # Check against each folder
        for folder in current_folders:
            # If folder name is found anywhere in the file name
            if folder.lower() in file_name.lower():
                # Source and destination paths
                source = os.path.join(fantome_path, file)
                destination = os.path.join('.', folder, file)
                
                try:
                    # Move the file
                    shutil.move(source, destination)
                    print(f"Moved '{file}' to folder '{folder}'")
                    moved_files += 1
                    break  # Move to next file after successful move
                except Exception as e:
                    print(f"Error moving '{file}' to '{folder}': {str(e)}")
    
    print(f"\nOperation completed. {moved_files} files moved.")

if __name__ == "__main__":
    main()