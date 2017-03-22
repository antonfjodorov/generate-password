# generate-password
Terminal "plugin" to quickly generate cryptographically strong passwords.

## Installation
### Linux
- Clone repo into whatever_folder
- Optional: copy whatever_folder/generatePassword.py to `~/src/` to keep a good folder structure.
- Make _generatePassword.py_ executable `chmod +x`
- Create symlink to _generatePassword.py_. To make file runnable from command line, place symlink in `/usr/local/bin`

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

## Todo
- Copy to clipboard function with import Tkinter

```
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append('i can has clipboardz?')
	r.destroy()
```