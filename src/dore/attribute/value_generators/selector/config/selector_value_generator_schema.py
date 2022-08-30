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
Selector Value Generator schema
"""

from dore.attribute.value_generators.value_generator_type import ValueGeneratorType
from dore.attribute.value_generators.selector.random_selector.config.random_selector_value_generator_schema \
    import random_selector_value_generator_schema
from dore.attribute.value_generators.selector.round_robin_selector.config.round_robin_selector_value_generator_schema \
    import round_robin_selector_value_generator_schema

selector_value_generator_schema = {
    'title': 'Selector',
    'description': '<h4> Selector based attribute value generator </h4>'
                   '<p>'
                   ' Dore allows you to define a list of values from which a value is selected for an attribute during'
                   ' record generation.'
                   '</p>'
                   '<p>'
                   ' Consider an example where you have an attribute representing the size of a T-shirt and you wanted '
                   ' the value of this attribute to be one of the following values: `"S"`, `"L"` or `"XL"` picked at '
                   ' random for each record. You can use the *Random Selector* for this. If, for example, you wanted '
                   ' the T-shirt size value to be picked from the list above in a round robin fashion for each record, '
                   ' you can use the *Round Robin Selector*'
                   '</p>'
                   '<p>'
                   ' Each section in the `selector` field below illustrates one of the various selector based value '
                   ' generators supported by Dore and contains documentation on how to use a particular selector.'
                   '</p>',
    'type': 'object',
    'properties': {
        ValueGeneratorType.SELECTOR.schema_key(): {
            'type': 'object',
            'oneOf': [
                random_selector_value_generator_schema,
                round_robin_selector_value_generator_schema
            ]
        }
    },
    'required': ['selector'],
    'additonalProperties': False,
    'examples': [
        {
            'selector': {
                'random': {
                    'items': [
                        'M'
                        'L',
                        'XL',
                        'XXL'
                    ]
                }
            }
        },
        {
            'selector': {
                'roundRobin': {
                    'items': [
                        'M',
                        'L',
                        'XL',
                        'XXL'
                    ]
                }
            }
        }
    ]
}
