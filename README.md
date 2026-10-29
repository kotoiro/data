# Kotoiro upstream data

Snapshots of the upstream data that [Kotoiro](https://github.com/kotoiro)'s built-in dictionaries are built from, kept exactly as upstream published it. Kotoiro's app build downloads a pinned snapshot and converts it, so any build can be made again from the same files, and anyone can check that they are upstream's own: each file's SHA-256 is the one upstream published.

## Releases

Each release, `upstream-YYYY.MM.DD`, is named after the day's JMdict it holds, and carries:

| File | What | Licence |
|---|---|---|
| `JMdict_e.gz` | [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project), English only, as the EDRDG published it that day | [CC BY-SA 4.0](https://www.edrdg.org/edrdg/licence.html) |
| `english-wordnet-2025.xml.gz` | [Open English WordNet](https://github.com/globalwordnet/english-wordnet), 2025 edition | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `wn3.1.dict.tar.gz` | [Princeton WordNet](https://wordnet.princeton.edu/) 3.1's database, for its sense frequencies, which Open English WordNet doesn't have | [WordNet licence](https://wordnet.princeton.edu/license-and-commercial-use) |
| `jiten_freq_global.csv` | [Jiten](https://jiten.moe/frequency-dictionaries)'s global frequency list, built from anime, drama, film, novels, visual novels and manga, as Jiten served it that day: for how common each Japanese word is, which JMdict tags only coarsely | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `SHA256SUMS` | Each file's SHA-256 | |

The [snapshot workflow](.github/workflows/snapshot.yml) fetches them on the first of each month, and whenever it is run by hand. It checks both WordNets against their pinned SHA-256s and that Jiten's list starts with its header, and publishes nothing when that day's JMdict already has a release. Releases from `upstream-2026.10.29` carry Princeton WordNet, and those after it Jiten's list.

## Attribution

- JMdict is the property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), and is used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).
- Open English WordNet is made by its [contributors](https://github.com/globalwordnet/english-wordnet), starting from Princeton WordNet.
- WordNet 3.1 Copyright 2011 by Princeton University. All rights reserved. Its licence and disclaimer head each of its files.
- Jiten's frequency list is made by [Jiten](https://jiten.moe) from the Japanese media it analyses, and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Each file stays under its own licence; the snapshots change nothing in them.
