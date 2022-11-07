from fastapi import APIRouter
from fastapi import Response, status
from starlette.responses import JSONResponse

router = APIRouter()


@router.get('/', response_class=JSONResponse, status_code=200)
async def healthcheck(response: Response):
    try:
        ...
    except Exception as error:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"success": False}
    else:
        return {"success": True}
