# SEsocial

A python repository for verifying and generating swedish social security numbers.

## Installation

`pip install SE-social`

## Usage

```python
from sesocial import se

se.verify("yymmddxxxx") # Returns True or False

se.gender("yymmddxxxx") # Returns Male or Female

se.generate() # Returns format yymmddxxxx
```

## License

This project uses the MIT License. See [LICENSE](LICENSE "LICENSE")
