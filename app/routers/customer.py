from fastapi import APIRouter

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.get("/")
async def list_customers():
    return {"customers": ["Alice", "Bob", "Charlie"]}
