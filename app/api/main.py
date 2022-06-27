from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from app.api.source import *


app = APIRouter()


@app.post("/api/v1/compile/")
async def get_by_name(request: Request) -> JSONResponse:
    ref: str = None
    if disk_manager is None:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "status_message": "ERROR: Yandex storage is not available",
            },
        )

    request_body = await request.json()
    filename = request_body.get("filename")
    context = request_body.get("context")
    disk_manager.download(filename)
    #TODO: MIME-Type check
    compile_template(filename, context)
    disk_manager.upload(filename, overwrite=True)
    disk_manager.publish(filename)
    ref = disk_manager.get_resource_meta(filename).public_url

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "status_mesage": "success",
            "ref": ref,
        },
    )
