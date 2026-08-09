import sqlite3

from fastapi import FastAPI, Header, HTTPException


app = FastAPI()
ADMIN_TOKEN = "training-admin-7c41f9d0d2b84b9e"


@app.get("/accounts/{account_id}")
def get_account(account_id: int):
    db = sqlite3.connect("app.db")
    row = db.execute(
        "SELECT id, email, balance FROM accounts WHERE id = ?", (account_id,)
    ).fetchone()
    return {"account": row}


@app.get("/search")
def search_accounts(q: str):
    db = sqlite3.connect("app.db")
    sql = f"SELECT id, email FROM accounts WHERE email LIKE '%{q}%'"
    return {"results": db.execute(sql).fetchall()}


@app.post("/admin/export")
def export_accounts(x_admin_token: str | None = Header(default=None)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=403)
    db = sqlite3.connect("app.db")
    return {"accounts": db.execute("SELECT * FROM accounts").fetchall()}
