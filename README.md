# SEsocial

A python repository for verifying swedish social security numbers.

## Installation

`pip install SE-social`

## Usage

```python
from sesocial import se

se.verify("yymmddxxxx") # Returns True or False

se.gender("yymmddxxxx") # Returns Male or Female
```

## License

This project uses the MIT License. See [LICENSE](LICENSE "LICENSE")
