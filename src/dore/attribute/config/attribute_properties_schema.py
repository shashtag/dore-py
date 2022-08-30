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
Attribute Properties schema
"""

from dore.protocol.mysql.config.mysql_attribute_properties_schema import mysql_attribute_properties_schema
from dore.protocol.mongodb.config.mongodb_attribute_properties_config import mongodb_attribute_properties_schema
from dore.protocol.postgresql.config.postgresql_attribute_properties_config import postgresql_attribute_properties_schema
from dore.protocol.elasticsearch.config.elasticsearch_attribute_properties_schema \
    import elasticsearch_attribute_properties_schema

attribute_properties_schema = \
{
    'title': 'Attribute Properties',
    'type': 'object',
    'description': '<h4> Attribute Properties </h4>'
                   '<p>'
                   ' This config is used to specify protocol specific attribute properties'
                   ' such as *column name* and *data type* for a MySQL column, *field name* and *field '
                   ' type* for an elasticsearch index, and so on.'
                   '</p>'
                   '<p>'
                   ' Dore uses this config for creating models and running queries on them in the underlying'
                   ' datastore.'
                   '<p>'
                   '<p>'
                   ' Since each protocol has different requirements for configuring an attribute,'
                   ' this config varies from one protocol to the other.'
                   ' Please refer to the protocol specific sections below to view which fields are'
                   ' required for a particular protocol.'
                   '</p>',
    'anyOf': [
        {**mysql_attribute_properties_schema},
        {**postgresql_attribute_properties_schema},
        {**mongodb_attribute_properties_schema},
        {**elasticsearch_attribute_properties_schema}
    ]
}
