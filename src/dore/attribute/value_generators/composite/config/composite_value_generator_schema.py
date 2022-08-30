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
Composite Value Generator schema
"""

from dore.attribute.value_generators.value_generator_type import ValueGeneratorType

composite_value_generator_schema = {
    'title': 'Composite',
    'description': '<h4> Composite attribute value generator </h4>'
                   '<p>'
                   ' The composite attribute value generator is similar to the `ref` attribute value generator in '
                   ' the sense that you can have attributes of a model be dependent on other models. But, it is'
                   ' different in one major way: While you would use the '
                   ' `ref` attribute value generator when you want values of an attribute of a particular model '
                   ' be dependent on the values of another attribute of a different model, the `composite` attribute '
                   ' value generator lets you assign the value of an attribute to be an *entire record* of the '
                   'dependent model.'
                   '</p>'
                   '<p>'
                   ' When an attribute uses a `composite` value generator, an entire record of the '
                   ' dependent model would be used as the value for the attribute. In other words, the attribute will'
                   ' have an *object* as a value and the value is a record of the dependent model.'
                   '</p>'
                   '<p>'
                   ' This is particularly useful in cases of NoSQL databases where we can have attributes that can be'
                   ' arbitrarily complex objects.'
                   '</p>'
                   '<p>'
                   ' Consider an example where you have a `customer` model with the following attributes:'
                   ' <ul>'
                   '  <li><p> `customerId`: unique ID for the customer. </p></li>'
                   '  <li><p> `billingAddress`: Billing address for the customer. </p></li>'
                   '  <li><p> `shippingAddress`: Shipping address for the customer.'
                   ' </ul>'
                   '</p>'
                   ' Addresses are generally complex in structure with many sub components. We can represent address as'
                   ' a separate model in the manifest, let Dore generate records for it, and use the generated records'
                   ' in their entirety as values for the `billingAddress` or `shippingAddress`.'
                   '</p>'
                   '<p>'
                   ' We can create an `address` model with the following attributes:'
                   ' <ul>'
                   '  <li><p>`house_number`</p></li>'
                   '  <li><p>`residence_name`: The apartment / building / society name. </p></li>'
                   '  <li><p>`street`: name of the street </p></li>'
                   '  <li><p>`state`'
                   '  <li><p>`country`</li></p>'
                   '  <li><p>`pin_code`</li></p>'
                   ' </ul>'
                   '</p>'
                   '<p>'
                   ' And specify that the `billingAddress`/`shippingAddress` attribute of the `customer` model has a '
                   ' `value` config of `composite` type and provide a reference to the address model\'s ID to it '
                   ' (This is illustrated in the second example below).'
                   '</p>'
                   '<p>'
                   ' The general structure of the `value` config for a `composite` attribute value generator is'
                   ' illustrated in the first example.'
                   '</p>',
    'type': 'object',
    'examples': [
        {
            'composite': {
                'ref': 'modelId'
            }
        },
        {
            'composite': {
                'ref': 'address'
            }
        }
    ],
    'properties': {
        ValueGeneratorType.COMPOSITE.schema_key(): {
            'type': 'object',
            'properties': {
                'ref': {
                    'type': 'string',
                    'description': '<h4> Model Reference </h4>. '
                                   '<p> '
                                   ' Use ID of the referenced model as values here.'
                                   ' A record of the referenced model will be used as value for this attribute.'
                                   '</p>'
                }
            },
            'required': ['ref']
        }
    },
    'required': ['composite']
}
