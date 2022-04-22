from pathlib import Path

from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import JsBundle
from youwol_utils.context import Context

import importlib.util

path_common = Path(__file__).parent.parent.parent.parent /'yw_pipeline.py'
spec = importlib.util.spec_from_file_location(
    "module.name",
    path_common
)
common_pipeline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common_pipeline)


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, _ctx: Context):

        config = common_pipeline.PipelineConfig(
            target=JsBundle()
        )
        return common_pipeline.pipeline(config)
