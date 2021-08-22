---
layout: default
permalink: /
---

<div class="larg">{% assign terms = site.data.terms | sort: 'name' %}
  <dl>{% for term in terms %}<dt data-url="{{ term.url }}" data-dfn="{{ term.definition | truncate: 150 }}">{% if term.core %}<span title="This is a core spack term">⭐️{% else %}<span title="This is a fun spack term.">😆{% endif %}</span> {{ term.name }}</dt>{% endfor %}
  </dl>
</div>
<div class="flap">
</div>
