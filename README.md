# dns-propagation-checker

Compare a DNS record's value across several resolvers from a CSV: CONSISTENT when all agree, DIFFERS with the disagreeing resolvers named — differing records first.

## How to run

```sh
python3 main.py records.csv
```

## Example output

```
www.example.com: DIFFERS (8.8.8.8=1.2.3.4, 1.1.1.1=5.6.7.8) (differs at: 1.1.1.1)
mail.example.com: CONSISTENT (8.8.8.8=9.9.9.9, 1.1.1.1=9.9.9.9)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
