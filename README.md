# CHEQ's Real Time Interception Middleware Demo

The following repository demonstrate a simple demo which utilize CHEQ's RTI solution <br> for Python WSGI application.

In order to run the demo you'll need to create a couple environment variables.

```code
    CHEQ_API_KEY
    CHEQ_TAG_HASH
```
Then run

````bash
$ export CHEQ_API_KEY=abcdddd-dddd3-492f-9417-66a1f22b4daa 
$ export CHEQ_TAG_HASH=000000000000 
````
For Flask run
````bash
$ python flask_wsgi_app.py
````

And visit  `localhost:8080`

**Notes:**
The configuration file can be found at `configuration/rti_configuration.py`

````python
import os
from urllib.parse import urlparse
from urllib.parse import parse_qs


def callback(app, environ, start_response):
    start_response('302 Found', [('Location', 'https://www.youtube.com/watch?v=LButXcZ57pc')])
    return ''


def get_ja3(request):
    parsed_url = urlparse(request.url)
    ja3 = parse_qs(parsed_url.query).get('ja3', None)
    if isinstance(ja3, list):
        return ja3[0]


def get_channel(request):
    parsed_url = urlparse(request.url)
    channel = parse_qs(parsed_url.query).get('ch', None)
    if isinstance(channel, list):
        return channel[0]


def get_resource_type(request):
    method = request.headers.environ['REQUEST_METHOD']
    if method == 'POST':
        return 'application/json'
    else:
        return 'text/html'


rout_to_event_type = {
    '/': 'page_load',
    '/subscribe': 'subscribe'
}


options = {
    'api_key': os.environ.get('CHEQ_API_KEY'),
    'tag_hash': os.environ.get('CHEQ_TAG_HASH'),
    'mode': 'blocking',
    'uri_exclusion': [],
    'api_endpoint': 'https://rti-us-east-1.cheqzone.com',
    'redirect_url': 'https://www.youtube.com/watch?v=LButXcZ57pc',
    'callback': callback,
    'route_to_event_type': rout_to_event_type,
    'invalid_block_redirect_codes': None,
    'invalid_captcha_codes': None,
    'trusted_ip_header': 'Client_IP',
    'get_ja3': '',
    'get_resource_type': get_resource_type,
    'timeout': 1000,
    'get_channel': get_channel

}

````