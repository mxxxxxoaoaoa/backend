from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
import database
import config as cfg
import base64

config = cfg.load_config(".env")
# db = database.Database(config.db.dbname, config.db.user, config.db.password)
# db.get_all_posts()
# res = db.get_post(29814)
# print(res['files'][0])
# r = base64.b64encode(res['files'][0]).decode("utf-8")
# print(r)
app = FastAPI()
router = APIRouter(
    prefix="/api"
)
origins = [
    "http://localhost:5173",
    "localhost:5173",
    "127.0.0.1:5173",
    "http://127.0.0.1:5173",
    "http://13.48.1.212/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
db = database.Database(config.db.dbname, config.db.user, config.db.password)


@router.get('/posts')
async def get_all_posts():
    print('zapros')
    return db.get_all_posts()

@router.get('/posts/{db_id}')
async def get_post(db_id):
    return db.get_post(db_id)

app.include_router(router)
