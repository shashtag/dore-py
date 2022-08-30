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
Attribute Value schema
"""

from dore.attribute.value_generators.faker.config.faker_value_generator_schema \
    import faker_value_generator_schema
from dore.attribute.value_generators.ref.config.ref_value_generator_schema \
    import ref_value_generator_schema
from dore.attribute.value_generators.composite.config.composite_value_generator_schema \
    import composite_value_generator_schema
from dore.attribute.value_generators.selector.config.selector_value_generator_schema \
    import selector_value_generator_schema

attribute_value_schema = \
{
    'title': 'Value',
    'description': '<h4> Attribute value schema </h4>'
                   '<p>'
                   ' This config is used specify how Dore should generate value for a particular'
                   ' attribute.'
                   '</p>'
                   '<p>'
                   ' Dore uses the concept of an *Attribute Value Generator* to generate values for attributes.'
                   ' There are various attribute value generators that you can use to do things such as *use faker '
                   ' to generate a date between a given range*, or *select from a list of values'
                   ' based on certain selection criteria*, etc.'
                   '</p>'
                   '<p>'
                   ' Each section below illustrates one of the various attribute value generators supported'
                   ' by Dore and contains documentation on how to use a particular attribute value generator.'
                   '</p>',
    'type': 'object',
    'oneOf': [
        faker_value_generator_schema,
        selector_value_generator_schema,
        ref_value_generator_schema,
        composite_value_generator_schema,
    ]
}
