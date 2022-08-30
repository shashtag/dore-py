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
Random Selector Value Generator schema
"""

random_selector_value_generator_schema = {
    'title': 'Random Selector',
    'description': '<h4> Random Selector </h4>'
                   '<p> '
                   ' Selects values at random for an attribute from the list of values provided.'
                   '</p>'
                   '<p> '
                   ' Each value in the list is usually equally likely to be picked. </p>'
                   '</p>',
    'type': 'object',
    'properties': {
        'random': {
            'title': 'Random Selector',
            'description': '<h4> Random Selector root object </h4>'
                           '<p>'
                           ' Use this object within the `selector` object to indicate that we want to use the'
                           ' random selector.'
                           '</p>',
            'type': 'object',
            'properties': {
                'items': {
                    'title': 'Items',
                    'description': '<h4> Item List </h4>'
                                   '<p> List of items to select from. </p>'
                                   '<p> Any item can be a number, a string, or an arbitrarily complex '
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
            'additionalProperties': False,
        },
    },
    'required': ['random'],
    'additionalProperties': False,
    'examples': [
        {
            'random': {
                'items': [
                    'item 1',
                    'item 2',
                    'item 3'
                ]
            }
        }
    ]
}
