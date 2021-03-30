# N2W-IT
This library convert numbers to italian words.\
For example: `73` -> `settantatré`.

It currently only supports converting numbers to **singular male** words.

## Installation ##
  - The easy way is to install from PyPI: `pip install n2w-it`.
  - Otherwise, you can download source package e manually install with: `pip install .` (desirable way),\
    or with: `python setup.py install`.

## Test ##
  - You can run: `python setup.py test`.
  - Otherwise you can directly test with: `unittest`.

## Usage ##
  - ### Command line ###
    The easy way to use, is to launch directly from terminal:
    ```
    $ n2w-it 73
    settantatré
    ```
    
  - ### Import ###
    You can import the libray in your code:
    ```
    from n2w_it import N2W_IT
    instance = N2W_IT()
    try:
      result = instance.number_to_words("73")
      print(result) #settantatré
    except Exception as exception:
      print(exception)
    ```
    
## APIs ##
  - The library supports number conversion in italian from:
    - Integer to cardinal: `int_to_cardinal(73)` -> `settantatré`.
    - Float to cardinal: `float_to_cardinal(73.37)` -> `settantatré virgola trentasette`.
    - Integer to ordinal: `int_to_ordinal(73)` -> `settantatreesimo`.
    - Roman to ordinal: `roman_to_ordinal("LXXIII")` -> `settantatreesimo`.

  - And a heuristic version:\
  _(If the `argument` passed is `None or Empty`, or the number format\
  is not found or valid, an `Exception` is raised.)_
    - `number_to_words("73")` -> `settantatré`.
    - `number_to_words("73.37")` -> `settantatré virgola trentasette`.
    - `number_to_words("73°")`  -> `settantatreesimo`.
    - `number_to_words("LXXIII")` -> `settantatreesimo`.
    - `number_to_words("LXXIII°")` -> `settantatreesimo`.