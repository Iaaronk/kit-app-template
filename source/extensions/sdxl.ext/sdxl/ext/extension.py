# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import omni.ext
import omni.ui as ui


# Functions and vars are available to other extensions as usual in python: `sdxl.ext.some_public_function(x)`
def some_public_function(x: int):
    print(f"[sdxl.ext] some_public_function was called with {x}")
    return x ** x


# Any class derived from `omni.ext.IExt` in the top level module (defined in `python.modules` of `extension.toml`) will
# be instantiated when the extension gets enabled, and `on_startup(ext_id)` will be called.
# Later when the extension gets disabled on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is the current extension id. It can be used with the extension manager to query additional information,
    # like where this extension is located on the filesystem.
    def on_startup(self, ext_id):
        print("[sdxl.ext] Extension startup")

        self._window = ui.Window("SDXL Extension", width=300, height=300)
        self.sampler_val = "K_DPM_2_ANCESTRAL"
        def dpm_clicked():
        	self.sampler_val = "K_DPM_2_ANCESTRAL"
        def ddim_clicked():
            self.sampler_val = "DDIM"
        def lms_clicked():
            self.sampler_val = "K_LMS"
        def eulera_clicked():
            self.sampler_val = "K_EULER_ANCESTRAL"
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("Enter Prompt:")
                self.prompt_model = ui.SimpleStringModel()
                self.prompt_field = ui.StringField(model = self.prompt_model)
                neg_label = ui.Label("Enter Negative Prompt:")
                self.neg_prompt_model = ui.SimpleStringModel()
                self.neg_prompt_field = ui.StringField(model=self.neg_prompt_model)
                with ui.HStack():
                    collection = ui.RadioCollection()
                    dpm_button = ui.RadioButton(radio_collection=collection, text="DPM", clicked_fn=dpm_clicked)
                    ddim_button = ui.RadioButton(radio_collection=collection, text="DDIM", clicked_fn=ddim_clicked)
                    lms_button = ui.RadioButton(radio_collection=collection, text="LMS", clicked_fn=lms_clicked)
                    eulera_button = ui.RadioButton(radio_collection=collection, text="Euler A", clicked_fn=eulera_clicked)


                self.test_label = ui.Label("Test")

                def on_click():
                    self.test_label.text = self.neg_prompt_model.as_string

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click)

    def on_shutdown(self):
        print("[sdxl.ext] Extension shutdown"
