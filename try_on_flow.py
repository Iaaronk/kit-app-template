# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

"""High-level orchestration script for the try-on workflow."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path

import websockets


# Placeholder imports for application specific functionality
from typing import Any


def load_character_model(*args: Any, **kwargs: Any) -> None:
    """Load the base character into the stage."""
    pass


def attach_clothing(*args: Any, **kwargs: Any) -> None:
    """Attach a clothing item to the character."""
    pass


def play_animation(name: str) -> None:
    """Play an animation on the character."""
    pass


def start_remote_stream(config_path: str) -> None:
    """Start Kit's remote stream using the provided config."""
    try:
        import omni.kit.app as kit_app
    except ImportError:
        raise RuntimeError("Omniverse Kit modules are unavailable")

    app = kit_app.get_app()
    app.start_remote_stream(config_path)


async def handle_message(websocket: websockets.WebSocketServerProtocol) -> None:
    """Process incoming websocket messages."""

    async for raw in websocket:
        data = json.loads(raw)
        if data.get("type") == "apply_clothing":
            attach_clothing(data.get("item"))
            await websocket.send(json.dumps({"type": "clothing_applied"}))
        elif data.get("type") == "play_anim":
            anim_name = data.get("name", "")
            if anim_name:
                play_animation(anim_name)


async def main() -> None:
    """Entry point for try-on workflow."""
    load_character_model()
    config_path = str(Path(__file__).with_name("stream.config.json"))
    start_remote_stream(config_path)

    async with websockets.serve(handle_message, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
