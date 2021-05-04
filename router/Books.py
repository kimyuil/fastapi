from fastapi import APIRouter, Depends, HTTPException
from model.BooksData import booksData

routerBooks = APIRouter(
    prefix="/books",
    tags=["books"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@routerBooks.get("/")
async def read_items():
    return booksData


@routerBooks.get("/{item_id}")
async def read_item(item_id: int):
    item = next((item for item in booksData if item["pk"] == item_id), None)
    
    if item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# @router.put(
#     "/{item_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}},
# )
# async def update_item(item_id: str):
#     if item_id != "plumbus":
#         raise HTTPException(
#             status_code=403, detail="You can only update the item: plumbus"
#         )
#     return {"item_id": item_id, "name": "The great Plumbus"}