Some python performance comparisons that I occasionally use for [my game](https://store.steampowered.com/app/3122220/Mr_Figs/).

They're pretty simple but they answer the questions I have at the time.

Run them with `python3 thefileyouwant.py`

Results will vary wildly per machine but it at least gives you _some_ idea of
the performance differences.

| file                                     | description                                                              | sample size | time                     |
|------------------------------------------|--------------------------------------------------------------------------|-------------|--------------------------|
| [Tuple vs List](tuple-vs-list-access.py) | Compares access time of lists v tuples (tuples are supposedly faster)    | 50 million  | list ~3.4s, tuple ~3.47s |
| [Set vs List](set-vs-python-in.py)   | Compares "in" time of Set v lists (sets are supposedly faster)           | 50 million  | list ~8.6s, set ~5.50s |
