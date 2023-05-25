# yuptools.tools.dictools

Utility functions for working with CSV files and dictionaries.


- [load_csv_dict](#load_csv_dict)
- [dict_to_df](#dict_to_df)
- [save_dict_in_csv](#save_dict_in_csv)
- [AttrDict](#AttrDict)
- [make_attrdict](#make_attrdict)


---


## load_csv_dict

Loads a CSV file into a dictionary format.

```
csv_dict: Dict[Any, List[Any]] = load_csv_dict(
    csv_path: str,
    index_col: Any = 0,
)
```

### Input

- **csv_path** (*str*):
The path to the CSV file.

- **index_col** (*Any, optional*):
Specifies the column to be used as the index.
Default is *0*.

### Output

- **csv_dict** (*dict*):
The loaded data in dictionary format,
where the keys represent column names and the values are lists of column values.


---


## dict_to_df

Converts a dictionary to a Pandas DataFrame.

```
df: pandas.DataFrame = dict_to_df(
    dictionary: Dict,
    index_col: Any = None,
)
```

### Input

- **dictionary** (*dict*):
The dictionary to be converted to a DataFrame.

- **index_col** (*Any*):
Specifies the column to be used as the index.
Default is *None*.

### Output

- **df** (*pandas.DataFrame*):
The converted DataFrame.


---


## save_dict_in_csv

Saves a dictionary as a CSV file.

```
save_dict_in_csv(
    dictionary: Dict,
    save_dir: str,
    save_name: str,
    index_col: Any = None,
)
```

### Input

- **dictionary** (*dict*):
The dictionary to be saved.

- **save_dir** (*str*):
The directory where the CSV file will be saved.

- **save_name** (*str*):
The name of the CSV file.

- **index_col** (*Any*):
Specifies the column to be used as the index.
Default is *None*.

### Output

- *None*


---


## AttrDict

A dictionary subclass that allows attribute-style access to its keys.


---


## make_attrdict

Converts a dictionary into an attribute-accessible dictionary.

```
attrdict: AttrDict = make_attrdict(
    dictionary: Dict,
)
```

### Input

- **dictionary** (*dict*):
The dictionary to be converted.

### Output

- **attrdict** (*dict*):
The converted dictionary with attribute-style access to keys and values.
