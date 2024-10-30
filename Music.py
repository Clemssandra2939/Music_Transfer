import os
import shutil
from pathlib import Path

def copy_mp3_files(parent_directory, output_directory):
    """
    Copy all MP3 files from a parent directory and all its subdirectories to the output directory.
    
    Args:
        parent_directory (str): Path to the parent directory containing music folders
        output_directory (str): Path to the output directory
    
    Returns:
        tuple: (number of files copied, list of any errors encountered)
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Convert parent directory to Path object
    parent_path = Path(parent_directory)
    
    files_copied = 0
    errors = []
    
    try:
        # Walk through the parent directory and all its subdirectories
        for root, _, files in os.walk(parent_path):
            for file in files:
                # Check if file is an MP3
                if file.lower().endswith('.mp3'):
                    source_file = Path(root) / file
                    try:
                        # Create unique filename if file already exists
                        base_name = file[:-4]  # Remove .mp3 extension
                        extension = '.mp3'
                        target_file = output_path / file
                        counter = 1
                        
                        # If file exists, add number to filename
                        while target_file.exists():
                            new_name = f"{base_name}_{counter}{extension}"
                            target_file = output_path / new_name
                            counter += 1
                        
                        # Copy file to output directory
                        shutil.copy2(source_file, target_file)
                        files_copied += 1
                        print(f"Copied: {source_file.relative_to(parent_path)} -> {target_file.name}")
                    except Exception as e:
                        errors.append(f"Error copying {file}: {str(e)}")
                        
    except Exception as e:
        errors.append(f"Error accessing directory {parent_directory}: {str(e)}")
    
    # Print summary
    print(f"\nOperation complete:")
    print(f"Files copied: {files_copied}")
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(error)
    
    return files_copied, errors

# Example usage:
if __name__ == "__main__":
    # Parent directory containing all music folders
    parent_dir = "mtp://Unisoc_Infinix_SMART_8_11661373CJ001739/"
    print(os.path.exists(parent_dir))
    
    # Output directory where MP3 files will be copied
    output_dir = "/home/sandra/Music"
    
    # Run the function
    copy_mp3_files(parent_dir, output_dir)