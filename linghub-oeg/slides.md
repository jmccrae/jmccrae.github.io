% Linghub: Reconciling Heterogeneous Metadata about Language Resources
% John P. McCrae
% 15th April 2015

# Problem

Many sources of information about language resources

# Datahub

(Mostly) linked data

# LLOD cloud diagram

# LRE Map

Collected from conference participants

Quality is an issue

# META-SHARE

Highly curated resources

Complex metadata

# CLARIN VLO

Collected from many partners

Metadata scheme is unique to each source

# Linghub

Goal: Make all these data available on the same portal

# Data collection

|:----------:|:-----------:|
| Datahub    | via API     |
| LRE Map    | Linked Data |
| META-SHARE | XML dump    |
| CLARIN VLO | OAI-PMH     |

# Data collected

| Source     | Records    | Triples    | Triples/Records |
|:-----------|:----------:|:----------:|:---------------:| 
| META-SHARE | 2,442      | 464,572    | 190.2           |
| CLARIN     | 144,570    | 3,381,736  | 23.4            |
| Datahub    | 218        | 10,739     | 49.3            |
| LRE Map    | 5,712      | 79,576     | 13.9            |

# Conversion

META-SHARE and CLARIN have different and complex XML schemas

# LIXR

"Lightweight Invertible XML to RDF"

A Scala DSL to quickly transform XML to RDF

# LIXR Example - Input
    
    <cmd:CMD xmlns:cmd="...">
       <cmd:Header>
          <cmd:MdCreator>Bernhard Jackl
          </cmd:MdCreator>

To

    <#Header> a dcat:CatalogRecord ;
      dc:creator "Bernhard Jackl" .

# LIXR Example - Definition

    cmd.CMD --> (
      node("Header") (
        a > dcat.CatalogRecord,
        handle(cmd.Header),
        ... ))

    cmd.Header --> (
      handle(cmd.MdCreator),
      ... )

    cmd.MdCreator --> (
      dc.creator > content)

# Benefits of LIXR

![Lines of code per tag](lixr-locs.png)

# Data harmonization

Most properties are still plain text.

Difficult to query, different expressions.

# Solution

Use state-of-the-art word sense disambiguation

Harmonize a small number of properties:

* Language
* Type (e.g., Corpus, Lexicon)
* Rights (License)
* Usage (intended or secondary)

# Results

| Property   | Record Count     | Triples  | Accuracy |
|:-----------|:----------------:|:--------:|:--------:|
| Access URL |  91,615 (91.6\%) | 191,006  | n/a      |
| Language   |  50,781 (50.7\%) | 98,267   | 99.85%   |
| Type       |  15,241 (15.2\%) | 17,894   | ??       |
| Rights     |   3,080 (3.0\%)  | 8915     | 95.8%    |
| Usage      |   3,397 (3.4\%)  | 4,530    | 98-99%   |

# Duplication

### Inter-repository duplication

Errors or multiple versions/parts of the same data

### Intra-repository duplication

Double recording of resource 

# Inter-repository duplication

| Resource   | Duplicate by Title | Duplicate by URL |
|:-----------|:------------------:|:----------------:|
| CLARIN*    | 50,589             | 20               |
| Datahub    | 0                  | 55               |
| META-SHARE | 63                 | 967              |

\* Same contributing institute

# Intra-repository duplication

| Resource    | Resource    | Duplicate Titles | Duplicate URLs | Both    |
|:------------|:-----------:|:----------------:|:--------------:|:--------|
| CLARIN      | CLARIN*     | 1,202            | 2,884          | 0       |
| CLARIN      | Datahub.io  | 1                | 0              | 0       |
| CLARIN      | LRE-Map     | 72               | 64             | 0       |
| CLARIN      | META-SHARE  | 1,204            | 1,228          | 28      |
| Datahub.io  | LRE-Map     | 59               | 5              | 0       |
| Datahub.io  | META-SHARE  | 3                | 0              | 0       |
| LRE-Map     | LRE-Map     | 763              | 454            | 359     |
| LRE-Map     | META-SHARE  | 91               | 51             | 0       |
| All         | All         | 3,395            | 4,686          | 387     |

\* Other contributing institute

# Next steps

More data sources (ELRA, ISLRN, LDC, OLAC)

Harmonize more properties (author, subject/topic)

# Try yourself

http://linghub.org/
