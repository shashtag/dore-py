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
Attribute Properties schema :: mongodb
"""

mongodb_attribute_properties_schema = {
    'title': 'MongoDB',
    'description': '<h4>MongoDB attribute properties</h4>'
                   '<p>'
                   ' An attribute corresponds to a '
                   '<a href="https://www.mongodb.com/docs/manual/core/document/#document-structure" target="_blank"> '
                   ' field of a MongoDB collection </a>'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model to which this attribute belongs refers to a'
                   ' datastore that uses the `mongodb` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'fieldName': {
            'title': 'Field Name',
            'description': '<h4>Field Name</h4>'
                           '<p>'
                           ' Name of the MongoDB field that the attribute corresponds to.'
                           '</p>'
                           '<p>'
                           ' While creating collections in MongoDB for MongoDB bound models in the manifest,'
                           ' Dore infers the required field name from this field\'s value.'
                           '</p>',
            'type': 'string',
            'examples': ['field_one', 'another_field']
        }
    },
    'required': ['fieldName'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'fieldName': 'foo'
            }
        }
    ]
}