# SEsocial

A python repository for verifying and generating swedish social security numbers.

## Installation

There is an issue where you can't import the library on newer versions.
Attention! The generate function doesn't exist in the 1.0.0 version.

`pip install SE-social==1.0.0`

## Usage

```python
from sesocial import se

se.verify("yymmddxxxx") # Returns True or False

se.gender("yymmddxxxx") # Returns Male or Female

se.generate() # Returns format yymmddxxxx
```

## License

This project uses the MIT License. See [LICENSE](LICENSE "LICENSE")
