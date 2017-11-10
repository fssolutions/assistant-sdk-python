#!/usr/bin/python
# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from googlesamples.assistant.grpc import devicetool


def test_print_model_with_no_trait(caplog):
    devicetool.pretty_print_model({
        'deviceModelId': 'model-id',
        'projectId': 'project-id',
        'deviceType': 'device-type'
    })
    assert 'model-id' in caplog.text()
    assert 'project-id' in caplog.text()
    assert 'device-type' in caplog.text()
