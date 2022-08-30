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
Round Robin Selector Value Generator schema
"""

round_robin_selector_value_generator_schema = {
    'title': 'Round Robin Selector',
    'description': '<h4> Round Robin Selector </h4>'
                   '<p>'
                   ' Selects a value in a round robin manner from the list of values provided.'
                   '</p>',
    'type': 'object',
    'properties': {
        'roundRobin': {
            'title': 'Round Robin Selector',
            'description': '<h4> Round Robin Selector root object </h4>'
                           '<p>'
                           ' Use this object within the `selector` object in the manifest to indicate that we want '
                           'to  use the random selector.'
                           '</p>',
            'type': 'object',
            'properties': {
                'items': {
                    'title': 'Items',
                    'description': '<h4> Item List </h4>'
                                   '<p> List of items to select from. </p>'
                                   '<p> An item can be a number, a string, or an arbitrarily complex '
                                   'JSON object. </p>',
                    'type': 'array',
                    'items': {
                        'oneOf': [
                            {
                                'title': 'String',
                                'type': 'string',
                                'description': 'An item can be a simple string.'
                            },
                            {
                                'title': 'Number',
                                'type': 'number',
                                'description': 'An item can be a number.'
                            },
                            {
                                'title': 'Object',
                                'type': 'object',
                                'description': 'An item can be arbitrarily complex JSON object'
                            },
                        ]
                    }
                }
            },
            'required': ['items'],
            'additionalProperties': False
        },
    },
    'required': ['roundRobin'],
    'additionalProperties': False,
    'examples': [
        {
            'roundRobin': {
                'items': [
                    'item_1',
                    'item_2',
                    'item_3'
                ]
            }
        }
    ]
}
