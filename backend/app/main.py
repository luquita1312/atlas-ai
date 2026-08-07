from fastapi import FastAPI


app = FastAPI(
    title="Atlas AI",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "project": "Atlas AI",
        "version": "0.1.0",
        "status": "running"
    }
