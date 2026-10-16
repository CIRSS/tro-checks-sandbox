rows = open("data.csv").read().splitlines()
open("results.txt", "w").write(f"{len(rows)} rows\n")
