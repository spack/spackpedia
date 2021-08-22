---
layout: page
title: Term Definition
permalink: /term/
form: true
---

<!-- Page Content -->
<div class="container">
  <div class="row">
      <h5></h5>
      <div id="term-definition"></div>
      <br>
      <blockquote id="term-usage" hidden></blockquote>
      <div id="term-related" hidden>
      <h2>Related terms</h2>
      <ul id="related-terms"></ul>
      </div>
      <br>
      <img id="spack-image" src="" style="padding-top:10px;padding-bottom:10px;max-height:400px" hidden>
      <br>
      <a href="{{ site.baseurl }}/"><button class="btn btn-info" style="margin-top:20px">Back</button></a>
      <a style="float:right" id="term-link" href="#" target="_blank" hidden><button class="btn btn-info" style="margin-top:20px">Learn More</button></a>
  </div>
</div>
<script>

// populate page with all terms and definitions
terms = { {% for term in site.data.terms %}"{{ term.name }}": {"definition": "{{ term.definition }}", "core": {{ term.core }}, {% if term.url %}"url": "{{ term.url }}",{% endif %} {% if term.related %}"related": [{% for related in term.related %}"{{ related }}"{% if loop.last %}{% else %},{% endif %}{% endfor %}] ,{% endif %} {% if term.image %}"image": "{{ term.image }}",{% endif %} "usage": "{{ term.usage }}"} {% if forloop.last %}{% else %},{% endif %}{% endfor %}}
console.log(terms)
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

var term = getUrlVars()["q"];
term = decodeURI(term);

if (term in terms) {
  console.log(term)

  // These attributes are not optional (and will be defined)
  document.getElementById('page-title').innerHTML = term;
  document.getElementById('term-definition').innerHTML = terms[term]["definition"];
  document.getElementById('term-usage').innerHTML = '"' + terms[term]["usage"] + '"';
  document.getElementById('term-usage').hidden = false;

  var core = terms[term]["core"]

  // These are optional, and page content is hidden if they aren't defined
  if ("url" in terms[term]) {
    var url = terms[term]["url"]
    if (url != "") {
      document.getElementById('term-link').href = terms[term]["url"]
      document.getElementById('term-link').hidden = false
    }
  }
  if ("image" in terms[term]) {
    var image = terms[term]["image"]
    if (image != "") {
      document.getElementById('spack-image').src = "{{ site.baseurl }}/assets/img/terms/" + terms[term]["image"]
      document.getElementById('spack-image').hidden = false
    }
  }

  if ("related" in terms[term]) {
    var related_terms = terms[term]["related"]
    related = "";
    for (i=0; i<related_terms.length; i++){
        related += '<a href="{{ site.baseurl }}/term/?q=' + related_terms[i] + '"><li>' + related_terms[i] + '</li></a>';
    }
    document.getElementById('related-terms').innerHTML = related
    document.getElementById('related-terms').hidden = false
    document.getElementById('term-related').hidden = false
  }

  if (core == "true") {
      document.getElementById('spack-core').hidden = false
  }
} else {
  document.getElementById('term-definition').innerHTML = "We couldn't find the term " + term + " in our lookup. Perhaps you can <a href='{{ site.repo }}' target='_blank'>contribute</a> it?";
}
</script>
