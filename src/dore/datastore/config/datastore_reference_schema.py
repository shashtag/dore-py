# Copyright 2022 Bhargav KN
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Datastore Reference schema
"""

datastore_reference_schema = {
    'title': 'Datastore Reference',
    'description': '<h4> Datastore Reference </h4>'
                   '<p>'
                   ' A datastore can be defined in a file separate from the manifest file.'
                   '</p>'
                   '<p>'
                   ' You would generally want to define each datastore in a separate file. It is recommended to'
                   ' spread different parts of the manifest such as models and datastores across '
                   ' different files in order to keep each config small and readable.'
                   '</p>'
                   ' Use this schema when the datastore is defined in a separate file and you need to provide a '
                   ' reference to that file in the manifest.'
                   '</p>'
                   ' <p>'
                   ' Use the `ref` field in the manifest and provide absolute path to the file that actually'
                   ' contains the <a href="#tab-pane_datastores_pattern1_oneOf_i0"> datastore definition </a>.'
                   '</p>'
                   ' In the example, the definition for `datastore_1` is present in a separate file and the'
                   ' `ref`erence to that file is added in the manifest.'
                   '</p>',
    'type': 'object',
    'properties': {
        'ref': {
            'type': 'string',
            'description': 'Absolute path to file that contains the datastore definition',
            'examples': ['/abs/path/to/file.json']
        }
    },
    'examples': [
        {
            'datastore_1': {'ref': '/abs/path/to/file.json'}
        }
    ],
    'required': ['ref'],
    'additionalProperties': False
}