from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.v1 import router as api_router
from app.services.logger import logger

app = FastAPI(
    title="Async FastAPI Processor",
    version="1.0.0"
)

# Middleware логирования
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        logger.info(f"➡️ Request: {request.method} {request.url} | Body: {body.decode('utf-8')}")
        
        try:
            response: Response = await call_next(request)
        except Exception as e:
            logger.exception(f"❌ Exception: {str(e)}")
            return JSONResponse(status_code=500, content={"error": "Internal Server Error"})
        
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        logger.info(f"⬅️ Response: {request.method} {request.url} | Status: {response.status_code} | Body: {response_body.decode('utf-8')}")

        return Response(content=response_body, status_code=response.status_code, headers=dict(response.headers), media_type=response.media_type)

app.add_middleware(LoggingMiddleware)

# Глобальный обработчик ошибок
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

# Подключение маршрутов с префиксом
app.include_router(api_router, prefix="/process_data")
