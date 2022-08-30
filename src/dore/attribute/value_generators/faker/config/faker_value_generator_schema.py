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
Faker Value Generator schema
"""

from dore.attribute.value_generators.value_generator_type import ValueGeneratorType


faker_value_generator_schema = {
    'title': 'Faker',
    'description': '<h4> Faker based attribute value generator </h4>'
                   '<p>'
                   ' With Dore, you can leverage the capabilities that '
                   ' <a href="https://faker.readthedocs.io/en/master/" target="_blank"> Python\'s Faker library </a>'
                   ' provides in order to generate values for attributes.'
                   '</p>'
                   '<p>'
                   ' Python\'s faker library uses the concept of '
                   ' <a href="https://faker.readthedocs.io/en/master/providers/baseprovider.html" target="_blank">'
                   ' `providers` </a> which **provide** methods to the faker instance. These methods, when invoked,'
                   ' generate a value. For example, the <a href="https://faker.readthedocs.io/en/master/providers/faker'
                   '.providers.misc.html?highlight=uuid#faker.providers.misc.Provider" target="_blank"> `misc` provider'
                   ' </a> provides a method <a href="https://faker.readthedocs.io/en/master/providers/'
                   'faker.providers.misc.html?highlight=uuid#faker.providers.misc.Provider" target="_blank"> `uuid4` '
                   ' </a>  that allows you to generate UUID4 strings. In a Python program, You can invoke this method '
                   ' by calling `fake.uuid4()` to get a randomly generated UUID4 string.'
                   '</p>'
                   '<p>'
                   ' In Dore manifest, Faker based attribute value configs follow a general structure which is '
                   ' depicted in the first example in the `Examples` below. Parameters required for a faker '
                   ' method can be provided by passing an object which contains the parameters as keys and the '
                   ' parameter values as values. Ex: `{ "param_1": "val2", "param_2": "val2" }`. For specifying a '
                   ' faker method should be invoked without any parameters, pass an empty object `{}`.'
                   '</p>',
    'examples': [
        {
            'value': {
                'faker': {
                    'faker_method_name': {
                        'a_param': 'val',
                        'another_param': 'val',
                    }
                }
            }
        },
        {
            'value': {
                "faker": {
                    "pyint": {
                        'min_value': 1,
                        'max_value': 3
                    }
                }
            }
        },
        {
            'value': {
                'faker': {
                    'uuid4': {}
                }
            }
        }
    ],
    'type': 'object',
    'properties': {
        ValueGeneratorType.FAKER.schema_key(): {
            'type': 'object',
            'description': '<p>'
                           ' All faker based configs should be present within the `faker` root object in the '
                           ' attribute `value` config.'
                           '</p>'
                           '<p>'
                           ' This object will contain an object with key as the required Faker method\'s name and '
                           ' value as parameters that we want to invoke the method with.'
                           '</p>',
            'examples': [
                {
                    'faker': {
                        "pyint": {
                            'min_value': 1,
                            'max_value': 3
                        }
                    }
                },
                {
                    'faker': {
                        'uuid': {}
                    }
                }
            ]
        }
    },
    'required': ['faker'],
    'additonalProperties': False
}
