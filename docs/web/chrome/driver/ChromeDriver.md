# yuptools.web.chrome.driver.ChromeDriver

Provides various methods to interact with a web page using the Chrome browser. \
Note: The locator strategies (***find_element_by*** and ***find_elements_by***)
accept values such as
*"ID"*, *"CLASS_NAME"*, *"CSS_SELECTOR"*, *"TAG_NAME"*, *"NAME"*, and *"XPATH"*.
These values are constants defined in the ***By*** class from the
***selenium.webdriver.common.by*** module.


- [Properties](#properties)
- [Attributes](#attributes)
- Methods
  - [close_driver](#close_driver)
  - [wait](#wait)
  - [go](#go)
  - [current_url](#current_url)
  - [get_element](#get_element)
  - [get_elements](#get_elements)
  - [does_element_exist](#does_element_exist)
  - [click](#click)
  - [input](#input)
  - [get_value](#get_value)
  - [get_text](#get_text)


---


```
ChromeDriver(
    time_to_wait: float = default_wait,
    time_to_sleep: float = default_sleep,
)
```

## Properties

- **time_to_wait** (*float*):
Time to wait for elements to appear on the page (in seconds).
Default is *default_wait (=60.)*.

- **time_to_sleep** (*float*):
Time to sleep between actions (in seconds).
Default is *default_wait (=1.)*.


## Attributes

- **driver** (*selenium.webdriver.Chrome*):
Chrome WebDriver.


## Methods


### close_driver

Closes the Chrome WebDriver and quits the browser.

```
driver = ChromeDriver(...)

driver.close_driver()
```


### wait

Sets the implicit wait time and sleeps for the specified sleep time.

```
driver = ChromeDriver(...)

driver.wait()
```


### go

Navigates to the specified URL in the Chrome browser.

- **url** (*str*):
The URL to navigate to.

```
driver = ChromeDriver(...)

driver.go(
    url: str,
)
```


### current_url

Returns the current URL of the web page.

```
driver = ChromeDriver(...)

current_url: str = driver.current_url()
```


### get_element

Finds and returns a single element on the web page
based on the specified locator strategy and value.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

```
driver = ChromeDriver(...)

element: Any = driver.get_element(
    find_element_by: str,
    element_value: str,
)
```


### get_elements

Finds and returns multiple elements on the web page
based on the specified locator strategy and value.

- **find_elements_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **elements_value** (*str*):
The value of the locator strategy.

```
driver = ChromeDriver(...)

elements: Any = driver.get_elements(
    find_elements_by: str,
    elements_value: str,
)
```


### does_element_exist

Checks if an element exists on the web page
based on the specified locator strategy and value.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

```
driver = ChromeDriver(...)

exist: bool = driver.does_element_exist(
    find_element_by: str,
    element_value: str,
)
```


### click

Finds an element on the web page
based on the specified locator strategy and value,
and clicks on it.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

```
driver = ChromeDriver(...)

driver.click(
    find_element_by: str,
    element_value: str,
)
```


### input

Finds an input element on the web page
based on the specified locator strategy and value,
clears it, and enters the specified input value.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

- **input_value** (*str*):
The value to enter in the input element.

```
driver = ChromeDriver(...)

driver.input(
    find_element_by: str,
    element_value: str,
    input_value: str,
)
```


### get_value

Finds an element on the web page
based on the specified locator strategy and value,
and returns the value of the specified attribute.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

- **element_attribute** (*str*):
The attribute whose value to retrieve.

```
driver = ChromeDriver(...)

value: Any = driver.get_value(
    find_element_by: str,
    element_value: str,
    element_attribute: str,
)
```


### get_text

Finds an element on the web page
based on the specified locator strategy and value,
and returns its text content.

- **find_element_by** (*str*):
The locator strategy to use (e.g., *"ID"*, *"CLASS_NAME"*, *"XPATH"*).

- **element_value** (*str*):
The value of the locator strategy.

```
driver = ChromeDriver(...)

text: Any = driver.get_text(
    find_element_by: str,
    element_value: str,
)
```
