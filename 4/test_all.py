import json
import re

from validator_collection import checkers 

from mytool import extract, extract_single


def test_extract_single():
    extracted = extract_single("http://google.com")
    # Image path probably pretty stable; ideally we extract from a page 
    # that never changes like a self-hosted testing page set up for this
    # purpose.
    assert re.findall("http://google.com/images.*.png", extracted["images"][0])

    for link in extracted["links"]:
        assert checkers.is_url(link)


def test_extract():
    extracted = extract(["http://google.com", "https://example.com"])
    assert json.loads(extracted)
