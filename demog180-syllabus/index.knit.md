---
title: "Social Networks (Demography 180)"
editor: source
pagetitle: "Social Networks (Demog 180)"
bibliography: class_networks.bib
csl: chicago-syllabus.csl
#suppress-bibliography: True
output:
  html_document: 
    css: syllabus.css
    pandoc_args: [
                  #"-F", "pandoc-include",
                  #"--citeproc",
                  #"-F", "pandoc-crossref", 
                  #"-F", "pandoc-citeproc"
                  ]
  pdf_document: default
---



<!--
NOTES:
- the chicago-syllabus.csl is from Kieran Healy: https://github.com/kjhealy/pandoc-templates/blob/master/csl/chicago-syllabus.csl
- if changing this in the future, you may have to tweak the 'range' values in the part that loads the excel sheet

WISHLIST:
- be able to generate pdf version (right now, the table looks wonky - links don't render, NAs, etc)
-->


<!-- LINK REFERENCES -->



::: {.cell}

:::

::: {.cell}

:::



(Syllabus last updated: 2025-August-27)

## Quick links

**Class meetings**: Tuesdays and Thursdays, 12:30-2:00PM, 166 Social Science Building   
<BR>
**Web**: <https://www.dennisfeehan.org/teaching/demog180-fa2025>  
**Ed page**: <https://edstem.org/us/courses/81974/discussion>  
**Gradescope page**: <https://www.gradescope.com/courses/1084072>  
**Bcourses page**: <https://bcourses.berkeley.edu/courses/1547380>  
**Lecture slides**: <https://drive.google.com/drive/folders/1jgKjkAImWtAzIusbB9mLGhthLyISQHZ2?usp=drive_link>  
<BR>
**Final exam**: TBA   
<BR>

## Staff
   
**Professor Dennis Feehan**, feehan [at] berkeley.edu  
Office hours: (see Ed post)  

**TA: Xinghe Pan**  
**TA: Nick Nolte**  
  
## Overview

The science of social networks focuses on measuring, modeling, and understanding the different ways that people are connected to one another.  In this class, we will use a broad toolkit of theories and methods drawn from the social, natural, and mathematical sciences to learn what a social network is, to understand how to work with social network data, and to illustrate some of the ways that social networks can be useful in theory and in practice. We will see that network ideas are powerful enough to be used everywhere from CDC and UNAIDS, where network models help epidemiologists prevent the spread of HIV, to Silicon Valley, where data scientists use network ideas to build products that enable people all across the globe to connect with one another.


**Please re-check the syllabus frequently; it will be updated as the semester progresses**



::: {.cell}
::: {.cell-output-display}

```{=html}
<div id="nrfetivwpl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>#nrfetivwpl table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#nrfetivwpl thead, #nrfetivwpl tbody, #nrfetivwpl tfoot, #nrfetivwpl tr, #nrfetivwpl td, #nrfetivwpl th {
  border-style: none;
}

#nrfetivwpl p {
  margin: 0;
  padding: 0;
}

#nrfetivwpl .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#nrfetivwpl .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#nrfetivwpl .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#nrfetivwpl .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#nrfetivwpl .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#nrfetivwpl .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#nrfetivwpl .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#nrfetivwpl .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#nrfetivwpl .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#nrfetivwpl .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#nrfetivwpl .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#nrfetivwpl .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#nrfetivwpl .gt_spanner_row {
  border-bottom-style: hidden;
}

#nrfetivwpl .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#nrfetivwpl .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#nrfetivwpl .gt_from_md > :first-child {
  margin-top: 0;
}

#nrfetivwpl .gt_from_md > :last-child {
  margin-bottom: 0;
}

#nrfetivwpl .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#nrfetivwpl .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#nrfetivwpl .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#nrfetivwpl .gt_row_group_first td {
  border-top-width: 2px;
}

#nrfetivwpl .gt_row_group_first th {
  border-top-width: 2px;
}

#nrfetivwpl .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#nrfetivwpl .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#nrfetivwpl .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#nrfetivwpl .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#nrfetivwpl .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#nrfetivwpl .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#nrfetivwpl .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#nrfetivwpl .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#nrfetivwpl .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#nrfetivwpl .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#nrfetivwpl .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#nrfetivwpl .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#nrfetivwpl .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#nrfetivwpl .gt_left {
  text-align: left;
}

#nrfetivwpl .gt_center {
  text-align: center;
}

#nrfetivwpl .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#nrfetivwpl .gt_font_normal {
  font-weight: normal;
}

#nrfetivwpl .gt_font_bold {
  font-weight: bold;
}

#nrfetivwpl .gt_font_italic {
  font-style: italic;
}

#nrfetivwpl .gt_super {
  font-size: 65%;
}

#nrfetivwpl .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#nrfetivwpl .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#nrfetivwpl .gt_indent_1 {
  text-indent: 5px;
}

#nrfetivwpl .gt_indent_2 {
  text-indent: 10px;
}

#nrfetivwpl .gt_indent_3 {
  text-indent: 15px;
}

#nrfetivwpl .gt_indent_4 {
  text-indent: 20px;
}

#nrfetivwpl .gt_indent_5 {
  text-indent: 25px;
}

#nrfetivwpl .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#nrfetivwpl div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>
<table class="gt_table" style="table-layout:fixed;" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
  <colgroup>
    <col style="width:10%;"/>
    <col style="width:5%;"/>
    <col style="width:5%;"/>
    <col style="width:40%;"/>
    <col style="width:20px;"/>
    <col style="width:10px;"/>
    <col style="width:10px;"/>
  </colgroup>
  <thead>
    <tr class="gt_col_headings">
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Theme">Theme</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Week">Week</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Date">Date</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Topic">Topic</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Demo">Demo</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Lab">Lab</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="Hwk">Hwk</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W0ludHJvICsgUGVyc29uYWwgTmV0d29ya3NdKCNzZWM6aW50cm8p"><span class='gt_from_md'><a href="#sec:intro">Intro + Personal Networks</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MQ=="><span class='gt_from_md'>1</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Aug 28</td>
<td headers="Topic" class="gt_row gt_left">Intro / what social networks are / basic graph theory / class info</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Mg=="><span class='gt_from_md'>2</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Sep 2</td>
<td headers="Topic" class="gt_row gt_left">Personal networks; social connectedness and social isolation in America</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W05ldHdvcmsgc3RydWN0dXJlOiBmb3VuZGF0aW9uc10oI3NlYzpzdHJ1Y3R1cmUp"><span class='gt_from_md'><a href="#sec:structure">Network structure: foundations</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Mg=="><span class='gt_from_md'>2</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Sep 4</td>
<td headers="Topic" class="gt_row gt_left">Triadic closure</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Mw=="><span class='gt_from_md'>3</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Sep 9</td>
<td headers="Topic" class="gt_row gt_left">Strength of Weak Ties, Social Capital, Structural Holes</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Mw=="><span class='gt_from_md'>3</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Sep 11</td>
<td headers="Topic" class="gt_row gt_left">Network centrality / the Friendship Paradox</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="NA=="><span class='gt_from_md'>4</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Sep 16</td>
<td headers="Topic" class="gt_row gt_left">Networks in context; homophily; affiliation networks; and foci</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="NA=="><span class='gt_from_md'>4</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Sep 18</td>
<td headers="Topic" class="gt_row gt_left">Positive and negative networks</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="NQ=="><span class='gt_from_md'>5</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Sep 23</td>
<td headers="Topic" class="gt_row gt_left">Intro to mathematical network models; the Erdos-Renyi model and its predictions</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W1NtYWxsIHdvcmxkc10oI3NlYzpzbWFsbHdvcmxkcyk="><span class='gt_from_md'><a href="#sec:smallworlds">Small worlds</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="NQ=="><span class='gt_from_md'>5</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Sep 25</td>
<td headers="Topic" class="gt_row gt_left">Small worlds</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Ng=="><span class='gt_from_md'>6</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Sep 30</td>
<td headers="Topic" class="gt_row gt_left">Search in small worlds</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Ng=="><span class='gt_from_md'>6</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Oct 2</td>
<td headers="Topic" class="gt_row gt_left">Scale-free networks</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W05ldHdvcmsgc3RydWN0dXJlOiBhZHZhbmNlZF0oI3NlYzphZHZhbmNlZHN0cnVjdHVyZSk="><span class='gt_from_md'><a href="#sec:advancedstructure">Network structure: advanced</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Nw=="><span class='gt_from_md'>7</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Oct 7</td>
<td headers="Topic" class="gt_row gt_left">More models: configuration model and stochastic block model</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="Nw=="><span class='gt_from_md'>7</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Oct 9</td>
<td headers="Topic" class="gt_row gt_left">Community detection</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="OA=="><span class='gt_from_md'>8</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Oct 14</td>
<td headers="Topic" class="gt_row gt_left">Midterm review</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="OA=="><span class='gt_from_md'>8</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Oct 16</td>
<td headers="Topic" class="gt_row gt_left">Midterm</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="OQ=="><span class='gt_from_md'>9</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Oct 21</td>
<td headers="Topic" class="gt_row gt_left">Empirical studies of network structure</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W0R5bmFtaWNzOiBTaW1wbGUgY29udGFnaW9uXSgjc2VjOnNpbXBsZWNvbnRhZ2lvbik="><span class='gt_from_md'><a href="#sec:simplecontagion">Dynamics: Simple contagion</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="OQ=="><span class='gt_from_md'>9</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Oct 23</td>
<td headers="Topic" class="gt_row gt_left">Diseases and simple contagion in general; SIR model</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTA="><span class='gt_from_md'>10</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Oct 28</td>
<td headers="Topic" class="gt_row gt_left">SIR model on networks; centrality, influence and network disease models</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W0NvbmN1cnJlbmN5XSgjc2VjOmNvbmN1cnJlbmN5KQ=="><span class='gt_from_md'><a href="#sec:concurrency">Concurrency</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTA="><span class='gt_from_md'>10</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Oct 30</td>
<td headers="Topic" class="gt_row gt_left">Sexual networks, concurrency, and HIV</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTE="><span class='gt_from_md'>11</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Nov 4</td>
<td headers="Topic" class="gt_row gt_left">Empirical studies of simple contagion</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W1NvY2lhbCBpbmZsdWVuY2VdKCNzZWM6c29jaWFsaW5mbHVlbmNlKQ=="><span class='gt_from_md'><a href="#sec:socialinfluence">Social influence</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTE="><span class='gt_from_md'>11</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Nov 6</td>
<td headers="Topic" class="gt_row gt_left">Social influence, herding, and cascades</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTI="><span class='gt_from_md'>12</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Nov 11</td>
<td headers="Topic" class="gt_row gt_left">Threshold models and complex contagion</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><span data-qmd-base64="W0R5bmFtaWNzOiBDb21wbGV4IGNvbnRhZ2lvbiBhbmQgc29jaWFsIGluZmx1ZW5jZV0oI3NlYzpjb21wbGV4Y29udGFnaW9uKQ=="><span class='gt_from_md'><a href="#sec:complexcontagion">Dynamics: Complex contagion and social influence</a></span></span></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTI="><span class='gt_from_md'>12</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Nov 13</td>
<td headers="Topic" class="gt_row gt_left">Complex contagion on networks</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTM="><span class='gt_from_md'>13</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Nov 18</td>
<td headers="Topic" class="gt_row gt_left">Guest lecture - Chris Soria</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTM="><span class='gt_from_md'>13</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Nov 20</td>
<td headers="Topic" class="gt_row gt_left">Complex contagion on networks, cont. + Empirical studies of complex contagion</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTQ="><span class='gt_from_md'>14</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Nov 25</td>
<td headers="Topic" class="gt_row gt_left">NO CLASS</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTQ="><span class='gt_from_md'>14</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Nov 27</td>
<td headers="Topic" class="gt_row gt_left">THANKSGIVING (NO CLASS)</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTU="><span class='gt_from_md'>15</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Dec 2</td>
<td headers="Topic" class="gt_row gt_left">Cooperation and networks</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTU="><span class='gt_from_md'>15</span></span></td>
<td headers="Date" class="gt_row gt_left">Thu, Dec 4</td>
<td headers="Topic" class="gt_row gt_left">Empirical studies of complex contagion/cooperation + Wrap up</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
    <tr><td headers="Theme" class="gt_row gt_left"><br /></td>
<td headers="Week" class="gt_row gt_right"><span data-qmd-base64="MTY="><span class='gt_from_md'>16</span></span></td>
<td headers="Date" class="gt_row gt_left">Tue, Dec 9</td>
<td headers="Topic" class="gt_row gt_left">READING WEEK</td>
<td headers="Demo" class="gt_row gt_left"><br /></td>
<td headers="Lab" class="gt_row gt_left"><br /></td>
<td headers="Hwk" class="gt_row gt_left"><br /></td></tr>
  </tbody>
  
  
</table>
</div>
```

:::
:::



## Requirements

### Lectures

Lectures will introduce and develop key theoretical and technical concepts in the study of social networks.  To illustrate these ideas, some of the lectures will have a live lab component, where  we will interactively discuss and work through an analysis in a Jupyter notebook. These live labs will help us explore and develop intuition about key concepts in the course.

The lectures are organized so that the first set of material, up to the mid-term exam, is a survey of the core theories, concepts, and methods needed to be familiar with social networks.  After the mid-term, the lectures will turn to an exploration of how these core ideas have been used, modified, and deepened in several different topic areas.

*You are responsible for all of the material covered in lectures, as well as any announcements made there.*

### Required readings

The course readings will include selections from the textbook 
[Networks, Crowds, and Markets](https://www.cs.cornell.edu/home/kleinber/networks-book/) by Easley and Kleinberg: 

* @easley_networks_2010

We will also read chapters from popular science books written by leading network researchers, including selections from

* @watts_six_2003
* @epstein_invisible_2008

Finally, we will read several journal and newspaper articles.

The readings serve two purposes: (1) they provide an introduction and reference for key concepts that we will need to study social networks; (2) they illustrate how social network ideas get used in real world research and applications across many different disciplines. You are expected to do the reading before each class. Whenever possible,  PDFs of the readings will be posted on the bCourses site.


### Homeworks and labs

There will be a total of 6 to 8 homeworks, a similar number of labs, and one mini-project.  These assignments are a critical part of the learning you will do in this class: they give you an opportunity to explore the topics we cover in the readings and in lecture on your own. They also give you a chance to practice your writing and your data analysis and programming skills.  Most homeworks and labs will ask you to provide some written arguments and to solve some problems by writing Python code in a Jupyter notebook.  

Labs are graded based on effort; therefore, you can get full credit on a lab even if you do not get all of the answers right. Labs must be handed in on time for full credit. 

Homeworks and are graded on correctness and must be handed in on time for full credit. However, we will drop the homework with the lowest score; thus, you can miss handing in one homework over the course of the semester without it affecting your grade. (Note that you cannot drop the grade for the mini-project.)

The mini-project is like an extended homework that comes after all of the notebook-based homeworks. The goal is to give you a chance to start from scratch with a new network dataset and to demonstrate that you can perform an analysis on the network with minimal hand-holding. It will count as two homeworks.

**Collaboration**: It can be helpful and educational to discuss the assignments with other students in the class, but (1) all of the work should be your own (i.e., you are not allowed to just copy code, answers, or arguments); (2) you should make a note of the names of the other students you worked with when handing your assignments in. Please treat AI tools like ChatGPT like another student: follow rules (1) and (2); that is, don't copy code or text directly from an AI tool and please make a note of any tool you consulted at the top of your assignment.


### Exams

There will be two in-class closed book examinations. The mid-term examination will be held during normal class time in our normal classroom; the timing of this midterm will be designed to assess your mastery of the core concepts in social networks. The final will be held during the final exam period (see the date/time above). The final exam will be cumulative.

### Participation and quizzes

In some lectures, you will be asked to participate in discussions and interactive demonstrations. There will also be a small number (about 2) quizzes on bCourses over the semester. These quizzes will consist of a few multiple choice questions; the goal of these quizzes will be to ensure that you are staying up to date with the reading and lecture materials covered in the class (including guest lectures). 

<!--### Sections                                                                                                                                                                                                                       -->

<!--There will be optional weekly sections. The goal of these sections will be (1) to give you a chance to discuss the material and (2) to give you a chance to practice problems similar to the problems that will be on the homework.-->


### Summary

|  Component | % of grade |
|  ------ | ------ |
|  Homeworks (you can drop your lowest score) | 35 |
|  Labs  | 15 |
|  Mid-term exam | 15 |
|  Final exam | 30 |
|  Participation + Quizzes | 5 |

## Detailed modules

<div class="singlespace">

### Introduction to social networks and Personal networks {#sec:intro}
	
Reading: 

* @watts_six_2003 preface-Ch.1
* @easley_networks_2010 Ch.1-Ch.2
* [optional] Fischer, [*Still connected*](https://muse.jhu.edu/book/15006), esp. Ch. 2 and 7 


### Network structure: foundations {#sec:structure}

Reading:

* @easley_networks_2010 Ch. 3.1-3.3 (Triadic closure + tie strength)
* @easley_networks_2010 Ch. 3.5 (Social capital)
* @easley_networks_2010 Ch.5.1-5.2 (Positive and negative relationships)
* [Friends you can count on](https://opinionator.blogs.nytimes.com/2012/09/17/friends-you-can-count-on/)
* [Why your friends have more friends than you do](https://www.journals.uchicago.edu/doi/abs/10.1086/229693)
* @watts_six_2003 Ch. 2 (Random networks)
* TBD - possibly some empirical examples


### Small worlds and beyond {#sec:smallworlds}

Readings:

* @easley_networks_2010 Ch.4.3-4.4 (Affiliation networks)
* @watts_six_2003 Ch. 3 (Small worlds)
* @watts_six_2003 Ch. 4 (Beyond small worlds; scale-free networks)
* @easley_networks_2010 Ch. 20.1-20.2 (Small worlds)
* @watts_six_2003 Ch. 5 (Search in networks)
* @easley_networks_2010 Ch. 20.3-20.5 (Search in small worlds)
* @easley_networks_2010 Ch. 18.1-18.5 (Scale-free networks)

### Network structure: advanced {#sec:advancedstructure}

Reading:

TBD

### Simple contagion {#sec:simplecontagion}

Reading:

* @watts_six_2003 Ch.6
* @easley_networks_2010 Ch. 21.1-21.3 (The SIR epidemic model)

### Concurrency in sexual networks {#sec:concurrency}

* Sexual networks, concurrency, and HIV
* @epstein_invisible_2008 Ch.2-4
* OPTIONAL: @easley_networks_2010 Ch. 21.6
* NOTE: if you are interested in reading more of the debate over concurrency, [this issue](https://link.springer.com/journal/10461/14/1/page/1) of the journal that Lurie and Rosenthal published in has papers on both sides. (These additional papers are not required reading.)

<!--

### Cooperation {#sec:cooperation}

Reading:

* @easley_networks_2010 Ch. 6.1-6.2 
* @axelrod_evolution_1984 Ch. 1 (on bCourses)

-->


### Social influence {#sec:socialinfluence}

Reading:

* @easley_networks_2010 Ch. 16.1-16.2; parts of 16.3-16.6; 16.7
* @watts_six_2003 Ch. 7 

### Complex contagion {#sec:complexcontagion}

Reading:

* @watts_six_2003 Ch. 8
* @easley_networks_2010 Ch. 19.1-19.6
* [Study says obesity can be contagious](https://www.nytimes.com/2007/07/25/health/25cnd-fat.html)



<!--
### Week 15: Guest lectures {#sec:guests}

Reading:

* TBA

-->

## Other class policies  
  
**Religious Accommodations**  
  
Requests to accommodate a student's religious creed by scheduling tests or
examinations at alternative times should be submitted directly to the
instructor. Reasonable common sense, judgment and the pursuit of mutual
goodwill should result in the positive resolution of scheduling conflicts. The
regular campus appeals process applies if a mutually satisfactory arrangement
cannot be achieved.

**Statement on Academic Freedom**  
  
Both students and instructors have rights to academic freedom. Please respect
the rights of others to express their points of view in the classroom.
  
**DSP Accommodations**  
  
The purpose of academic accommodations is to ensure that all students have a fair chance at academic success. Disability, or hardships such as basic needs insecurity, uncertain documentation and immigration status, medical and mental health concerns, pregnancy and parenting, significant familial distress, and experiencing sexual violence or harassment, can affect a student’s ability to satisfy particular course requirements. Students have the right to reasonable academic accommodations, without having to disclose personal information to instructors. For more information about accommodations, scheduling conflicts related to religious creed or extracurricular activities, please see the [Academic Accommodations hub website](https://evcp.berkeley.edu/programs-resources/academic-accommodations-hub#accommodations).
  
**Student Resources**  
  
The Student Learning Center provides a wide range of resources to promote learning and academic success for students. For information regarding these services, please consult the Student Learning Center Website:
https://slc.berkeley.edu/

**Classroom Climate**  
  
We are all responsible for creating a learning environment that is welcoming, inclusive, equitable, and respectful. If you feel that these expectations are not being met, you can consult your instructor(s) or seek assistance from campus resources (see the [Academic Accommodations website](https://evcp.berkeley.edu/programs-resources/academic-accommodations-hub#accommodations)).
  
**Academic Integrity**  
  
The high academic standard at the University of California, Berkeley, is reflected in each degree that is awarded. As a result, every student is expected to maintain this high standard by ensuring that all academic work reflects unique ideas or properly attributes the ideas to the original sources.

These are some basic expectations of students with regards to academic integrity:

* Any work submitted should be your own individual thoughts, and should not have been submitted for credit in another course unless you have prior written permission to re-use it in this course from this instructor.
* All assignments must use "proper attribution," meaning that you have identified the original source and extent or words or ideas that you reproduce or use in your assignment. This includes drafts and homework assignments!
* In general, you should not turn in work that was done by an AI tool, such as an LLM (like ChatGPT). If you have any questions, please ask an instructor.
* If you are unclear about expectations, ask your instructor or GSI.
* Do not collaborate or work with other students on assignments or projects unless you have been given permission or instruction to do so.

