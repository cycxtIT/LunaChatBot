HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "5045995046:AAGZOP46w96nXh5ORg9vIL8bekHLe3_zjEI"
    ARQ_API_KEY = "XNGIAT-CFTXQS-MEDCWV-SWVHYC-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "zh-cn"

# Leave it as it is
ARQ_API_BASE_URL = "https://thearq.tech"
