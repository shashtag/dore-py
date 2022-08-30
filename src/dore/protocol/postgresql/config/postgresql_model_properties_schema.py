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
PostgreSQL Model Properties schema
"""

postgresql_model_properties_schema = {
    'title': 'PostgreSQL',
    'description': '<h4>PostgreSQL model properties</h4>'
                   '<p>'
                   '  A model corresponds to a table in a PostgreSQL database.'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model refers to a datastore'
                   ' that uses the `postgres` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'tableName': {
            'title': 'Table Name',
            'type': 'string',
            'description': '<h4> Table Name </h4>'
                           '<p> Name of the PostgreSQL table that the model corresponds to. </p>'
                           '<p> While creating tables in PostgreSQL based on PostgreSQL bound models in the manifest, '
                           'Dore infers the required columns and their data types from attribute config for the '
                           'model. </p>',
            'examples': ['some_table', 'some_other_table']
        },
        'schemaName': {
            'title': 'PostgreSQL schema name',
            'type': 'string',
            'description': '<h4> PostgreSQL schema name </h4>'
                           '<p> Name of the PostgreSQL schema for the table that the model corresponds to. </p>',
            'examples': ['schema_name', 'some_other_schema_name']
        }
    },
    'required': ['tableName', 'schemaName'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'tableName': 'some_table',
                'schemaName': 'some_schema'
            }
        }
    ]
}
