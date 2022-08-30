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
MySQL Datastore Properties schema
"""

mysql_datastore_properties_schema = {
    'title': 'MySQL',
    'description': '<h4> MySQL datastore properties </h4>'
                   '<p>'
                   ' A datastore corresponds to a **MySQL database**.'
                   '</p>'
                   '<p>'
                   ' Use this when `datastore.protocol` is `mysql`.'
                   '</p>',
    'type': 'object',
    'properties': {
        'host': {
            'title': 'Host',
            'type': 'string'
        },
        'port': {
            'title': 'Port',
            'type': 'string'
        },
        'user': {
            'title': 'User',
            'description': 'MySQL `username` for connecting to the database.',
            'type': 'string'
        },
        'password': {
            'title': 'Password',
            'description': 'MySQL `password` for connecting to the database.',
            'type': 'string'
        },
        'database': {
            'title': 'Database name',
            'description': 'Name of the MySQL database to connect to',
            'type': 'string'
        },
    },
    'required': [
        'host',
        'port',
        'user',
        'password',
        'database',
    ],
    'additionalProperties': False,
    'examples': [
        {
            'properties': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'john_doe',
                'password': 'yourpassword',
                'database': 'foobar'
            }
        }
    ]
}
