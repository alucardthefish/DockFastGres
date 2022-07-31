import uvicorn

from db import db
from backend import create_app
from backend.api.routes.users import user_api as user_api
from backend.api.routes.items import item_api as item_api


app = create_app()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(user_api.user_router)
app.include_router(item_api.item_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
