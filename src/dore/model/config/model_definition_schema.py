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
Model Definition schema
"""

from dore.model.config.persistence_level import PersistenceLevel
from dore.model.config.model_properties_schema import model_properties_schema
from dore.attribute.config.attribute_container_schema import attribute_container_schema

model_definition_schema = {
    'title': 'Model Definition',
    'type': 'object',
    'description': '<h4> Model Definition </h4>'
                   'A standard model corresponds to a table in SQL database, an index in Elasticsearch, '
                   'a collection in MongoDB, etc. <br>',
    'properties': {
        'persistence': {
            'title': 'Persistence Level',
            'type': 'string',
            'enum': [PL.name for PL in PersistenceLevel],
            'description': '<h4> Persistence Level </h4>'
                           '<p> Dore allows you to specify various persistence levels for models </p>'
                           '<p> '
                           ' This is particularly useful when you have nested attributes that need'
                           ' to be represented as a separate model in itself. In such scenarios, you'
                           ' would often want to only generate records for that model and not persist '
                           ' it in the underlying database.'
                           '</p>'
                           '<p>'
                           ' Consider the case of a `customer` model which has a `shippingAddress` attribute. '
                           ' We would want to generate addresses for the customer and use those records '
                           ' as values for the `shippingAddress` attribute.'
                           ' Since addresses are complex structures with multiple components, we would perhaps'
                           ' represent it as a separate model in the manifest so Dore can generate records '
                           ' for it.'
                           '</p>'
                           '<p>'
                           ' But, we wouldn\'t want to persist the `address` model itself in the datastore. '
                           ' This would be the equivalent of having an `address` table with all addresses as '
                           ' rows in the table. We just want to use the model so that its records can be used '
                           ' for values in other attributes.'
                           '</p>'
                           '<h5> Persistence Levels </h5>'
                           '<p>'
                           ' The Persistence levels supported by Dore along with its implications are given'
                           ' below:'
                           ' <ul>'
                           f'  <li><p> `{PersistenceLevel.FULL.name}`: When this persistence level is used on a'
                           f' model, Dore creates a model for this in the underlying datastore and persists'
                           ' records generated for this model in the datastore. </p></li>'
                           f'  <li><p> `{PersistenceLevel.MEMORY_ONLY.name}`: When this persistence level is'
                           ' used on a model, Dore persists the records generated for the model in the *cache '
                           ' only* and does not create the model or persist records for the model in any'
                           ' datastore. </p></li>'
                           f'  <li><p> `{PersistenceLevel.NO_PERSIST.name}`: When this persistence level is'
                           f' used on a model, Dore does NOT persist the model or the records generated for'
                           f' it in cache nor in any datastore. Each record is generated on the fly and'
                           f' discarded after being used. '
                           f' </p></li>'
                           ' </ul>'
                           '</p>',
            'default': PersistenceLevel.default().name,
            'examples': [{'persistence': 'MEMORY_ONLY'}]
        },
        'records': {
            'title': 'Records Count',
            'description': '<h4> Records Count </h4>'
                           '<p> '
                           ' We can use this field to specify the number of records to be generated for the '
                           ' model.'
                           '</p>'
                           '<p>'
                           ' *Note:* The actual number of records that Dore generates will depend on the value '
                           ' provided here as well as the `scale_factor` provided during invocation.'
                           '</p>'
                           '<p>'
                           ' For example, if a model has `records` as `10000`, and we provide a `scale_factor` '
                           ' value of `0.1` when invoking Dore, the actual number of records generated by Dore'
                           ' will be `10000 * 0.1 = 1000`.'
                           '</p>',
            'type': 'integer',
            'examples': [{'records': 10000}]
        },
        'datastore': {
            'title': 'Datastore Reference',
            'description': '<h4> Datastore Reference </h4>'
                           'ID of the datastore to which this model belongs. This is a required field in cases'
                           ' of models that have `FULL` persistence levels.',
            'type': 'string',
            'examples': [{'datastore': 'datastoreId'}]
        },
        'properties': {**model_properties_schema},
        'attributes': {**attribute_container_schema}
    },
    'required': ['attributes'],
    'additionalProperties': False,
    'examples': [
        {
            'model-1': {
                'persistence': 'FULL',
                'records': 100,
                'datastore': 'datastoreId',
                'properties': "{ ** Protocol specific model properties ** }",
                'attributes': "{ ** Attributes Definition ** }"
            }
        }
    ]
}
