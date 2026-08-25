from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import LibraryException


async def library_exception_handler(request: Request, exc: LibraryException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message},
    )
