from pathlib import Path
from typing import Any

from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import (  # noqa: E402
    Alconna,
    AlconnaMatcher,
    UniMessage,
    on_alconna,
)

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="matcha-218",
    description="",
    usage="",
    type="application",
    homepage="",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "version": __version__,
        "authors": [
            "hanasaki <hanasakayui2022@gmail.com>",
        ],
    },
)

_test: Alconna[Any] = Alconna("test")
test: type[AlconnaMatcher] = on_alconna(_test, use_cmd_start=True)

@test.handle()
async def _() -> None:
    await test.finish(UniMessage.image(path=Path(__file__).parent / "arona.svg"))

