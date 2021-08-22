#!/usr/bin/env python

# Read in the terms.yml file to validate each entry. Required are:
# - name: "term name"
#   definition: Those who regularly use expertise in programming to advance research.
#   usage: This is an example
#   core: true

# Optional are
#  url: https://us-rse.org/what-is-an-rse/
#  related:
#    - term1
#    - term2

import pytest
import yaml
import os

here = os.path.dirname(os.path.abspath(__file__))


def test_terms(tmp_path):
    """test that terms are valid."""
    termsfile = os.path.join(os.path.dirname(here), "_data", "terms.yml")
    print("Testing loading of the terms.yml file")
    assert os.path.exists(termsfile)

    # Read in the terms
    with open(termsfile, "r") as stream:
        terms = yaml.safe_load(stream)

    # Keep track of terms we've seen
    seen = set()

    # Keep track of related to ensure we don't have any unknown terms
    related = set()

    # required fields, and cannot be empty
    requireds = ["name", "definition", "core", "usage"]
    for entry in terms:
        print("Testing %s" % entry)
        for required in requireds:
            print("Looking for %s" % required)
            assert required in entry

        # Usage cannot be empty
        assert entry["usage"] not in ["", None]

        # Core must be true or false
        assert entry["core"] in [True, False]

        # Cannot have double quote in definition
        assert '"' not in entry["definition"]

        # If related defined, must be list
        if "related" in entry:
            assert isinstance(entry["related"], list)
            [related.add(x) for x in entry["related"]]

        # Url must be defined
        if "url" in entry:
            assert entry["url"].strip() not in ["", None]
            assert isinstance(entry["url"], str)

        # don't start with uppercase
        assert entry["name"][0] == entry["name"][0].lower()

        # cannot have duplicates
        assert entry["name"] not in seen
        seen.add(entry["name"])

    # Make sure we've seen all related terms
    for related_term in related:
        assert related_term in seen
