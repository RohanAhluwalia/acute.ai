from fastapi import APIRouter

router = APIRouter()


@router.get("/example")
async def example_endpoint():
    return {"message": "This is an example endpoint"}


@router.get("/metriport")
async def get_metriport_data():
    # Your logic to fetch data from Metriport
    return {"message": "Metriport data"}


@router.get("/tidepool")
async def get_tidepool_data():
    # Your logic to fetch data from Tidepool
    return {"message": "Tidepool data"}
