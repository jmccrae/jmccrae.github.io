# Your 'References' Section Sucks! 

... but don't worry, so do most papers.

This is a guide about how to use BibTeX to manage your references, focusing on
ACL-format and computer science publications. It is based on my experience as a reviewer and seeing
many, many publications with horrible reference sections. The references section
of your work is not a trivial part of your paper, it is a critical part of your
work, that should be prepared with the same care as the rest of your paper.


## Sin 1: Protect your titles

The most common issue I see is that titles of papers are not properly are 
not in the correct case. BibTeX will automatically adapt the case of titles
so that they fit the style of the publication venue. For example, ACL wants titles
to be in sentence case, while other venues want them to be in title case. You
need to explicitly tell BibTeX to protect the case of certain words in titles,
as follows

```bibtex
@inproceedings{smith2020awesome,
  title = {An Awesome Approach to {NLP} Tasks},
  author = {Smith, John and Doe, Jane},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year = {2020},
}
```

If you don't do this, BibTeX will convert "NLP" to "Nlp" or "nlp", which is
wrong. You should protect any acronym, proper noun, or any word that should
not be changed.

## Sin 2: Poor source of .bib files

Many people use Google Scholar to find publications and it has a feature to get
BibTeX entries. DO NOT USE IT! The BibTeX entries from Google Scholar are often
incomplete or incorrect. Instead, use the following sources:

- **DBLP**: A computer science bibliography website that provides high-quality
  BibTeX entries. (https://dblp.org/)
- **ACL Anthology**: For NLP papers, the ACL Anthology provides accurate BibTeX
    entries. (https://aclanthology.org/)
- **Publisher websites**: Many publishers provide BibTeX entries for their papers.
  Check the paper's page on the publisher's website.
- **DOI to BibTeX converters**: Use services like CrossRef (https://www.crossref.org/)
  or doi2bib (https://www.doi2bib.org/) to get BibTeX entries from DOIs.

## Sin 3: Incomplete entries

Another common issue is that entries in the `.bib` file are incomplete. At a
minimum, you should provide the following fields for each entry type:

- `@article`: `author`, `title`, `journal`, `year`, `volume`, `number`, `pages`
- `@inproceedings`: `author`, `title`, `booktitle`, `year`, `pages`
- `@book`: `author` or `editor`, `title`, `publisher`, `year`
etc.

Make sure to fill in all relevant fields. Missing information can make it
difficult for readers to locate the referenced work. This can normally be fixed
by using good sources as above.

## Sin 4: Overuse of arXiv

A reference to arXiv should only be used for papers that have not passed peer review.
A paper that has not passed peer review should probably not be cited in the first place,
so find the peer-reviewed version of the paper and cite this.

## Sin 5: Citation as a noun

In most citation styles it is not correct to use the citation as a noun, e.g.,
"In (Smith et al., 2020), they show that...". Instead, you should use the correct
LaTeX command to cite the paper as part of the sentence, for example:

```latex
\citet{smith2020awesome} show that...
```

Here is a table of common citation commands and their outputs:

| Command | Output |
|---------|--------|
| `\citep` | (Smith et al., 2020) |
| `\citet` | Smith et al. (2020) |
| `\citealp` | Smith et al., 2020 |
| `\citeyearpar` | (2020) |
| `\citeposs` (ACL only) | Smith et al.'s (2020) |

Some citations styles use different commands such as `\shortcite` or `\newcite`,
so check the documentation of the style you are using.

For IEEE style citations, it **is allowed** to use the citation as a noun, e.g.,
"In [1], they show that...". I don't like this **but** it is allowed.

## Sin 6: Not Grouping References

If you wish to reference multiple papers at once, do not write each reference
separately like this: (Smith et al., 2020), (Doe et al., 2019), (Johnson, 2018).
Instead, group them together in a single citation command like this:

```latex
\citep{smith2020awesome, doe2019great, johnson2018fantastic}
```

This will produce a single citation with all the references grouped together,
like this: (Smith et al., 2020; Doe et al., 2019; Johnson, 2018).
