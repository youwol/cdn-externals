from pathlib import Path
from typing import Any

from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol_utils.context import Context

import importlib.util

path_common = Path(__file__).parent.parent.parent /'yw_pipeline.py'
spec = importlib.util.spec_from_file_location("module.name", path_common)
common: Any = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, ctx: Context):
        return await common.pipeline_typescript(ctx)
