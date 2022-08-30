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
Attribute schema
"""

from dore.attribute.config.attribute_reference_schema import attribute_reference_schema
from dore.attribute.config.attribute_definition_schema import attribute_definition_schema

attribute_schema = {
    'type': 'object',
    'title': 'Attribute',
    'description': '<h4>Attribute</h4>'
                   '<p> Generally, models have attributes associated with them. '
                   'You can think of an attribute as a *column* of a MySQL table (where the model '
                   'corresponds to the table), a *field* of an Elasticsearch index (where the model corresponds '
                   'to the index), a *field* of a MongoDB collection (where the model corresponds to the MongoDB '
                   'collection), and so on. </p>'
                   '<p> An attribute can either be defined in place or in a separate file <p>'
                   '<ul>'
                   '  <li>'
                   '    <p><b>In place:</b> If you are defining the attribute in place, use the Attribute Definition'
                   '    schema for reference </p>'
                   '  </li>'
                   '  <li>'
                   '    <p><b>Separate file:</b> When the attribute is defined in a separate file, use the Attribute'
                   '       Reference schema instead to provide a `ref`erence to the file which contains the attribute '
                   '       definition.</p>'
                   '  </li>'
                   '</ul>',
    'examples': [
        {
            'attributes': {
                'attribute_1': {
                    'ref': '/abs/path/to/file.json'
                },
                'attribute_2': {
                    'properties': {
                        'columnName': 'foobar',
                        'columnType': 'DATE'
                    },
                    'value': {
                        'faker': {
                            'date_between': {
                                'start_date': '-1M'
                            }
                        }
                    }
                }
            }
        }
    ],
    'oneOf': [
        attribute_definition_schema,
        attribute_reference_schema
    ]
}
