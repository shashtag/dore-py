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
Model schema
"""

from dore.model.config.model_reference_schema import model_reference_schema
from dore.model.config.model_definition_schema import model_definition_schema

model_schema = {
    'title': 'Model',
    'type': 'object',
    'description': '<h4> Model </h4>'
                   '<p>'
                   ' You can think of a model as *table* in MySQL, an *index* in Elasticsearch, '
                   'a *collection* in MongoDB, and so on.'
                   '</p>'
                   '<p>'
                   ' Each protocol has a different way of implementing the model abstraction. Please '
                   ' refer to the protocol specific documentation for models to see how a particular protocol '
                   ' uses the model abstraction.'
                   '</p>'
                   '<h5> In place vs Referenced definition </h5>'
                   '<p> A model can either be defined in place or in a separate file. </p>'
                   '<ul>'
                   ' <li>'
                   '  <p>'
                   '    <b>In place</b> '
                   '    <br>'
                   '    If you are defining the model in place, use the'
                   '    <a href="#tab-pane_models_pattern1_oneOf_i0"> Model Definition </a> schema for reference. '
                   '  </p>'
                   ' </li>'
                   ' <li>'
                   '  <p>'
                   '   <b>Separate file</b>'
                   '   <br>'
                   '   When the model is defined in a separate file, use the '
                   '   <a href="#tab-pane_models_pattern1_oneOf_i1"> Model Reference </a>'
                   '   schema instead to provide a `ref`erence to the file which contains the model definition.'
                   '  </p>'
                   ' </li>'
                   '</ul>',

    'oneOf': [
        model_definition_schema,
        model_reference_schema
    ]
}
