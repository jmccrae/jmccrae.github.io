#let n(num, decimal: ".", thousands: ",") = {
  let parts = str(num).split(".")
  let decimal_part = if parts.len() == 2 { parts.at(1) }
  let integer_part = parts.at(0).rev().clusters().enumerate()
    .map((item) => {
      let (index, value) = item
      return value + if calc.rem(index, 3) == 0 and index != 0 {
        thousands
      }
    }).rev().join("")
  return integer_part + if decimal_part != none { decimal + decimal_part }
}

#let d = n.with(decimal: ".", thousands: ",") // English Style

#show heading: set text(font: "Linux Biolinum")

#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommend resume text size is from `10pt` to `12pt`
// #set text(
//   size: 12pt,
// )

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/

#set par(justify: true)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}

#let cv = yaml("_data/cv.yaml")

#let publications = yaml("_data/publications.yaml")

#let total_assigned = cv.funding.map(t => t.assigned).sum()

= John P. McCrae

#grid(
  columns: (70pt, 1fr),
  gutter: 10pt,
  [#image("me.jpg")],
  [
#h(1fr) #box[#image("_img/noun-mail-6923091.svg", height: 0.7em)] john\@mccr.ae |
#box[#image("_img/github-mark.svg", height: 0.7em)] #link("https://github.com/jmccrae")[github.com/jmccrae] | 
#box[#image("_img/noun-globe-6593229.svg", height: 0.7em)] #link("https://john.mccr.ae")[https://john.mccr.ae] \
#h(1fr) *Location*: #cv.city, #cv.country \
#h(1fr) *Citizenship*: #cv.citizenship \
#h(1fr) *Date of Birth*: #cv.date_of_birth \
#h(1fr) *Gender*: #cv.gender 
])

== Achievements
#chiline()

- Leading researcher in natural language processing, knowledge graphs and linked data.
- Obtained €#d(total_assigned) in funding, including IRC Consolidator Laureate Award, Co-ordinator of H2020 Project, Collaborative projects with Fidelity Investments, Huawei and Genesys.
- #publications.len() publications at EMNLP, COLING, LREC etc. (#cv.google_scholar.citations Citations; h-Index: #cv.google_scholar.h_index). #link("https://john.mccr.ae/publications")[Full Publication List].
- Supervised #cv.students.filter(s => s.completed).len() PhD students to completion (#cv.students.filter(s => not s.completed).len() ongoing).
- Chair and Founder of #link("https://2023.ldk-conf.org")[Language, Data and Knowledge Conference] Series.
- Led departmental self-assessment team to Athena SWAN Bronze Award (for gender equality).
- NUI Galway President's Award for Research Excellence.
- Lectured courses on Natural Language Processing, Knowledge Graphs, Linked Data and Semantic Web and the University of Galway and Bielefeld University using PyTorch, TensorFlow, NLTK, RDFlib, SPARQL, etc.

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
