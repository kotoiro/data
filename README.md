# Kotoiro upstream data

Snapshots of the upstream data that [Kotoiro](https://github.com/kotoiro)'s built-in dictionaries and word data are built from, kept exactly as upstream published it. Kotoiro's app build downloads a pinned snapshot and converts it, so any build can be made again from the same files, and anyone can check that they are upstream's own: each file's SHA-256 is the one upstream published.

One file is derived instead, where the original can't be kept: `cefrj-1.6.tsv`, from the CEFR-J Wordlist, whose terms allow making another word list from it but don't mention redistribution. The workflow makes it from the original with [`scripts/cefrj.py`](scripts/cefrj.py), keeping only what Kotoiro reads, and the release notes give the original's URL and SHA-256.

## Releases

Each release, `upstream-YYYY.MM.DD`, is named after the day's JMdict it holds, and carries:

| File | What | Licence |
|---|---|---|
| `JMdict_e.gz` | [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project), English only, as the EDRDG published it that day | [CC BY-SA 4.0](https://www.edrdg.org/edrdg/licence.html) |
| `english-wordnet-2025.xml.gz` | [Open English WordNet](https://github.com/globalwordnet/english-wordnet), 2025 edition | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `wn3.1.dict.tar.gz` | [Princeton WordNet](https://wordnet.princeton.edu/) 3.1's database, for its sense frequencies, which Open English WordNet doesn't have | [WordNet licence](https://wordnet.princeton.edu/license-and-commercial-use) |
| `jiten_freq_global.csv` | [Jiten](https://jiten.moe/frequency-dictionaries)'s global frequency list, built from anime, drama, film, novels, visual novels and manga, as Jiten served it that day: for how common each Japanese word is, which JMdict tags only coarsely | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `large_en.msgpack.gz`, `large_zh.msgpack.gz` | [wordfreq](https://github.com/rspeer/wordfreq) 3.2's lists of how common each English and Chinese spelling is | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `_chinese_mapping.msgpack.gz` | The table wordfreq maps traditional Chinese to simplified with, since it counts only simplified | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `1_1_all_fullalpha.zip` | The [BNC lemma list](https://ucrel.lancs.ac.uk/bncfreq/flists.html): English counted by dictionary form and part of speech, for sharing out wordfreq's count of a spelling among the words it can be | [CC BY-SA 2.0 UK](https://creativecommons.org/licenses/by-sa/2.0/uk/) |
| `cefrj-1.6.tsv` | Derived from the [CEFR-J Wordlist](https://www.cefr-j.org/download.html) 1.6: each word's Headword, part of speech and CEFR level, A1 to B2 | [CEFR-J's terms](https://www.cefr-j.org/download.html) |
| `octanove-vocabulary-profile-c1c2-1.0.csv` | The [Octanove Vocabulary Profile C1/C2](https://github.com/openlanguageprofiles/olp-en-cefrj) 1.0: words at C1 and C2 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `jlpt-n5.csv` to `jlpt-n1.csv` | Jonathan Waller's JLPT lists, with each word's JMdict entry number, from [stephenmk/yomitan-jlpt-vocab](https://github.com/stephenmk/yomitan-jlpt-vocab)'s `original_data/n5.csv` to `n1.csv` | Waller's: Creative Commons BY; the entry numbers: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `NGSL_12_stats.csv`, `NAWL_12_lemmatized_for_teaching.csv`, `TSL_12_stats.csv`, `BSL_120_stats.csv` | The [NGSL family](https://www.newgeneralservicelist.com/word-lists)'s word lists: the New General Service List 1.2, the New Academic Word List 1.2, the TOEIC Service List 1.2 and the Business Service List 1.20 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `cedict_1_0_ts_utf-8_mdbg.txt.gz` | [CC-CEDICT](https://cc-cedict.org/wiki/), Chinese to English, as MDBG published it that day | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `Unihan.zip` | The [Unihan database](https://www.unicode.org/reports/tr38/) of Unicode 18.0.0: for how often each reading of a Chinese character is used, and its usual reading, which choose the first of CC-CEDICT's entries for a character | [Unicode License v3](https://www.unicode.org/license.txt) |
| `ejdic-hand-txt.zip` | [EJDict](https://github.com/kujirahand/EJDict) v2.0.1, English to Japanese | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |
| `SHA256SUMS` | Each file's SHA-256 | |

The [snapshot workflow](.github/workflows/snapshot.yml) fetches them on the first of each month, and whenever it is run by hand. It checks every file but JMdict, Jiten's list and CC-CEDICT against its SHA-256 in [`pinned.sha256`](pinned.sha256), the CEFR-J Wordlist before deriving from it, that Jiten's list starts with its header, and that CC-CEDICT's header still names the format and licence Kotoiro relies on. It publishes nothing when that day's JMdict already has a release. Releases from `upstream-2026.10.29` carry Princeton WordNet, those after it Jiten's list, and those after `upstream-2026.10.30` the wordfreq, BNC, CEFR, JLPT and NGSL files, and CC-CEDICT, Unihan and EJDict.

## Attribution

- JMdict is the property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), and is used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).
- Open English WordNet is made by its [contributors](https://github.com/globalwordnet/english-wordnet), starting from Princeton WordNet.
- WordNet 3.1 Copyright 2011 by Princeton University. All rights reserved. Its licence and disclaimer head each of its files.
- Jiten's frequency list is made by [Jiten](https://jiten.moe) from the Japanese media it analyses, and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- wordfreq's data is by Robyn Speer, from Google Books Ngrams, Wikipedia, the Leeds Internet Corpus, ParaCrawl, OpenSubtitles, Twitter and the SUBTLEX lists of Marc Brysbaert et al., which are freely available data. Its README lists each source and its terms.
- The BNC lemma list is from Leech, G., Rayson, P. and Wilson, A. (2001), *Word Frequencies in Written and Spoken English: based on the British National Corpus*, Longman, as published by [UCREL, Lancaster University](https://ucrel.lancs.ac.uk/bncfreq/).
- The CEFR-J Wordlist Version 1.6. Compiled by Yukio Tono, Tokyo University of Foreign Studies. Its copyright is Tono Laboratory's.
- The Octanove Vocabulary Profile C1/C2 is made by [Octanove Labs](http://www.octanove.com/).
- The JLPT lists are compiled by [Jonathan Waller](http://www.tanos.co.uk/jlpt/), with JMdict entry numbers added by stephenmk. The JLPT publishes no word lists: these are his reconstruction.
- The New General Service List and the New Academic Word List are by Browne, C., Culligan, B., and Phillips, J.; the TOEIC Service List and the Business Service List by Browne, C. and Culligan, B.
- CC-CEDICT is made by its [contributors](https://cc-cedict.org/wiki/) and published by [MDBG](https://www.mdbg.net/chinese/dictionary?page=cc-cedict), and builds on CEDICT, Copyright (C) 1997, 1998 Paul Andrew Denisowski.
- The Unihan database is © Unicode, Inc., and is used under the [Unicode License v3](https://www.unicode.org/license.txt). Unicode and the Unicode Logo are registered trademarks of Unicode, Inc. in the U.S. and other countries.
- EJDict (ejdict-hand) is kept by [kujirahand](https://kujirahand.com/web-tools/EJDictFreeDL.php), with corrections from its users, and starts from `ejdic`, an English–Japanese dictionary file once given free to schools.

Each file stays under its own licence; the snapshots change nothing in them, and the derived list keeps its original's terms and credits it.
