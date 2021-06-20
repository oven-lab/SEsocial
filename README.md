# SEsocial

A python repository for verifying and generating swedish social security numbers.

## Installation

### Easy:

`pip install SE-social`

### Advanced:

`git clone http://github.com/WaldemarBjornstrom/SEsocial.git`

Then go to the SEsocial directory you just downloaded and copy the sesocial folder into your project.

## Usage

```python
from sesocial import se

se.verify("yymmddxxxx") # Returns True or False

se.gender("yymmddxxxx") # Returns Male or Female

se.generate() # Returns format yymmddxxxx
```

## License

This project lies under the MIT License. See [LICENSE](LICENSE "LICENSE")
