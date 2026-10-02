# Arrangements

The directories whose files comprise the arrangements of the candidate TRO declarations.

Each directory holds a copy of the files in the one before it, plus the files its row adds.

| Directory | Adds | Where the added files came from |
| --- | --- | --- |
| [`0-staged/`](0-staged) | `download.sh`, `analyze.py`, `package.sh` | Written for this repository. |
| [`1-downloaded/`](1-downloaded) | `data.csv` | Written for this repository; nothing was downloaded. |
| [`2-analyzed/`](2-analyzed) | `results.txt` | Made by running `analyze.py`. |
| [`3-packaged/`](3-packaged) | `package.zip` | Made by running `package.sh`. |
