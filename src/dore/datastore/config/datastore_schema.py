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
Datastore schema
"""

from dore.datastore.config.datastore_reference_schema import datastore_reference_schema
from dore.datastore.config.datastore_definition_schema import datastore_definition_schema

datastore_schema = {
    'title': 'Datastore',
    'type': 'object',
    'description': '<h4> Datastore </h4>'
                   '<p>'
                   ' You can think of a datastore as a *database in MySQL*, a *database in MongoDB*, an *Elasticsearch'
                   ' cluster*, and so on.'
                   '</p>'
                   '<p>'
                   ' Each protocol has a different way of implementing the datastore abstraction. Please refer to the'
                   ' protocol specific documentation for datastores to see how a particular protocol uses'
                   ' datastores.'
                   '</p>'
                   '<h5> In place vs Referenced definition </h5>'
                   '<p>'
                   'A datastore can either be defined in place or in a separate file.'
                   ' <ul>'
                   '  <li><p><b>In place</b><br> '
                   '  If you are defining the datastore in place, use the `Datastore Definition` schema for '
                   '  reference. </p></li>'
                   '  <li><p><b>Separate file</b><br>'
                   '  When the datastore is defined in a separate file, use the Datastore Reference schema instead to'
                   '  provide a `ref`erence to the file which contains the datastore definition. </p></li>'
                   ' </ul>'
                   '</p>',
    'oneOf': [
        datastore_definition_schema,
        datastore_reference_schema,
    ]
}
