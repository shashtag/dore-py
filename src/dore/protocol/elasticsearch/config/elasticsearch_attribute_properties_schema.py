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
ElasticSearch8 Attributes Properties schema
"""

elasticsearch_attribute_properties_schema = {
    'title': 'Elasticsearch',
    'description': '<h4> Elasticsearch attribute properties </h4>'
                   '<p>'
                   ' An attribute corresponds to a '
                   '<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html'
                   '#documents-indices" target="_blank"> field of an elasticsearch index </a>.'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model to which this attribute belongs refers to a'
                   ' datastore that uses the `elasticsearch7` or `elasticsearch8` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'fieldName': {
            'title': 'Field Name',
            'description': '<h4> Field Name </h4>'
                           '<p>'
                           ' Name of the Elasticsearch field that the attribute corresponds to.'
                           '</p>',
            'type': 'string',
            'examples': ["foo", "bar"]
        },
        'fieldType': {
            'title': 'Field Type',
            'description': '<h4> Field Type </h4>'
                           '<p>'
                           ' While creating indices in Eleasticsearch for elasticsearch bound models in the'
                           ' manifest, Dore creates an index and an'
                           '<a href="https://www.elastic.co/guide/en/elasticsearch/reference/8.3/explicit-mapping.html#'
                           'create-mapping" target="_blank"> index mapping </a> before generating and storing records'
                           ' for the model. Dore uses the `fieldType` value to assign the right data types for fields '
                           ' when creating an index mapping in Elasticsearch.'
                           '</p>'
                           '<p>'
                           ' You can use any '
                           ' <a href="https://www.elastic.co/guide/en/elasticsearch/reference/8.3/mapping-types.html"'
                           ' target="_blank"> field data type that is supported by elasticsarch </a> here.'
                           '</p>',
            'oneOf': [
                {
                    'title': 'Simple Data Types',
                    'type': 'string',
                    'description': 'Use this when field types can be represented as strings.',
                    'examples': ['int', 'keyword']
                },
                {
                    'title': 'Complex Data Types',
                    'type': 'object',
                    'description': 'Use this when field types need to be represented as objects.',
                    'examples': [
                        {
                            'type': 'date_range',
                            'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                        }
                    ]
                }
            ],
            'examples': [
                {
                    'fieldType': 'int'
                },
                {
                    'fieldType': 'keyword'
                },
                {
                    'fieldType':  {
                        'type': 'date_range',
                        'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                    }
                }
            ]
        }
    },
    'required': ['fieldName', 'fieldType'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'fieldName': 'foo',
                'fieldType': 'int'
            }
        },
        {
            'properties': {
                'fieldName': 'bar',
                'fieldType': {
                    'time_frame': {
                        'type': 'date_range',
                        'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                    }
                }
            }
        }
    ]
}
