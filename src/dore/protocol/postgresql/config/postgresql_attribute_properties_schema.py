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
PostgreSQL Attribute Properties schema
"""

postgresql_attribute_properties_schema = {
    'title': 'PostgreSQL',
    'description': '<h4>PostgreSQL attribute properties</h4>'
                   '<p>'
                   ' An attribute corresponds to a column of a PostgreSQL table'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model to which this attribute belongs refers to a'
                   ' datastore that uses the `postgres` protocol.'
                   '</p>',
    'type': 'object',
    'examples': [
        {
            'properties': {
                'columnName': 'foo',
                'columnType': 'DATETIME'
            }
        },
        {
            'properties': {
                'columnName': 'bar',
                'columnType': 'DECIMAL(5,2)'
            }
        }
    ],
    'properties': {
        'columnName': {
            'title': 'Column Name',
            'description': '<h4>Column Name</h4>'
                           '<p> '
                           ' Name of the PostgreSQL column that the attribute corresponds to.'
                           '</p>'
                           '<p>'
                           ' While creating tables in PostgreSQL for PostgreSQL bound models in the manifest, '
                           ' Dore infers the required column name from this field\'s value.'
                           '</p>',
            'type': 'string',
            'examples': ['column_one', 'column_two']
        },
        'columnType': {
            'title': 'Column Type',
            'description': '<h4>Column Type</h4>'
                           '<p>'
                           ' Data type of the PostgreSQL column that the attribute corresponds to.'
                           '</p>'
                           '<p>'
                           ' While creating tables in PostgreSQL for PostgreSQL bound models in the manifest, '
                           ' Dore infers the required data type for a column from this field\'s value.'
                           '</p>'
                           '<p>'
                           ' All <a target="_blank" href="https://www.postgresql.org/docs/current/datatype.html">'
                           ' data types supported by PostgreSQL</a> are supported here.'
                           '</p>',
            'type': 'string',
            'examples': ['DATETIME', 'DECIMAL(5,2)', 'CIDR']
        }
    },
    'required': ['columnName', 'columnType'],
    'additionalProperties': False,
}
