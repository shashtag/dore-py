# Copyright 2022 Bhargav KN
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
# ==============================================================================

"""
Attribute Container schema
"""

from dore.attribute.config.attribute_schema import attribute_schema

attribute_container_schema = {
    'title': 'Attribute Container',
    'type': 'object',
    'description': '<h4> Attribute Container </h4>'
                   '<p> '
                   ' All attribute definitions for a model go here. '
                   '</p>'
                   '<p>'
                   ' Each model will generally have a set of attributes associated with it. '
                   ' You can think of an attribute as a *column* of a MySQL table (where the model '
                   ' corresponds to the table), a *field* of an Elasticsearch index (where the model corresponds '
                   ' to the index), a *field* of a MongoDB collection (where the model corresponds to the MongoDB '
                   ' collection), and so on. '
                   '</p>'
                   '<p>'
                   ' Please refer to the protocol specific attribute documentation for more information on how '
                   ' a particular protocol implements the **attribute** abstraction.'
                   '</p>'
                   '<p>'
                   ' Each attribute can be defined as an object with key as the attribute\'s ID '
                   ' (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and '
                   ' value as the attribute\'s definition. Please refer the **Attribute** definition schema for'
                   ' reference'
                   '</p>',
    'patternProperties': {
        r'^[A-Za-z]+[A-Za-z0-9_\-]': {**attribute_schema}
    },
    'additionalProperties': False,
    'examples': [
        {
            'model-1': {
                'attributes': {
                    'attribute-1': '{ ** Attribute definition ** }',
                    'attribute-2': '{ ** Attribute definition ** }'
                }
            }
        }
    ]
}
