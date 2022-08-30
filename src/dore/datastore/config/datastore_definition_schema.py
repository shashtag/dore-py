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
Datastore Definition schema
"""

from dore.protocol.dore_protocol import DoreProtocol
from dore.protocol.mysql.config.mysql_datastore_properties_schema import mysql_datastore_properties_schema
from dore.protocol.mongodb.config.mongodb_datastore_properties_schema import mongodb_datastore_properties_schema
from dore.protocol.postgresql.config.postgresql_datastore_properties_schema import postgresql_datastore_properties_schema
from dore.protocol.elasticsearch.config.elasticsearch_datastore_properties_schema import elasticsearch_datastore_properties_schema

datastore_definition_schema = {
    'title': 'Datastore Definition',
    'description': '<h4> Datastore Definition </h4>'
                   '<p>'
                   ' A standard datastore corresponds to a **MySQL database**, an **Elasticsearch cluster**, '
                   ' a **MongoDB database**, etc.'
                   '</p>'
                   '<p>'
                   ' In a datastore definition, we specify what the properties of the system (database, etc) '
                   ' that Dore is trying to connect to are and details on how to connect to it.'
                   '</p>',
    'type': 'object',
    'examples': [
        {
            'protocol': 'mysql',
            'properties': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'john_doe',
                'password': 'yourpassword',
                'database': 'foobar'
            }
        }
    ],
    'properties': {
        'protocol': {
            'title': 'Protocol',
            'description': '<h4> Protocol </h4>'
                           '<p>'
                           ' The protocol / type of system that the datastore represents.'
                           '</p>',
            'type': 'string',
            'enum': [protocol.name.casefold() for protocol in DoreProtocol],
            'examples': [{'protocol': 'mysql'}, {'protocol': 'elasticsearch7'}]
        },
        'properties': {
            'title': 'Datastore Properties',
            'description': '<h4> Datastore Properties </h4>'
                           '<p>'
                           ' This config is used to specify protocol specific datastore properties such as'
                           ' *which MySQL database to use*, *host name of the Elasticsearch cluster*, *what'
                           ' are the credentials for accessing the database*, etc.'
                           '</p>'
                           '<p>'
                           ' Since each protocol has different requirements for configuring / connecting to'
                           ' the underlying system, this config varies from one protocol to the other. '
                           ' Please refer to the protocol specific sections below to view which fields are '
                           ' required for a particular protocol.'
                           '</p>',
            'anyOf': [
                {**mysql_datastore_properties_schema},
                {**postgresql_datastore_properties_schema},
                {**mongodb_datastore_properties_schema},
                {**elasticsearch_datastore_properties_schema},
            ]
        },
    },
    'required': ['protocol', 'properties'],
    'additionalProperties': False
}
