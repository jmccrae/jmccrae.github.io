#import "@preview/tada:0.1.0"

#show heading: set text(font: "Linux Biolinum")


// Uncomment the following lines to adjust the size of text
// The recommend resume text size is from `10pt` to `12pt`
// #set text(
//   size: 12pt,
// )

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

#set par(justify: true)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}

#let cv = yaml("_data/cv.yaml")

#let publications = yaml("_data/publications.yaml")

#let total_assigned = cv.funding.map(t => t.assigned).sum()

= John P. McCrae

john\@mccr.ae |
#link("https://github.com/jmccrae")[github.com/jmccrae] | #link("https://john.mccr.ae")[john.mccr.ae] \
#cv.city, #cv.country \ 
#h(1fr) *Citizenship*: #cv.citizenship \
#h(1fr) *Date of Birth*: #cv.date_of_birth \
#h(1fr) *Gender*: #cv.gender \
#h(1fr) *Languages Spoken:* '#for lang in cv.languages [
  #lang.name#if "level" in lang [ (#lang.level)],
]

== Achievements
#chiline()

- Obtained €#total_assigned in funding, including IRC Consolidator Laureate Award, Co-ordinator of H2020 Project, Collaborative projects with Fidelity Investments, Huawei and Genesys.
- #publications.len() publications. (#cv.google_scholar.citations Citations; h-Index: #cv.google_scholar.h_index). #link("https://john.mccr.ae/publications")[Full Publication List].
- Supervised #cv.students.filter(s => s.completed).len() PhD students to completion (#cv.students.filter(s => not s.completed).len() ongoing).
- Chair and Founder of #link("https://2023.ldk-conf.org")[Language, Data and Knowledge Conference] Series.
- Led departmental self-assessment team to Athena SWAN Bronze Award (for gender equality).
- NUI Galway President's Award for Research Excellence.
- Lectured courses on Natural Language Processing, Knowledge Graphs, Linked Data and Semantic Web and the University of Galway and Bielefeld University.

== Education
#chiline()

#for edu in cv.education  [ *#link(edu.url)[#edu.institute]* #h(1fr) #edu.date \
#edu.address\
#edu.degree
#if "title" in edu ["#edu.title" - Supervisor: #edu.supervisor]

]


== Work Experience
#chiline()

#for emp in cv.employment [
*#emp.institute* #h(1fr) #emp.date \
#emp.jobtitle

]

== Teaching
#chiline()

#for t in cv.teaching [*#t.title* (#t.role, #t.level, #t.institute) #h(1fr) AY
#t.AY

]

== Students
#chiline()

#for s in cv.students [
- *#s.name* - #if "title" in s ["#s.title"] (#s.degree, #s.year) #if "secondary" in s [(**secondary supervisor**)] #if not s.completed [(**ongoing**)]

]

== Funding
#chiline()

#let funding_data = cv.funding.map(f =>
  ("Name": f.name, "Funder": f.funder, "Date": f.date, "Amount": [#f.total (#f.assigned)])
)

#import tada: TableData, to-tablex

#to-tablex(tada.from-records(funding_data))

== Publications
#chiline()

#for paper in publications [
- #text(weight: "bold")[#if "url" in paper [ #link(paper.url)[#paper.title]] else [#paper.title]]. #if "author" in paper [ #paper.author.join(", ") ]
   #if "editor" in paper [ #paper.editor.join(", ") (eds) ]
   #if paper.type == "InProceedings" or paper.type == "Conference" or paper.type == "Workshop" [ _#paper.booktitle _ ]
   #if paper.type == "Article" [ _#paper.journal _ #if "number" in paper [ #paper.number ]#if "pages" in paper [ pp #paper.pages ] ]
   #if paper.type == "InCollection" [
     In: _#paper.booktitle _ #if "editor" in paper [ #paper.editor.join(", ") (eds) ]#if "pages" in paper [ pp #paper.pages ] ]
   #if paper.type == "Book" [
     _#paper.publisher _ ]
   #if paper.type == "Proceedings" [
     _#paper.publisher _ #if "series" in paper [ \- #paper.series ] ]
   #if paper.type == "PhDThesis" [ PhD Thesis for Graduate University of Advanced Studies (SoKenDai) ]
   #if paper.type == "Misc" [
     Technical Report: #paper.organization ]
    #if paper.type == "Patent" [
      Patent: #paper.note
    ] (#paper.year#if "accepted" in paper [, Accepted])
]



== Activities
#chiline()

#for a in cv.activities [
- #a
]

== Program Committees
#chiline()

#for pc in cv.program_committees [
- #pc
]

== Taught Students
#chiline()

#for s in cv.taught_students [
- #s.name, _"#s.title"_
]
