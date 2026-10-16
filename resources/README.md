# Resources

The files [`generate-candidates.sh`](../generate-candidates.sh) generates the candidate TRO declarations from.

| File | Role | Where it came from |
| --- | --- | --- |
| [`arrangements/`](arrangements/README.md) | The sets of files the candidates record as arrangements. | Described in its README. |
| [`TRO_UTILS_VERSION.txt`](TRO_UTILS_VERSION.txt) | The release of `tro-utils` the image installs. | Chosen for this repository. |
| [`readme-trs-declaration.jsonld`](readme-trs-declaration.jsonld) | The TRS declaration for candidates 02 and 03. | Based on the example in the `tro-utils` README. |
| [`trs-key.asc`](trs-key.asc) | The dummy GPG key that candidate 03 is signed with. | Generated 2026-10-02 (UTC) with GnuPG. |
| [`trs-key-passphrase`](trs-key-passphrase) | The passphrase protecting `trs-key.asc`. | Chosen with `trs-key.asc`. |
