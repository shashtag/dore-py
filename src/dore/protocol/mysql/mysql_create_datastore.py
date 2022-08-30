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
Create Datastore :: mysql
"""

from __future__ import annotations
import logging

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dore.protocol.mysql.mysql_datastore import MySQLDatastore

from dore.protocol.mysql.config.mysql_datastore_properties_config import MySQLDatastorePropertiesConfig

LOGGER = logging.getLogger(__name__)

def mysql_create_datastore(datastore: MySQLDatastore) -> None:
    connection = datastore.connection()
    database_name = datastore.config().properties(MySQLDatastorePropertiesConfig).database()

    LOGGER.info('creating database [%s]', database_name)

    create_datastore_command = f'CREATE DATABASE `{database_name}`'
    cursor = connection.cursor()

    try:
        cursor.execute(create_datastore_command)
    except Exception as err:
        cursor.close()
        raise err

    cursor.close()
