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
Ref Value Generator schema
"""

from dore.attribute.value_generators.value_generator_type import ValueGeneratorType

ref_value_generator_schema = {
    'title': 'Ref',
    'description': '<h4> Ref attribute value generator </h4>'
                   '<p> '
                   ' Often times, we would want the value of an attribute to be based on the value of an attribute of '
                   ' a different model.'
                   '<p>'
                   ' A typical scenario where we might want do this is while generating data in'
                   ' a relational database with Foreign Key dependencies.'
                   '</p>'
                   '<p>'
                   ' Consider an example of a schema where you are recording invoices generated by a business.'
                   ' An invoice generally has a customer associated with it.'
                   '</p>'
                   '<p>'
                   '<p>'
                   ' On attempting to represent this scenario in a database schema, You would have a `customer` model '
                   ' which would have some of the following attributes:'
                   ' <ul>'
                   '  <li>'
                   '    <p> `customerId`: a unique ID for the customer. </p>'
                   '    <p>  This is a primary key for the customer model. </p>'
                   '  </li>'
                   '  <li> `name`: Customer\'s name.'
                   '  <li> `address`: The customer\'s address.'
                   ' </ul>'
                   '</p>'
                   ' And you would have an `invoice` model which would have some of the following attributes:'
                   ' <ul>'
                   '  <li> `invoiceId`: a unique ID for the invoice. </li>'
                   '  <li> `date`: Date when the invoice was created. </li>'
                   '  <li>'
                   '    <p>`customerId`: ID of the customer to whom the invoice is addressed. </p>'
                   '    <p> This is a foreign key which references the `customerId` of the customer model'
                   '  </li>'
                   ' </ul>'
                   '</p>'
                   '<p>'
                   ' When we want to generate data for this schema with Dore, we can specify the value config '
                   ' for `customerId` in the `invoice` model as a `ref` value and provide a reference to the '
                   ' dependent attribute and model, which is the `customerId` attribute of the `customer` model in this'
                   ' case. Please refer the examples below on how to specify these references.'
                   '</p>'
                   '<p>'
                   ' When we do this, Dore uses the `customer` model\'s `customerId` values as values for the '
                   ' `customerId` attribute for the `invoice` model.'
                   '</p>'
                   '<p>'
                   ' Before Dore starts generating records for any model, it analyzes the attribute and model '
                   ' dependencies and creates an iteration order over the models based on topological sorting of their'
                   ' dependencies. By doing this, Dore ensures that records for a model which has other models'
                   ' dependent on it are generated before generating records for the dependent models.'
                   '</p>',
    'examples': [
        {
            'ref': 'modelId.attributeId'
        },
        {
            'ref': 'customer.customerId'
        }
    ],
    'type': 'object',
    'properties': {
        ValueGeneratorType.REF.schema_key(): {
            'title': 'Attribute Reference',
            'description': '<h4> Attribute Reference </h4>'
                           '<p> Attribute references here take have the following syntax: `modelId.attributeId`. </p>',
            'type': 'string',
        }
    },
    'required': ['ref'],
    'additonalProperties': False
}
