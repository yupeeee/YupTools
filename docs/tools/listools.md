# yuptools.tools.listools

Utility functions for working with lists.


- [argmax_list](#argmax_list)
- [argmin_list](#argmin_list)
- [sort_str_list](#sort_str_list)
- [merge_list_of_lists](#merge_list_of_lists)
- [merge_lists_in_dict](#merge_lists_in_dict)


---


## argmax_list

Returns the index of the maximum value in a list.
If multiple elements have the same maximum value, the index of the first occurrence is returned.

```
max_idx: int = argmax_list(lst: List[Any],)
```

### Input

- **lst** (*list*):
List containing elements that can be compared by size, magnitude, etc.

### Output

- **max_idx** (*int*):
The index of the maximum value.


---


## argmin_list

Returns the index of the minimum value in a list.
If multiple elements have the same minimum value, the index of the first occurrence is returned.

```
min_idx: int = argmin_list(lst: List[Any],)
```

### Input

- **lst** (*list*):
List containing elements that can be compared by size, magnitude, etc.

### Output

- **min_idx** (*int*):
The index of the minimum value.


---


## sort_str_list

Sorts a list of strings alphabetically, considering numeric values within the strings.

```
sorted_str_list: List[str] = sort_str_list(
    str_list: List[str],
    return_indices: bool = False,
)

sorted_str_list: List[str], indices: List[int] = sort_str_list(
    str_list: List[str],
    return_indices: bool = True,
)
```

### Input

- **str_list** (*list*):
The list of strings to be sorted.

- **return_indices** (*bool, optional*):
Specifies whether to return the sorted indices along with the sorted strings.
Default is *False*.
  - If *True*, a tuple containing the sorted strings and the corresponding indices will be returned. 
  - If *False*, only the sorted strings will be returned.

### Output

- **sorted_str_list** (*list*) (, **indices** (*list*)):
The sorted list of strings,
or a tuple containing the sorted list of strings and the corresponding indices (if ***return_indices*** is *True*).


---


## merge_list_of_lists

Merges a list of lists into a single list.

```
merged_list: List[Any] = merge_list_of_lists(
    list_of_lists: List[List[Any]],
)
```

### Input

- **list_of_lists** (*list*):
The input list of lists.

### Output

- **merged_list** (*list*):
The merged list.


---


## merge_lists_in_dict

Merges all the lists in a dictionary into a single list.

```
merged_list: List[Any] = merge_lists_in_dict(
    dictionary: Dict[Any, List[Any]],
)
```

### Input

- **dictionary** (*dict*):
The input dictionary.

### Output

- **merged_list** (*list*):
The merged list.
The order of the merged list is determined by the order of the input dictionary keys.
