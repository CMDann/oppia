# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from extensions.interactions import base


class MusicNotesInput(base.BaseInteraction):
    """Interaction for music notes input."""

    name = 'Music Notes Input'
    description = (
        'Allows learners to drag and drop notes onto the lines of a music '
        'staff.')
    display_mode = base.DISPLAY_MODE_SUPPLEMENTAL
    _dependency_ids = ['midijs']
    answer_type = 'MusicPhrase'

    _customization_arg_specs = [{
        'name': 'sequenceToGuess',
        'description': 'Correct sequence of notes',
        'schema': {
            'type': 'custom',
            'obj_type': 'MusicPhrase',
        },
        'default_value': [],
    }, {
        'name': 'initialSequence',
        'description': 'Starting notes on the staff',
        'schema': {
            'type': 'custom',
            'obj_type': 'MusicPhrase',
        },
        'default_value': [],
    }]
