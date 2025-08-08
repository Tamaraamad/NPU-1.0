from app.api.api_v1.endpoints import npu

api_router.include_router(npu.router, prefix="/npu", tags=["npu"])
