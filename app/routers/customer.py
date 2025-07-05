from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
async def get_customers():
    return {"message": "Customers endpoint"}
