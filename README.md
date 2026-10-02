# tro-utils-checks

This repository makes TRO declarations with
[`tro-utils`](https://github.com/transparency-certified/tro-utils), checks them using
[`tro-checks`](https://github.com/transparency-certified/tro-checks), and reports what it
found. The report for each target is listed in [`reports/README.md`](reports/README.md).

This repository does not define its own checks. It performs those defined by the
`tro-checks` module on candidates `tro-utils` makes from the arrangements and resources in this repository.

The image installs the release of `tro-utils` named in [`Dockerfile`](Dockerfile), and the
candidates change with that release only when it is changed there.

## Key files

| File | What it is |
| --- | --- |
| [`arrangements/`](arrangements/README.md) | The sets of files the candidates record as arrangements. |
| [`resources/`](resources/README.md) | The other files the candidates are made from. |
| [`make-candidates`](make-candidates) | Script that uses `tro-utils` to create the candidates from the arrangements and resources. |
| [`candidates/`](candidates) | The candidates created by `make-candidates` and assessed by `tro-checks`. |
| [`candidates/manifest.json`](candidates/manifest.json) | Describes each candidate and lists the versions and tiers it targets. |
| [`reports/`](reports) | The reports of what the checks found. |
| [`Dockerfile`](Dockerfile) | Installs `tro-checks` and a particular release of `tro-utils`. |

## Running it

In the top-level directory of this repository, build the Docker image:

```
make build-image
```

Make the candidates, then regenerate the reports:

```
make build-candidates
make build-reports
```
