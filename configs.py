from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25377875"))
    API_HASH = getenv("API_HASH", "cf80e342be48570ca2e4c9d2c7695413")
    BOT_TOKEN = getenv("BOT_TOKEN", "6435555746:AAH38KE9X7FthT4bD7hcdGRNxUVgV5mKx5g")
    CHID = int(getenv("CHID", "-1001948610504"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://nehal969797:nehalsingh969797@cluster0.4xsgmgm.mongodb.net/?retryWrites=true&w=majority")
    LOGCHID = int(getenv("LOGCHID", "-1001748572062"))
    API = getenv("API", "abcdefu67-8dgdg")
cfg = Config()
