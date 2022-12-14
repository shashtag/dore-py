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
Model conflict exception
"""

class ModelConflictException(Exception):
    """
    Model conflict exception
    """

    def __init__(self, model_id: str, datastore_id: str):
        super().__init__(f'conflicting model [{model_id}] found in datastore [{datastore_id}]')
