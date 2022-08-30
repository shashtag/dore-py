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
MySQL Model Properties schema
"""

mysql_model_properties_schema = {
    'title': 'MySQL',
    'description': '<h4> MySQL model properties </h4>'
                   '<p>'
                   '  A model corresponds to a table in a MySQL database.'
                   '</p>'
                   '<p>'
                   ' Use this schema when the `datastore` id on the model refers to a datastore'
                   ' that uses the `mysql` protocol.'
                   '</p>',
    'type': 'object',
    'properties': {
        'tableName': {
            'title': 'Table Name',
            'type': 'string',
            'description': '<h4> Table Name </h4>'
                           '<p>'
                           ' Name of the MySQL table that the model corresponds to. '
                           '</p>'
                           '<p>'
                           ' While creating tables in MySQL for MySQL bound models in the manifest, '
                           ' Dore infers the required columns and their data types from attribute '
                           ' config for the model.'
                           '</p>',
            'examples': ["some_table", "some_other_table"]
        }
    },
    'required': ['tableName'],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'tableName': 'some_table'
            }
        }
    ]
}
