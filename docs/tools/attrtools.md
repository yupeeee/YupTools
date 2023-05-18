# yuptools.tools.attrtools

Utility functions for retrieving attributes of an object.


- [get_attr](#get_attr)


---


## get_attr

Retrieves the value of a nested attribute from an object.

```
obj: Any = get_attr(
    obj: Any,
    attrs: str,
)
```

### Input

- **obj** (*Any*):
The object from which to retrieve the attribute.

- **attrs** (*str*):
The string representing the nested attribute path, separated by dots.
If any attribute in the nested path does not exist, an *AttributeError* is raised.

### Output

- **obj** (*Any*):
The value of the nested attribute.
