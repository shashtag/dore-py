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
Datastore Container schema
"""

from dore.datastore.config.datastore_schema import datastore_schema

datastore_container_schema = \
{
    'title': 'Datastore Container',
    'description': '<h4> Datastore Container </h4>'
                   '<p> All datastore definitions go here. </p>'
                   '<p>'
                   ' You can think of datastores as **MySQL databases**, a **MongoDB databases**, '
                   ' an **Elasticsearch clusters**, etc. '
                   '</p>'
                   '<p>'
                   ' Each datastore can be defined as an object with key as the datastore\'s ID'
                   ' (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and value'
                   ' as the datastore definition (view definition schema for reference) </p>'
                   '</p>',
    'type': 'object',
    'examples': [
        {
            'datastores': {
                'a_datastore': {
                    'ref': '/abs/path/to/a_datastore_definition.json'
                },
                'another_datastore': {
                    'protocol': 'elasticsearch',
                    'properties': {
                        'host': '127.0.0.1',
                        'port': '9200',
                        'user': 'john_doe',
                        'password': 'yourpassword'
                    }
                }
            }
        }
    ],
    'patternProperties': {
        r'^[A-Za-z]+[A-Za-z0-9_\-]': {**datastore_schema}
    },
    'additionalProperties': False,
}
