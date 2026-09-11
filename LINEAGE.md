# Project Lineage

## Canonical role

This repository is the **structured academic/evidence successor** for Stanley Osei-Wusu's 2024 news-summarization project family.

It follows the earlier public prototype:

- `stanleymay20/news-summarizer` — historical prototype, last active 2024-09-18.
- `stanleymay20/text-summarization-news-aggregation` — structured successor, created 2024-09-26.

The predecessor is intentionally preserved because it contains experimental implementation history that is not reproduced here.

## What this repository preserves and improves

The structured successor separates the main pipeline into modules:

- `src/data_collection.py` — NewsAPI ingestion;
- `src/preprocessing.py` — text cleaning/preprocessing;
- `src/summarization.py` — T5 abstractive summarization;
- `src/publishing.py` — WordPress publishing;
- `src/evaluation.py` — evaluation scaffold;
- `src/main.py` — orchestration;
- `report/` and `diagrams/` — academic/reporting evidence.

## Unique predecessor evidence retained in `news-summarizer`

The earlier notebook contains experimental capabilities that are not present in this repository's current `src/` implementation:

1. direct Reuters archive scraping in addition to NewsAPI;
2. TF-IDF extractive summarization alongside T5 abstractive summarization;
3. a Flask `/summarize` trigger endpoint.

Those features are preserved as historical evidence in the predecessor rather than being silently discarded or represented as implemented here.

## Current implementation boundaries

This repository should be treated as **academic / technical evidence**, not as a verified production deployment.

- The current summarization implementation is T5-based abstractive summarization. The README must not claim that the current modular `src/` code implements extractive summarization.
- `UNSPLASH_ACCESS_KEY` is currently checked by `src/main.py`, but there is no image-fetching implementation in the current source path.
- The workflow reference is stored at `github/workflows/deploy.yml`, not `.github/workflows/deploy.yml`; therefore it is **not an active GitHub Actions workflow**.
- The workflow reference also contains an obsolete `git push origin master` command while the repository default branch is `main`.

Do not activate publishing/scheduling automation until those behaviors are deliberately reviewed, external WordPress side effects are authorized, and a current CI/security baseline is added.

## Consolidation decision

**Status:** CANONICAL ACADEMIC SUCCESSOR / LINEAGE RESOLVED / NOT PRODUCTION-VERIFIED.

The predecessor may eventually be archived as a historical repository, but it should not be deleted because it contains unique experiment history. Archiving is a presentation decision, not a data-loss operation.
