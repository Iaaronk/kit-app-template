from __future__ import annotations

import carb
import omni.usd
import omni.timeline
from pxr import Usd


def play_animation(anim_name: str, loop: bool = True) -> None:
    """Play the animation clip using the Omniverse timeline.

    Parameters
    ----------
    anim_name : str
        Name of the animation clip prim under ``/Root/Animations``.
    loop : bool, optional
        Whether the timeline should loop playback, by default ``True``.
    """
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        carb.log_warn("No stage available for playback")
        return

    clip_path = f"/Root/Animations/{anim_name}"
    clip_prim = stage.GetPrimAtPath(clip_path)
    if not clip_prim or not clip_prim.IsValid():
        carb.log_warn(f"Animation prim not found: {clip_path}")
        return

    start_attr = clip_prim.GetAttribute("startTimeCode")
    end_attr = clip_prim.GetAttribute("endTimeCode")
    if not start_attr or not end_attr:
        carb.log_warn(f"Animation {anim_name} missing timecode attributes")
        return

    start = start_attr.Get()
    end = end_attr.Get()

    timeline = omni.timeline.get_timeline_interface()
    timeline.set_looping(loop)
    timeline.set_playback_range(start, end)
    timeline.set_current_time(start)
    timeline.play()

    if not loop:

        def _on_tick(event):
            if event.type == int(omni.timeline.TimelineEventType.TICK):
                if timeline.get_current_time() >= end:
                    timeline.pause()
                    timeline.remove_callback(_sub)

        _sub = timeline.get_timeline_event_stream().create_subscription_to_pop(_on_tick)
