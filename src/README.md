
# Reproduce results
To reproduce the results follow these steps:

```
python3 generateMaps.py      # generate the maps in ../maps
```

Before the next step better remove all files in ../results

```
python3 generateResults.py   # run various algorithms on the maps and produce results in ../results

python3 generateCharts.py    # generate charts of the results in ../results
                             # requires matplotlib

python3 drawSolutions.py     # visualize solutions found in ../results
                             # requires tkinter and pyscreenshot
```