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
Datastore :: elasticsearch7
"""

from __future__ import annotations
import logging

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dore.model.model import Model
    from dore.protocol.batched_writer import BatchedWriter
    from dore.datastore.config.datastore_config import DatastoreConfig

from elasticsearch7 import Elasticsearch

from dore.datastore.datastore import Datastore
from dore.protocol.elasticsearch.elasticsearch7.elasticsearch7_model_exists import elasticsearch7_model_exists
from dore.protocol.elasticsearch.elasticsearch7.elasticsearch7_delete_model import elasticsearch7_delete_model
from dore.protocol.elasticsearch.elasticsearch7.elasticsearch7_create_model import elasticsearch7_create_model
from dore.protocol.elasticsearch.elasticsearch7.elasticsearch7_batched_writer import ElasticSearch7BatchedWriter
from dore.protocol.elasticsearch.config.elasticsearch_datastore_properties_config \
    import ElasticSearchDatastorePropertiesConfig
from dore.protocol.elasticsearch.elasticsearch7.elasticsearch7_all_records_for_model \
    import elasticsearch7_all_records_for_model

LOGGER = logging.getLogger(__name__)

class ElasticSearch7Datastore(Datastore):
    """
    ElasticSearch 7 Datastore
    """

    es_client: Elasticsearch = None

    def __init__(self, datastore_config: DatastoreConfig):
        super().__init__(datastore_config)
        self.__init_es_client__()

    def __init_es_client__(self):
        datastore_properties = self._config.properties(ElasticSearchDatastorePropertiesConfig)
        self.es_client = Elasticsearch(
            hosts=[f'http://{datastore_properties.host()}:{datastore_properties.port()}'],
            http_auth=(datastore_properties.user(), datastore_properties.password()),
        )

        es_logger = logging.getLogger('elasticsearch')
        es_logger.setLevel(logging.WARNING)

    def client(self) -> Elasticsearch:
        return self.es_client

    def create(self) -> None:
        """
        Does Nothing. There are no databases in elasticsearch.
        """

    def exists(self) -> bool:
        """
        Always returns True.
        There are no databases in ElasticSearch.

        :return: True
        """
        return True

    def create_model(self, model: Model) -> None:
        return elasticsearch7_create_model(self, model)

    def delete_model(self, model: Model) -> None:
        return elasticsearch7_delete_model(self, model)

    def model_exists(self, model: Model) -> bool:
        return elasticsearch7_model_exists(self, model)

    def all_records_for_model(self, model: Model) -> list[dict]:
        return elasticsearch7_all_records_for_model(self, model)

    def get_batched_writer(self, model: Model) -> BatchedWriter:
        return ElasticSearch7BatchedWriter(self, model)
