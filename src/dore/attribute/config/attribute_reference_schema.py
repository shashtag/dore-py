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
Attribute Reference schema
"""

attribute_reference_schema = {
    'title': 'Attribute Reference',
    'description': '<h4> Attribute Reference </h4>'
                   '<p>'
                   ' An attribute can be defined in a file separate from the manifest file.'
                   '</p>'
                   '<p>'
                   ' You can, if you want, define each attribute in a separate file similar to how you can store'
                   ' each model and datastore in a separate file. We have no recommendations for or against this. '
                   ' So, you might want to take a call to start splitting attributes across different'
                   ' files if you feel your model file is getting too large and difficult to read.'
                   '</p>'
                   ' Use this schema when the attribute is defined in a separate file and you need to provide a '
                   ' reference to that file in the manifest.'
                   '</p>'
                   ' <p>'
                   ' Use the `ref` field in the manifest and provide absolute path to the file that actually'
                   ' contains the <a href="#tab-pane_datastores_pattern1_oneOf_i0">attribute definition </a>.'
                   '</p>'
                   ' In the example, the definition for `attribute_1` is present in a separate file and the'
                   ' `ref`erence to that file is added in the manifest.'
                   '</p>',
    'type': 'object',
    'examples': [
        {
            'attribute_1': {
                'ref': '/abs/path/to/file.json'
            }
        }
    ],
    'properties': {
        'ref': {
            'type': 'string',
            'description': 'Absolute path to file that contains the attribute definition',
            'examples': ['/abs/path/to/file.json']
        }
    },
    'required': ['ref'],
    'additionalProperties': False
}
