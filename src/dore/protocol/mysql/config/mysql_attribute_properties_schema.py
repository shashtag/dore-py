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
MySQL attribute properties schema
"""

mysql_attribute_properties_schema = {
    'title': 'MySQL',
    'description': '<h4>MySQL attribute properties</h4>'
                   '<p>'
                   '  An attribute corresponds to a column of a MySQL table.'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model to which this attribute belongs refers to a'
                   ' datastore that uses the `mysql` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'columnName': {
            'title': 'Column Name',
            'description': '<h4>Column Name</h4>'
                           '<p> '
                           ' Name of the MySQL column that the attribute corresponds to.'
                           '</p>'
                           '<p>'
                           ' While creating tables in MySQL for MySQL bound models in the manifest, '
                           ' Dore infers the required column name from this field\'s value.'
                           '</p>',
            'type': 'string',
            'examples': ['column_one', 'column_two']
        },
        'columnType': {
            'title': 'Column Type',
            'description': '<h4>Column Type</h4>'
                           '<p>'
                           ' Data type of the MySQL column that the attribute corresponds to.'
                           '</p>'
                           '<p>'
                           ' While creating tables in MySQL for MySQL bound models in the manifest, '
                           ' Dore infers the required data type for a column from this field\'s value.'
                           '</p>'
                           '<p>'
                           ' All <a target="_blank" href="https://dev.mysql.com/doc/refman/8.0/en/data-types.html">'
                           'data types supported by MySQL</a> are supported here.'
                           '</p>',
            'type': 'string',
            'examples': ['DATETIME', 'DECIMAL(5,2)', 'VARCHAR(4)']
        }
    },
    'required': ['columnName', 'columnType'],
    'additionalProperties': False,
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
    ]
}