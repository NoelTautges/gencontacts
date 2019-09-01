# gencontacts

A script to easily generate lists of emails and phone numbers.

## Key Features

- Easy automation of brute force contact lists for tools like Google Contacts or Gmail-Enum
- Hashcat-like custom character sets
- Usable for any  email format or numbering plan

## Installation

**Python 3 is required.**

```bash
git clone https://github.com/NoelTautges/gencontacts
cd gencontacts
python3 gencontacts.py
```

## Usage

Use the --email and --phone parameters to make a template with the following character sets:
- ?l (lowercase letters)
- ?d (digits)
- ?a (lowercase letters + digits)
- ?1-4 (custom character sets 1-4, via --1-4)

The result will be an `itertools.product`-filled list of all the possible combinations of characters in the template!

```bash
# Saves a list of emails from geniusface0000@gmail.com  to geniusface9999@gmail.com to bobmcgee-emails.txt
python3 gencontacts.py --email "geniusface?d?d?d?d@gmail.com" --outfile bobmcgee-emails.txt

# Saves a CSV of contacts with phone numbers from +1 (608) 200-1131 to +1 (608) 999-1131 to bobmcgee-phones.csv
# Note the usage of a custom character set to comply with the restricts on central office codes in the North American Numbering Plan
python3 gencontacts.py --1 "23456789" --phone "+1608?1?d?d1131" --csv bobmcgee-phones.csv

# Passes a list of emails from geniusface0000@gmail.com to geniusface9999@gmail.com to Gmail-Enum in order to narrow down the possibilities
python3 gencontacts.py --email "geniusface?d?d?d?d@gmail.com" | Gmail-Enum -stdin -t 100 -o bobmcgee-verified-emails.txt
```

## Contributing

Pull requests are welcome.

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## TODO

- [ ] Make the CSV format less awful
- [ ] Better generation of phone numbers based on numbering plans
- [ ] Module support