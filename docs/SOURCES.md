# Sources

The graph begins with scholarly editions of ancient texts. Its source material is the surviving documentary record associated with Girsu, available through digital catalogue records and transliterations. The project's work is to turn those edited texts into explicit, evidence-linked interpretations that can be used computationally.

“Source” can mean several things here. There is the ancient inscribed object, the edition through which it is read, the digital file supplied to the authoring process, and the canonical record produced from that file. They should not be treated as interchangeable.

## Girsu and its documents

Girsu is the ancient Sumerian city at modern Tello in southern Iraq. It belonged to the larger state of Lagash, alongside Lagash itself, at modern al-Hiba, and Nigin. The same name can therefore refer to a political territory or to a particular settlement. A document associated with the Girsu administration need not come from the settlement of Lagash. The [British Museum's account of Gudea and the Lagash state](https://www.britishmuseum.org/collection/object/W_1903-1012-3) makes this geography clear.

The site's history extends beyond the period represented by this collection. Girsu was an important third-millennium religious centre associated with Ningirsu. French excavations began in 1877 under Ernest de Sarzec. The [French Ministry of Culture's introduction to Tello](https://archeologie.culture.gouv.fr/proche-orient/en/tello-formerly-girsu) describes this archaeological setting.

The collection's principal historical setting is Ur III, the Third Dynasty of Ur, broadly the twenty-first century BCE. The administrative documents survive because institutions recorded particular acts and responsibilities: goods received or issued, work and personnel, inventories, obligations, balances and legal matters. They give unusually detailed evidence for everyday administration. Their detail is organised around what ancient record-keepers needed to record, rather than the categories a modern historian might wish to investigate.

The current canonical records are predominantly administrative. They include 8,979 accounts, 3,494 receipts, 1,090 expenditure records, 325 personnel lists and 232 inventories. There are also 321 legal records and 233 letters, together with 2,434 records classified as other and 1,301 whose genre is null. These are classifications of the current preserved records. A less specific genre does not mean that a document has no useful content.

Within those documents are people identified by names, offices, kinship or institutional associations; collective workforces; institutions; places; deities; commodities; and the relationships that connect them to particular entries. The graph records 5,818 institution mentions and 16,137 place mentions, for example. Those are occurrences in texts, not a count of distinct institutions or settlements.

## Ancient provenance and modern custody

A catalogue's provenance field is not the same thing as an archaeological excavation record. Some objects have secure find contexts; others were acquired through the antiquities trade and attributed to a site. The British Museum's [BM 15243](https://www.britishmuseum.org/collection/object/W_1896-0408-438), for example, is catalogued as found/acquired at Girsu and separately recorded as purchased in 1896. The wording “excavated at Girsu” would lose that distinction.

Nor is a source's provenance the same as the places named in its inscription. A Girsu document can refer to goods intended for another place. A museum collection identifies modern custody, not an ancient institution, and a set of texts sharing a site label is not necessarily one ancient archive.

The project preserves source-local mentions and their roles separately from catalogue provenance. It does not infer institutional membership or a common archive simply from the Girsu site group.

## CDLI, BDTNS and the edited text

The upstream acquisition code identifies CDLI, the [Cuneiform Digital Library Initiative](https://cdli.earth/about), as the primary digital provider. CDLI publishes catalogue information and textual material for cuneiform artifacts across many periods and sites. The P-number identifiers used throughout this repository belong to that cataloguing system. They identify documentary objects, not historical people.

BDTNS, the [Database of Neo-Sumerian Texts](https://bdtns.cesga.es/index.php?p=about), is a major scholarly resource for the Neo-Sumerian corpus. Its development incorporates the work of cataloguers, editors and contributors and includes collaboration with CDLI. These resources are not independent authors of every reading they transmit. Published editions, transliterations, corrections and editorial attributions remain part of the intellectual provenance of the text.

The project used BDTNS in an earlier, restricted comparison of 100 short administrative texts, with 20 from each of five sites. The comparison code explicitly describes shared source traditions and a purposive sample. It is not evidence that the entire Girsu corpus was downloaded directly from BDTNS, nor a corpus-wide independent accuracy assessment.

The supplied texts are represented in ATF, the ASCII Transliteration Format. ATF is a notation for scholarly transliteration, not a translation, an image of the tablet or another ancient archive. It represents textual organisation and conventions for readings, damage, restoration and other editorial information. The [Oracc ATF primer](https://oracc2.museum.upenn.edu/doc/help/editinginatf/primer/index.html) explains those conventions.

Our use of “original text” means the exact digital input preserved for a record. It does not mean that the project holds the ancient original or has independently collated every reading against the physical object.

## The acquisition and selection record

The preserved upstream acquisition code records a CDLI content-negotiated API query for Ur III material on 7 October 2026. It describes a collection assembled over multiple requests, not an instantaneous snapshot of the service. The files named `cdli_cat.csv` and `cdliatf_unblocked.atf` are described as normalized projections of the acquired JSON. The code also identifies a December 2022 ORACC/ePSD2 corpus and lexicon as auxiliary resources.

In the upstream processing code, catalogue rows whose period starts with `Ur III` enter the text collection. The `site_group` field is formed from the catalogue's provenance label by removing the modern-place parenthesis and surrounding whitespace. It is a catalogue grouping, not a geographical inference made by the interpretation agents.

The later Girsu reconciliation uses the preserved `ur-iii-text.csv.gz` catalogue, containing 110,686 records. Its SHA-256 is:

```text
7a4db6cf899f228d99cf515bed31aca5a08dfb96a7a2f5ef0276d3f8073d3c06
```

The comparison selects `site_group == 'Girsu'` and then distinguishes rows with `atf_present == 'True'`. It makes no additional genre or date exclusions at that stage. The 30,256 Girsu catalogue IDs divide into 19,208 with saved ATF and 11,048 without it. The ATF-present set matches the registered source IDs exactly.

This provides an independently checked membership comparison against the preserved catalogue. The recovered catalogue is tied to the project's October 13 baseline by its hash. The acquisition code's account of the October 7 collection and this later byte-verified comparison are separate pieces of evidence. The original live-page receipt chain has not been freshly reverified here, and the comparison does not claim to recover the original activation selector. It would therefore be misleading to describe this release as a fresh download of every text currently offered by CDLI or BDTNS.

The supporting project records are the pinned [acquisition manifest code](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/reconstruction_inputs/ur/ur-iii-current/code/current_manifest.py), [catalogue-processing code](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/reconstruction_inputs/ur/ur-iii-current/code/pipeline.py), [site-label handling](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/reconstruction_inputs/ur/ur-iii-current/code/references.py), [catalogue receipt](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/operations/recovery/catalogue-20261019T2117Z.json) and [Girsu membership comparison](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/checkpoints/girsu-consolidated-20261029/catalogue/COMPARISON.json), together with its [catalogue provenance note](https://github.com/caiusdfolkerts/ur-reconstruction/blob/accb42db04a09233dc6795afab58ed041ab0b68d/checkpoints/girsu-consolidated-20261029/catalogue/README.md). These are historical acquisition references in the private production repository, not dependencies needed to read this release.

## What is available here

The release includes 18,409 current canonical interpretations and three archival selections. It also preserves the source registry and the dispositions of registered sources without a current interpretation. The 11,048 catalogue-only entries are available as documentary metadata rather than fabricated empty records.

There are 38,046 stored original-text witness rows across the 19,208 registered sources. This is not a count of distinct tablets. A source can have registered and canonical copies of its digital text, and 17,969 of those pairs are byte-identical. A single source can also include tablet, envelope and seal material. The reader resolves the exact witness used by an interpretation rather than treating all copies as interchangeable.

Editorial marks and source qualifications remain available through the record and its evidence. Adoption of a restoration as a default does not turn it into an intact reading, and a default is not a claim that all editors agree. The [method](METHODS.md) explains how these supplied texts became canonical records; [provenance](PROVENANCE.md) gives the exact release bindings and review histories.

## Attribution

This project builds on the scholarship that catalogued, published, transliterated and interpreted the underlying material, and on the institutions that made it accessible digitally. Creating structured interpretations does not transfer authorship of those readings to this repository. Source and edition attribution should travel with any downstream quotation or analysis.

For an introduction to the character and history of the wider corpus, see Manuel Molina's [“The Corpus of Neo-Sumerian Tablets: An Overview”](https://bdtns.cesga.es/PDFs/Molina_2008_BPOA_5.pdf). Its corpus statistics describe the time of publication and should not be substituted for the release counts above. Its broader Neo-Sumerian coverage also should not be confused with this project's particular catalogue selection.

No blanket new licence for the underlying editions is asserted here. Users should consult the relevant source providers and editions when planning redistribution or publication.
