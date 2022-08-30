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
Manifest schema.
"""

from dore.model.config.model_container_schema import model_container_schema
from dore.datastore.config.datastore_container_schema import datastore_container_schema

manifest_schema = {
    'title': 'Dore Manifest schema',
    'type': 'object',
    'description': '<h3> Introduction </h3>'
                   '<p> '
                   ' This page contains documentation about the structures and components that form the Dore manifest.'
                   '</p>'
                   '<p>'
                   ' Before reading the schema and fields mentioned in this document, it might be helpful to remember '
                   ' what Dore\'s core functionality is as this will help in understanding how the various components '
                   ' and fields in the manifest come together in the big picture.'
                   '</p>'
                   '<p>'
                   ' Fundamentally, Dore is a schema based fake data generation tool. '
                   '</p>'
                   '<p>'
                   ' It supports data generation for various protocols (MySQL, MongoDB, Elasticsearch, etc) '
                   ' with the ability to generate data which adheres to the referential integrity constraints and inter'
                   ' schema dependencies.'
                   ' The referential integrity is maintained irrespective of which protocol either of the models reside'
                   ' in are using.'
                   '</p>'
                   '<h5> How it Works </h5>'
                   '<p>'
                   ' We start by creating the manifest which contains details about the schema based on which'
                   ' data is to be generated. The manifest contains details for `models` (which are analogous to'
                   ' tables in SQL), the attributes of models (which are analogous to columns of a SQL table), and'
                   ' `datastores` (which are analogous to databases in SQL).'
                   '</p>'
                   '<p>'
                   ' Once the manifest is created, we invoke Dore with it.'
                   '</p>'
                   '<p>'
                   ' Dore reads the manifest and proceeds to generate data for models by analyzing'
                   ' the model\'s attributes and their dependencies. It generates values for each attribute of a model '
                   ' and the collection of values for a model\'s attributes forms a record for the model which is then '
                   ' persisted in the datastore. This is done until Dore has generated the required number of records'
                   ' for each of the models.'
                   '</p>'
                   '<h5> Manifest Schema Summary </h5>'
                   '<p>'
                   ' The high level structure of the manifest is as shown below. The list here is intentionally not '
                   ' exhaustive as we want to take a look at the forest from the sky before we actually go into it'
                   ' in order to avoid getting lost. The exhaustive schema documentation can be referred to in the '
                   ' later sections'
                   '</p>'
                   '<p>'
                   ' A manifest has:'
                   ' <ol>'
                   '   <li><p>`id`: a string identifier for the manifest. </p></li>'
                   '   <li>'
                   '    <p>`datastores`: a set of `datastore` configs. </p>'
                   '    <p> Each `datastore` has: </p>'
                   '    <ol>'
                   '     <li><p>`protocol`: indicates which protocol the datastore uses (`MySQL`, `MongoDB`, etc).'
                   '             </p></li>'
                   '     <li><p>`properties`: protocol specific datastore properties and connection info. </p></li>'
                   '    </ol>'
                   '   </li>'
                   '   <li>'
                   '      <p>`models`: a set `model` configs.</p>'
                   '      <p> Each `model` has: </p>'
                   '      <ol>'
                   '       <li><p>`datastore`: indicates which datastore the model belongs to.</p></li>'
                   '       <li><p>`properties`: protocol specific model properties.</p></li>'
                   '       <li><p>`attributes`: set of attributes and their configs for the model.</p>'
                   '        <p>Each `attribute` has: </p>'
                   '         <ol>'
                   '          <li><p>`properties`: protocol specific attribute properties.</p></li>'
                   '          <li><p>`value`: indicates how value for the attribute should be generated.</p></li>'
                   '         </ol>'
                   '       </li>'
                   '      </ol>'
                   '   </li>'
                   ' </ol>'
                   '</p>'
                   '<h3> Schema Documentation </h3>'
                   '<p> The sections below describe the manifest schema in detail. </p>',
    'properties': {
        'id': {
            'type': 'string',
            'description': '<h4> Manifest ID </h4>'
                           '<p>'
                           ' Although Dore does not use the Manifest ID, it proves helpful to have an ID as part of the'
                           ' manifest to understand what we are looking at without referencing the file name. The id'
                           ' has thus been kept as a `required` field.'
                           '</p>',
            'required': True,
            'examples': [{'id': 'tpch-manifest'}]
        },
        'datastores': {**datastore_container_schema},
        'models': {**model_container_schema},
    },
    'additionalProperties': False,
    'required': ['id', 'models', 'datastores']
}
