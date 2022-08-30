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
Attribute Definition schema
"""

from dore.attribute.config.attribute_value_schema import attribute_value_schema
from dore.attribute.config.attribute_properties_schema import attribute_properties_schema

attribute_definition_schema = {
    'title': 'Attribute Definition',
    'type': 'object',
    'description': '<h4> Attribute Definition </h4>'
                   '<p> '
                   ' You can think of an attribute as a *column* of a MySQL table (where the model '
                   ' corresponds to the table), a *field* of an Elasticsearch index (where the model '
                   ' corresponds to the index), a *field* of a MongoDB collection (where the model corresponds '
                   ' to the MongoDB collection), and so on. '
                   '</p>'
                   '<p> '
                   ' On a high level, we need to provide two types of information about an attribute'
                   ' to Dore in order for Dore to generate data: '
                   ' <ul>'
                   '  <li><p> '
                   '   The second type of information we need to provide is *How should values for the'
                   '   attribute be generated*?<br> '
                   '   We use the `value` field of the attribute definition to specify'
                   '   this information.'
                   '  </p></li>'
                   '  <li><p> '
                   '   The first is *How should/is the attribute represented in the underlying datastore*?<br>'
                   '   We use the `properties` field of the attribute definition to specify this information.'
                   '  </p></li>'
                   ' </ul>',
    'properties': {
        'value': attribute_value_schema,
        'properties': attribute_properties_schema
    },
    'required': [
        'value', 'properties'
    ],
    'additionalProperties': False
}
