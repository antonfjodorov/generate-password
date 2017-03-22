# generate-password
Terminal "plugin" to quickly generate cryptographically strong passwords.

## Installation
### Linux
- Clone repo into some_folder
- Create symlink to _generatePassword.py_. Place symlink in e.g. `/usr/local/bin` to make it runnable from the command line
- You will probably have to make _generatePassword.py_ executable `chmod +x`

### Mac & Win users
Contact me to add installation instructions here

## Code
Char space: uppercase ASCII, lowercase ASCII, digits and %`\'()*+-,./:;<>=!_&~{}|^?$#@"
Random number generator: [os.urandom(1)](https://docs.python.org/3.4/library/os.html#os.urandom).

## Examples
| # | Command | Output | Description |
| - | - | - | - |
| 1 |`generatePassword`| `U($mfeLNwv` | 10 random characters (10 is default)|
| 2 |`generatePassword 20`| `:doAV@YzS18pos:e@.no` |20 random chars|
| 3 |`generatePassword omit uppercase`|`qtpfx-!f5*`|10 chars, no uppercase chars|
| 4 |`generatePassword omit asdfghjk1`|`}Oe~Gix={T`|10 chars, excluding specified list of chars|

Other character groups you can omit (like in #3) are _uppercase_, _lowercase_, _digits_ and _special_.
