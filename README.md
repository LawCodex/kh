# Cambodia — LawCodex

Part of [LawCodex](https://github.com/LawCodex). **Status: no texts published yet.** No usable
official source of Cambodian legislation in machine-readable Khmer text could be found (checked
2026-10-12/13). This repository documents what was tried and what would be needed.

## Sources checked

| Source | Result |
|---|---|
| Ministry of Justice legal database `cambodiajustice.gov.kh` | No response (TCP timeout over HTTPS, HTTP 502 over HTTP). No Internet Archive captures of its PDFs. |
| Ministry of Justice `moj.gov.kh`, Council of Ministers `ocm.gov.kh` (Royal Gazette / legal documents), Constitutional Council `ccc.gov.kh`, `cambodia.gov.kh`, `mfaic.gov.kh` | Every request is answered by a WAF page ("The requested URL was rejected", HTTP 200/403). Not circumvented. |
| National Assembly `nac.org.kh/files/<n>.pdf` (laws adopted by the Assembly) | Reachable. Sampled files are **image scans without a text layer**; the Constitution PDF (`files/1.pdf`) has a text layer, but its Khmer is broken: almost no COENG (subscript) signs, i.e. clusters such as រដ្ឋធម្មនុញ្ញ come out as រដធមមនុញញ. |
| Senate `senate.gov.kh` (Internet Archive copies) | `constitution-updated-on-october-2014.pdf` (archived 2016-10-20): Khmer text with hundreds of U+FFFD replacement characters (fonts without Unicode mappings). `cambodian-constitution-3-language.pdf` (2008): Khmer in legacy "Limon" font encoding (Latin glyphs, e.g. `rdæFmµnuBaØ`). English/French versions exist there but are outdated (pre-2014 amendments) and are translations, so they were not published. |
| Council of Ministers PDFs archived by the Internet Archive (`ocm.gov.kh/wp-content/uploads/2021/05/NN-YYYY.pdf`, ~1,100 files) | Sampled files are image scans (no text layer). |

`scripts/kh_check.py` is the check used to decide whether extracted Khmer text is usable
(Khmer characters present, COENG signs present, no replacement / legacy-encoding glyphs). Per
LawCodex policy no garbled text and no OCR output were published.

## What would be needed

- Access to the Ministry of Justice database (`cambodiajustice.gov.kh`) or the Council of
  Ministers' Royal Gazette with Unicode-text PDFs or HTML, e.g. by having the LawCodex crawler
  allow-listed by the WAF operators; or
- an official Unicode Khmer bulk export (constitution, codes — Civil Code, Code of Civil Procedure,
  Criminal Code, Code of Criminal Procedure — and laws/ច្បាប់ adopted since 1993); or
- a decision to accept quality-checked OCR of the official scans (not done here).
