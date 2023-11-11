---
---
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

= John P. McCrae

john\@mccr.ae |
#link("https://github.com/jmccrae")[github.com/jmccrae] | #link("https://john.mccr.ae")[john.mccr.ae] \
{{ site.data.cv.city }}, {{ site.data.cv.country }}

== Education
#chiline()

{% for edu in site.data.cv.education %}*#link("{{ edu.url }}")[{{ edu.institute }}]* #h(1fr) {{ edu.date }} \
{{ edu.degree | replace: "*", "\\*" }}\
{% if edu.title %} ("{{edu.title}}" - Supervisor: {{edu.supervisor}}){% endif %}

{% endfor %} 


== Work Experience
#chiline()

{% for emp in site.data.cv.employment %}
*{{ emp.institute }}* #h(1fr) {{ emp.date }}\
{{emp.jobtitle}}
{% endfor %}

== Achievements
#chiline()

- Obtained €{{ total_assigned }} in funding, including IRC Consolidator Laureate Award, Co-ordinator of H2020 Project, Collaborative projects with Fidelity Investments, Huawei and Genesys.
- {{ site.data.publications | size }} publications. ({{ site.data.cv.google_scholar.citations}} Citations; h-Index: {{ site.data.cv.google_scholar.h_index }}). #link("https://john.mccr.ae/publications")[Full Publication List].
- Supervised {{ site.data.cv.students | where: "completed", "true" | size }} PhD students to completion ({{ site.data.cv.students | where: "completed", "false" | size }} ongoing).
- Chair and Founder of #link("https://2023.ldk-conf.org")[Language, Data and Knowledge Conference] Series.
- Led departmental self-assessment team to Athena SWAN Bronze Award (for gender equality).
- NUI Galway President's Award for Research Excellence.
- Lectured courses on Natural Language Processing, Knowledge Graphs, Linked Data and Semantic Web and the University of Galway and Bielefeld University.
