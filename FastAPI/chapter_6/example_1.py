from fastapi import FastAPI, Depends

app = FastAPI()


def user_dep(name: str, password: str):
    return {"name": name, "valid": True}


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


def check_dep(name: str, password: str):
    if not name:
        raise


@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True
