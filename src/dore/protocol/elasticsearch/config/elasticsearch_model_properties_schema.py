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
ElasticSearch8 Model Properties schema.
"""

elasticsearch_model_properties_schema = {
    'title': 'Elasticsearch',
    'description': '<h4>Elasticsearch model properties</h4>'
                   '<p>'
                   '  A model corresponds to an index in elasticsearch.'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model refers to a datastore'
                   ' that uses the `elasticsearch7` or `elasticsearch8` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'indexName': {
            'title': 'Index Name',
            'type': 'string',
            'description': '<h4> Index Name </h4>'
                           '<p> Name of the Elasticsearch Index that the model corresponds to. </p>'
                           '<p> While creating indices in Elasticsearch based on Elasticsearch bound models '
                           'in the manifest, Dore infers the fields and their data types from attribute config'
                           ' for the model.</p>',
            'examples': ['index_name', 'other_name']
        }
    },
    'required': ['indexName'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'indexName': 'index_name'
            }
        }
    ]
}
