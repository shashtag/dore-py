# Copyright 2022 Bhargav KN
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Model Container schema
"""

from dore.model.config.model_schema import model_schema

model_container_schema = \
    {
        'title': 'Model Container',
        'type': 'object',
        'description': '<h4> Model Container </h4>'
                       '<p> '
                       ' All model definitions go here. '
                       '</p>'
                       '<p> '
                       ' You can think of a model as a MySQL table, an Elasticsearch index, '
                       ' a collection in MongoDB, etc. '
                       '</p>'
                       '<p>'
                       ' Each model can be defined as an object with key as the model\'s ID '
                       ' (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and '
                       ' value as the model definition. Please refer the '
                       ' <a href="#models_pattern1"> Model </a> schema for reference.'
                       '</p>',
        'examples': [
            {
                'models': {
                    'model-1': '{ ** Model definition ** }',
                    'model-2': '{ ** Model definition ** }'
                }
            }
        ],
        'patternProperties': {
            r'^[A-Za-z]+[A-Za-z0-9_\-]': {**model_schema}
        },
        'additionalProperties': False
    }
