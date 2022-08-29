# My RSS Cache

Sometitmes the RSS feed caching is not implemented, customizing the RSS cache for my favorite RSS feed.

<img src="https://i.imgur.com/cz13UZ9.png" width="100%" height="auto">

<img src="https://i.imgur.com/513JoLL.png" width="100%" height="auto">

## How it works


### How the data is stored:

- The RSS data contents is stored in the single key and data type.
  - For each RSS data contents:
    - The `lic_nttu_rss` is  the key and its value is the RSS XML feed contents.
    - The `lic_nttu_rss_expired` is the key and its value is current timestamp for fetching the RSS contents.

### How the data is accessed:

- Here is the sample code to access the RSS feed and expired with Python Redis OM:

```python
from redis_om import get_redis_connection

# Get the RSS feed
rss_contents = redis_conn.get('lic_nttu_rss')

# Get the RSS expired value
expired = redis_conn.get('lic_nttu_rss_expired')
```

## How to run it locally?

### Prerequisites

- Python - 3.8+
- pip - 21.1.1+

### Local installation

- Cloning the repository with `git clone` command.
- Running the `pip install -r requirements.txt` command.
- Running the `flask run` to run the RSS Cache App in the development mode.

## Available source RSS feed urls

- [LIC NTTU](https://lic.nttu.edu.tw/search.getService.asp?serviceName=GIP.xdrss&mp=1&ctNodeId=755)
    - https://my-rss-cache.herokuapp.com/lic_nttu
- [LIB NTU](https://www.lib.ntu.edu.tw/rss/newsrss.xml)
    - https://my-rss-cache.herokuapp.com/lib_ntu
- Coming soon!

## Deployment

To make deploys work, you need to create free account on [Redis Cloud](https://redis.info/try-free-dev-to)

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/peter279k/my-rss-cache)

