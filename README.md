# My RSS Cache

Sometitmes the RSS feed caching is not implemented, customizing the RSS cache for my favorite RSS feed.

[My RSS Cache Version](https://i.imgur.com/cz13UZ9.png)
[My RSS Cache for lic_nttu](https://i.imgur.com/513JoLL.png)

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

## Deployment

To make deploys work, you need to create free account on [Redis Cloud](https://redis.info/try-free-dev-to)

### Heroku

[Insert Deploy on Heroku button](https://heroku.com/deploy?template=https://github.com/peter279k/my-rss-cache)

