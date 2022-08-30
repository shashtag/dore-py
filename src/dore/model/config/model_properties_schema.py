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
Model Properties schema
"""

from dore.protocol.mysql.config.mysql_model_properties_schema import mysql_model_properties_schema
from dore.protocol.mongodb.config.mongodb_model_properties_schema import mongodb_model_properties_schema
from dore.protocol.postgresql.config.postgresql_model_properties_schema import postgresql_model_properties_schema
from dore.protocol.elasticsearch.config.elasticsearch_model_properties_schema \
    import elasticsearch_model_properties_schema

model_properties_schema = \
{
    'title': 'Model Properties',
    'description': '<h4> Model Properties </h4>'
                   '<p>'
                   ' This config is used to specify protocol specific model properties such as table properties in SQL,'
                   ' index properties in Elasticsearch, collection properties in MongoDB, etc.'
                   '</p>'
                   '<p>'
                   ' As protocol specific properties of a model are required only when there is a need to persist'
                   ' the model and it\'s records in any datastore, the `properties` field is a **required** field only'
                   ' when `persistence` on a model is set to `"FULL"` or is not explicitly mentioned in the manifest as'
                   ' the Dore assumes the default `persistence` as `"FULL"` if not specified.'
                   '</p>'
                   '<p>'
                   '  Since each protocol has different requirements for configuring'
                   '  a model, this config varies from one protocol to the other. '
                   '  Please refer to the protocol specific sections below to view which fields'
                   '  are required for a particular protocol.'
                   '</p>',
    'type': 'object',
    'oneOf': [
        {**mysql_model_properties_schema},
        {**postgresql_model_properties_schema},
        {**mongodb_model_properties_schema},
        {**elasticsearch_model_properties_schema}
    ]
}
