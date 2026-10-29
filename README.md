# Kotoiro upstream data

Snapshots of the upstream data that [Kotoiro](https://github.com/kotoiro)'s built-in dictionaries are built from, kept exactly as upstream published it. Kotoiro's app build downloads a pinned snapshot and converts it, so any build can be made again from the same files, and anyone can check that they are upstream's own: each file's SHA-256 is the one upstream published.

## Releases

Each release, `upstream-YYYY.MM.DD`, is named after the day's JMdict it holds, and carries:

| File | What | Licence |
|---|---|---|
| `JMdict_e.gz` | [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project), English only, as the EDRDG published it that day | [CC BY-SA 4.0](https://www.edrdg.org/edrdg/licence.html) |
| `english-wordnet-2025.xml.gz` | [Open English WordNet](https://github.com/globalwordnet/english-wordnet), 2025 edition | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `SHA256SUMS` | Each file's SHA-256 | |

The [snapshot workflow](.github/workflows/snapshot.yml) fetches them on the first of each month, and whenever it is run by hand. It checks Open English WordNet against its pinned SHA-256, and publishes nothing when that day's JMdict already has a release.

## Attribution

- JMdict is the property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), and is used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).
- Open English WordNet is made by its [contributors](https://github.com/globalwordnet/english-wordnet), starting from Princeton WordNet.

Each file stays under its own licence; the snapshots change nothing in them.
