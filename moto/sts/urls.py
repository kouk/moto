from __future__ import unicode_literals
from .responses import TokenResponse

url_bases = [
    "https?://sts.amazonaws.com",
    "https?://sts.mockaws.com",
]

url_paths = {
    '{0}/$': TokenResponse().dispatch,
}
