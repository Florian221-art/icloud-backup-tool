# icloud-backup-tool
easy to use python tool to backing up any folder you want with automatic ZIP archiving

## Features
- Creates a backup of a specified source folder
- Maintains the directory structure in the backup
- Progress display using `tqdm`
- Automatically creates a ZIP archive
- Deletes temporary backup folders after successful archiving

## Requirements
The script requires Python 3 and the following modules:
- `os`
- `shutil`
- `datetime`
- `tqdm`

If `tqdm` is not installed, it can be installed with:
```sh
pip install tqdm
```

## Usage
1. **Adjust source and target directories:**
   Edit the following lines in the script to define the source and target folders:
   ```python
   source_folder = r"example directory"  # Source directory
   backup_folder = r"example directory"  # Target directory
   zip_Name = "iCloud"  # Name of the ZIP file
   ```
2. **Run the script:**
   ```sh
   python IcloudBackupper.py
   ```

## Example Output
```
Welcome to the iCloud Backup Program!
Creating backup...  [#####----------------] 25%
Backup successfully created
```

## Notes
- Ensure that the script has the necessary permissions to access the specified directories.
- If a file cannot be copied, an error message will be displayed.
- The script creates a timestamped backup directory and archives it as a ZIP file.

## License
This project is licensed under the MIT License.


