from fastapi import FastAPI, HTTPException, Depends, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models import Item, SessionLocal, init_db

# Initialize DB and app
init_db()
app = FastAPI()

# Enable CORS (so frontend can connect to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE - Add a new item
@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

# READ - Get all items
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# READ - Get one item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE - Update an item by ID
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str = Body(...),
    description: str = Body(...),
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = name
    item.description = description
    db.commit()
    db.refresh(item)
    return item

# DELETE - Delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Deleted successfully"}

# ✅ HOME ROUTE — accessible via browser (HTML) or curl (JSON)
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    user_agent = request.headers.get("user-agent", "").lower()
    if "curl" in user_agent or "httpie" in user_agent:
        return {"message": "Welcome to My API Server"}
    return HTMLResponse("""
        <h2>🚀 Welcome to My API Server</h2>
        <p>Use <code>/items/</code> to GET or POST items.</p>
        <p>Try <code>curl http://127.0.0.1:8000/items/</code> in terminal.</p>
    """)
