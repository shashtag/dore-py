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
Model Properties schema :: mongodb
"""

mongodb_model_properties_schema = {
    'title': 'MongoDB',
    'description': '<h4>MongoDB model properties</h4>'
                   '<p>'
                   '  A model corresponds to a '
                   '<a href="https://www.mongodb.com/docs/manual/core/databases-and-collections/#collections"collection'
                   ' target="_blank"> collection </a> in a MongoDB database'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model refers to a datastore'
                   ' that uses the `mongodb` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'collectionName': {
            'title': 'Collection Name',
            'type': 'string',
            'description': '<h4> Collection Name </h4>'
                           '<p> Name of the MongoDB collection that the model corresponds to.<p>'
                           '<p> While creating collections in MongoDB for MongoDB bound models in the manifest,'
                           ' Dore infers the field names from attribute config for the model. </p>',
            'examples': ['some_collection', 'some_other_collection']
        }
    },
    'required': ['collectionName'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'collectionName': 'some_collection'
            }
        }
    ]
}
