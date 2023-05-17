# yuptools.tools.pathtools

Utility functions for working with files and directories.


- [mkdir](#mkdir)
- [rmdir](#rmdir)
- [join_path](#joinpath)
- [ext](#ext)
- [ls](#ls)


---


## mkdir

Creates a new directory at the specified path. 
If the directory already exists, the function does nothing and does not raise an error.

```
mkdir(path: str,)
```

### Input

- **path** (*str*):
The path where the directory should be created.


---


## rmdir

Removes a directory and its contents at the specified path.
**This operation is irreversible and permanently deletes the directory and its contents.**
Use with caution.

```
rmdir(path: str,)
```

### Input

- **path** (*str*):
The path of the directory to be removed.


---


## join_path

Joins multiple path components into a single path.

```
joined_path: str = join_path(path_list: List[str],)
```

### Input

- **path_list** (*list*):
List of path components to be joined.

### Output

- **joined_path** (*str*):
The joined path.


---


## ext

Extracts the file extension from a file path, including the dot.

```
fext: str = ext(path: str,)
```

### Input

- **path** (*str*):
The file path.

### Output

- **fext** (*str*):
The file extension, including the dot (e.g., ".txt").


---

## ls

Lists files and directories in a directory specified by the path.

```
file_list: List[str] = ls(
    path: str,
    fext: Optional[str] = None,
    sort: bool = True,
)
```

### Input

- **path** (*str*):
The path of the directory to list.

- **fext** (*str, optional*):
Optional file extension filter.
If specified, only files with the specified extension will be returned.
Default is *None*.
  - If ***fext*** is *None* or an empty string, all files and directories will be returned.
  - If ***fext*** is set to *"dir"*, only directories (folders) will be returned.
  - If ***fext*** is set to a specific file extension (e.g., *"txt"*), only files with that extension will be returned.

- **sort** (*bool, optional*):
Specifies whether to sort the file list alphabetically.
If *True*, the list will be sorted.
Default is *True*.

### Output

- **file_list** (*list*):
A list of file and directory names.
