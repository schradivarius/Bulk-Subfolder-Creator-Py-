# Bulk Subfolder Creator (Python)

A simple Python script to standardize folder structures by creating a subfolder inside a specified subfolder for every directory in a base path.

Useful for administrative, HR, or project file systems where many folders need the same internal structure.

## What it does
- Iterates through each folder in a base directory
- Looks for a specified subfolder
- Creates a new subfolder inside it if missing
- Reports how many folders were created, already existed, or missing the target subfolder

## Example
```
Base Path
├── Employee A
│   ├── Personal Documents
│       ├── Driver's License
├── Employee B
│   ├── Personal Documents
│       ├── Driver's License
```
## Configuration

Edit these variables in the script:

```python
base_path = r"FILE_PATH"
subfolder_name = "SUBNAME"
new_subfolder_name = "NEWSUBNAME"
```

## Requirements

Python 3.x

Standard library only (os)

## Notes

The script is safe to re-run.

Existing folders are not overwritten.