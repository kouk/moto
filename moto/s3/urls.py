from __future__ import unicode_literals
from .responses import S3ResponseInstance

url_bases = [
    "https?://(?P<bucket_name>[a-zA-Z0-9\-_.]*)\.?s3(.*).amazonaws.com",
    "https?://(?P<bucket_name>[a-zA-Z0-9\-_.]*)\.?s3.mockaws.com",
    "https?://(?P<bucket_name>[a-zA-Z0-9\-_.]*)\.?s3.mockaws.com:9876",
]

url_paths = {
    '{0}/$': S3ResponseInstance.bucket_response,
    '{0}/(?P<key_name>.+)': S3ResponseInstance.key_response,
}
