# Dore Manifest schema

- [1. [Required] Property `Dore Manifest schema > id`](#id)
- [2. [Required] Property `Dore Manifest schema > datastores`](#datastores)
  - [2.1. [Optional] Pattern Property `Dore Manifest schema > datastores > Datastore`](#datastores_pattern1)
    - [2.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition`](#datastores_pattern1_oneOf_i0)
      - [2.1.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > protocol`](#datastores_pattern1_oneOf_i0_protocol)
      - [2.1.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties`](#datastores_pattern1_oneOf_i0_properties)
        - [2.1.1.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0)
          - [2.1.1.2.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > host`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_host)
          - [2.1.1.2.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > port`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_port)
          - [2.1.1.2.1.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > user`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_user)
          - [2.1.1.2.1.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > password`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_password)
          - [2.1.1.2.1.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > database`](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_database)
        - [2.1.1.2.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1)
          - [2.1.1.2.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > host`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_host)
          - [2.1.1.2.2.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > port`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_port)
          - [2.1.1.2.2.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > user`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_user)
          - [2.1.1.2.2.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > password`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_password)
          - [2.1.1.2.2.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > database`](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_database)
        - [2.1.1.2.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2)
          - [2.1.1.2.3.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > host`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_host)
          - [2.1.1.2.3.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > port`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_port)
          - [2.1.1.2.3.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > user`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_user)
          - [2.1.1.2.3.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > password`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_password)
          - [2.1.1.2.3.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > database`](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_database)
        - [2.1.1.2.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch`](#datastores_pattern1_oneOf_i0_properties_anyOf_i3)
          - [2.1.1.2.4.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > host`](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_host)
          - [2.1.1.2.4.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > port`](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_port)
          - [2.1.1.2.4.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > user`](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_user)
          - [2.1.1.2.4.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > password`](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_password)
    - [2.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Reference`](#datastores_pattern1_oneOf_i1)
      - [2.1.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Reference > ref`](#datastores_pattern1_oneOf_i1_ref)
- [3. [Required] Property `Dore Manifest schema > models`](#models)
  - [3.1. [Optional] Pattern Property `Dore Manifest schema > models > Model`](#models_pattern1)
    - [3.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition`](#models_pattern1_oneOf_i0)
      - [3.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > persistence`](#models_pattern1_oneOf_i0_persistence)
      - [3.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > records`](#models_pattern1_oneOf_i0_records)
      - [3.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > datastore`](#models_pattern1_oneOf_i0_datastore)
      - [3.1.1.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties`](#models_pattern1_oneOf_i0_properties)
        - [3.1.1.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MySQL`](#models_pattern1_oneOf_i0_properties_oneOf_i0)
          - [3.1.1.4.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MySQL > tableName`](#models_pattern1_oneOf_i0_properties_oneOf_i0_tableName)
        - [3.1.1.4.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL`](#models_pattern1_oneOf_i0_properties_oneOf_i1)
          - [3.1.1.4.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL > tableName`](#models_pattern1_oneOf_i0_properties_oneOf_i1_tableName)
          - [3.1.1.4.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL > schemaName`](#models_pattern1_oneOf_i0_properties_oneOf_i1_schemaName)
        - [3.1.1.4.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MongoDB`](#models_pattern1_oneOf_i0_properties_oneOf_i2)
          - [3.1.1.4.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MongoDB > collectionName`](#models_pattern1_oneOf_i0_properties_oneOf_i2_collectionName)
        - [3.1.1.4.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > Elasticsearch`](#models_pattern1_oneOf_i0_properties_oneOf_i3)
          - [3.1.1.4.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > Elasticsearch > indexName`](#models_pattern1_oneOf_i0_properties_oneOf_i3_indexName)
      - [3.1.1.5. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes`](#models_pattern1_oneOf_i0_attributes)
        - [3.1.1.5.1. Pattern Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute`](#models_pattern1_oneOf_i0_attributes_pattern1)
          - [3.1.1.5.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0)
            - [3.1.1.5.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value)
              - [3.1.1.5.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Faker`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0)
                - [3.1.1.5.1.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Faker > faker`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0_faker)
              - [3.1.1.5.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1)
                - [3.1.1.5.1.1.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector)
                  - [3.1.1.5.1.1.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0)
                    - [3.1.1.5.1.1.1.2.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random)
                      - [3.1.1.5.1.1.1.2.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items)
                        - [3.1.1.5.1.1.1.2.1.1.1.1.1. Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items](#autogenerated_heading_2)
                          - [3.1.1.5.1.1.1.2.1.1.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > String`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i0)
                          - [3.1.1.5.1.1.1.2.1.1.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > Number`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i1)
                          - [3.1.1.5.1.1.1.2.1.1.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > Object`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i2)
                  - [3.1.1.5.1.1.1.2.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1)
                    - [3.1.1.5.1.1.1.2.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin)
                      - [3.1.1.5.1.1.1.2.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items)
                        - [3.1.1.5.1.1.1.2.1.2.1.1.1. Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items](#autogenerated_heading_3)
                          - [3.1.1.5.1.1.1.2.1.2.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > String`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i0)
                          - [3.1.1.5.1.1.1.2.1.2.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > Number`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i1)
                          - [3.1.1.5.1.1.1.2.1.2.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > Object`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i2)
              - [3.1.1.5.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Ref`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2)
                - [3.1.1.5.1.1.1.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Ref > ref`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2_ref)
              - [3.1.1.5.1.1.1.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3)
                - [3.1.1.5.1.1.1.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite > composite`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite)
                  - [3.1.1.5.1.1.1.4.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite > composite > ref`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite_ref)
            - [3.1.1.5.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties)
              - [3.1.1.5.1.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0)
                - [3.1.1.5.1.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL > columnName`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnName)
                - [3.1.1.5.1.1.2.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL > columnType`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnType)
              - [3.1.1.5.1.1.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1)
                - [3.1.1.5.1.1.2.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL > columnName`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnName)
                - [3.1.1.5.1.1.2.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL > columnType`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnType)
              - [3.1.1.5.1.1.2.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MongoDB`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2)
                - [3.1.1.5.1.1.2.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MongoDB > fieldName`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2_fieldName)
              - [3.1.1.5.1.1.2.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3)
                - [3.1.1.5.1.1.2.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldName`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldName)
                - [3.1.1.5.1.1.2.4.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType)
                  - [3.1.1.5.1.1.2.4.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType > oneOf > Simple Data Types`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i0)
                  - [3.1.1.5.1.1.2.4.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType > oneOf > Complex Data Types`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i1)
          - [3.1.1.5.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Reference`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1)
            - [3.1.1.5.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Reference > ref`](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1_ref)
    - [3.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Reference`](#models_pattern1_oneOf_i1)
      - [3.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Reference > ref`](#models_pattern1_oneOf_i1_ref)

**Title:** Dore Manifest schema

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h3> Introduction </h3><p>  This page contains documentation about the structures and components that form the Dore manifest.</p><p> Before reading the schema and fields mentioned in this document, it might be helpful to remember  what Dore's core functionality is as this will help in understanding how the various components  and fields in the manifest come together in the big picture.</p><p> Fundamentally, Dore is a schema based fake data generation tool. </p><p> It supports data generation for various protocols (MySQL, MongoDB, Elasticsearch, etc)  with the ability to generate data which adheres to the referential integrity constraints and inter schema dependencies. The referential integrity is maintained irrespective of which protocol either of the models reside in are using.</p><h5> How it Works </h5><p> We start by creating the manifest which contains details about the schema based on which data is to be generated. The manifest contains details for `models` (which are analogous to tables in SQL), the attributes of models (which are analogous to columns of a SQL table), and `datastores` (which are analogous to databases in SQL).</p><p> Once the manifest is created, we invoke Dore with it.</p><p> Dore reads the manifest and proceeds to generate data for models by analyzing the model's attributes and their dependencies. It generates values for each attribute of a model  and the collection of values for a model's attributes forms a record for the model which is then  persisted in the datastore. This is done until Dore has generated the required number of records for each of the models.</p><h5> Manifest Schema Summary </h5><p> The high level structure of the manifest is as shown below. The list here is intentionally not  exhaustive as we want to take a look at the forest from the sky before we actually go into it in order to avoid getting lost. The exhaustive schema documentation can be referred to in the  later sections</p><p> A manifest has: <ol>   <li><p>`id`: a string identifier for the manifest. </p></li>   <li>    <p>`datastores`: a set of `datastore` configs. </p>    <p> Each `datastore` has: </p>    <ol>     <li><p>`protocol`: indicates which protocol the datastore uses (`MySQL`, `MongoDB`, etc).             </p></li>     <li><p>`properties`: protocol specific datastore properties and connection info. </p></li>    </ol>   </li>   <li>      <p>`models`: a set `model` configs.</p>      <p> Each `model` has: </p>      <ol>       <li><p>`datastore`: indicates which datastore the model belongs to.</p></li>       <li><p>`properties`: protocol specific model properties.</p></li>       <li><p>`attributes`: set of attributes and their configs for the model.</p>        <p>Each `attribute` has: </p>         <ol>          <li><p>`properties`: protocol specific attribute properties.</p></li>          <li><p>`value`: indicates how value for the attribute should be generated.</p></li>         </ol>       </li>      </ol>   </li> </ol></p><h3> Schema Documentation </h3><p> The sections below describe the manifest schema in detail. </p>

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description                                                                    |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------ |
| + [id](#id )                 | No      | string | No         | -          | <h4> Manifest ID </h4><p> Although Dore does not use the Manifest ID, it proves  ... |
| + [datastores](#datastores ) | No      | object | No         | -          | Datastore Container                                                                  |
| + [models](#models )         | No      | object | No         | -          | Model Container                                                                      |

## <a name="id"></a>1. [Required] Property `Dore Manifest schema > id`

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Manifest ID </h4><p> Although Dore does not use the Manifest ID, it proves helpful to have an ID as part of the manifest to understand what we are looking at without referencing the file name. The id has thus been kept as a `required` field.</p>

**Example:** 

```json
{
    "id": "tpch-manifest"
}
```

## <a name="datastores"></a>2. [Required] Property `Dore Manifest schema > datastores`

**Title:** Datastore Container

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Datastore Container </h4><p> All datastore definitions go here. </p><p> You can think of datastores as **MySQL databases**, a **MongoDB databases**,  an **Elasticsearch clusters**, etc. </p><p> Each datastore can be defined as an object with key as the datastore's ID (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and value as the datastore definition (view definition schema for reference) </p></p>

| Property                                            | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [^[A-Za-z]+[A-Za-z0-9_\-]](#datastores_pattern1 ) | Yes     | Combination | No         | -          | Datastore         |

**Example:** 

```json
{
    "datastores": {
        "a_datastore": {
            "ref": "/abs/path/to/a_datastore_definition.json"
        },
        "another_datastore": {
            "protocol": "elasticsearch",
            "properties": {
                "host": "127.0.0.1",
                "port": "9200",
                "user": "john_doe",
                "password": "yourpassword"
            }
        }
    }
}
```

### <a name="datastores_pattern1"></a>2.1. [Optional] Pattern Property `Dore Manifest schema > datastores > Datastore`
> All properties whose name matches the regular expression
```^[A-Za-z]+[A-Za-z0-9_\-]``` ([Test](https://regex101.com/?regex=%5E%5BA-Za-z%5D%2B%5BA-Za-z0-9_%5C-%5D))
must respect the following conditions

**Title:** Datastore

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Datastore </h4><p> You can think of a datastore as a *database in MySQL*, a *database in MongoDB*, an *Elasticsearch cluster*, and so on.</p><p> Each protocol has a different way of implementing the datastore abstraction. Please refer to the protocol specific documentation for datastores to see how a particular protocol uses datastores.</p><h5> In place vs Referenced definition </h5><p>A datastore can either be defined in place or in a separate file. <ul>  <li><p><b>In place</b><br>   If you are defining the datastore in place, use the `Datastore Definition` schema for   reference. </p></li>  <li><p><b>Separate file</b><br>  When the datastore is defined in a separate file, use the Datastore Reference schema instead to  provide a `ref`erence to the file which contains the datastore definition. </p></li> </ul></p>

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Datastore Definition](#datastores_pattern1_oneOf_i0) |
| [Datastore Reference](#datastores_pattern1_oneOf_i1)  |

#### <a name="datastores_pattern1_oneOf_i0"></a>2.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition`

**Title:** Datastore Definition

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Datastore Definition </h4><p> A standard datastore corresponds to a **MySQL database**, an **Elasticsearch cluster**,  a **MongoDB database**, etc.</p><p> In a datastore definition, we specify what the properties of the system (database, etc)  that Dore is trying to connect to are and details on how to connect to it.</p>

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description    |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | -------------------- |
| + [protocol](#datastores_pattern1_oneOf_i0_protocol )     | No      | enum (of string) | No         | -          | Protocol             |
| + [properties](#datastores_pattern1_oneOf_i0_properties ) | No      | Combination      | No         | -          | Datastore Properties |

**Example:** 

```json
{
    "protocol": "mysql",
    "properties": {
        "host": "127.0.0.1",
        "port": "3306",
        "user": "john_doe",
        "password": "yourpassword",
        "database": "foobar"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i0_protocol"></a>2.1.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > protocol`

**Title:** Protocol

| Type | `enum (of string)` |
| ---- | ------------------ |

**Description:** <h4> Protocol </h4><p> The protocol / type of system that the datastore represents.</p>

Must be one of:
* "mysql"
* "mongodb"
* "postgres"
* "elasticsearch7"
* "elasticsearch8"

**Examples:** 

```json
{
    "protocol": "mysql"
}
```

```json
{
    "protocol": "elasticsearch7"
}
```

##### <a name="datastores_pattern1_oneOf_i0_properties"></a>2.1.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties`

**Title:** Datastore Properties

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Datastore Properties </h4><p> This config is used to specify protocol specific datastore properties such as *which MySQL database to use*, *host name of the Elasticsearch cluster*, *what are the credentials for accessing the database*, etc.</p><p> Since each protocol has different requirements for configuring / connecting to the underlying system, this config varies from one protocol to the other.  Please refer to the protocol specific sections below to view which fields are  required for a particular protocol.</p>

| Any of(Option)                                                     |
| ------------------------------------------------------------------ |
| [MySQL](#datastores_pattern1_oneOf_i0_properties_anyOf_i0)         |
| [PostgreSQL](#datastores_pattern1_oneOf_i0_properties_anyOf_i1)    |
| [MongoDB](#datastores_pattern1_oneOf_i0_properties_anyOf_i2)       |
| [Elasticsearch](#datastores_pattern1_oneOf_i0_properties_anyOf_i3) |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0"></a>2.1.1.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL`

**Title:** MySQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> MySQL datastore properties </h4><p> A datastore corresponds to a **MySQL database**.</p><p> Use this when `datastore.protocol` is `mysql`.</p>

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [host](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_host )         | No      | string | No         | -          | Host              |
| + [port](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_port )         | No      | string | No         | -          | Port              |
| + [user](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_user )         | No      | string | No         | -          | User              |
| + [password](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_password ) | No      | string | No         | -          | Password          |
| + [database](#datastores_pattern1_oneOf_i0_properties_anyOf_i0_database ) | No      | string | No         | -          | Database name     |

**Example:** 

```json
{
    "properties": {
        "host": "127.0.0.1",
        "port": "3306",
        "user": "john_doe",
        "password": "yourpassword",
        "database": "foobar"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0_host"></a>2.1.1.2.1.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > host`

**Title:** Host

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0_port"></a>2.1.1.2.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > port`

**Title:** Port

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0_user"></a>2.1.1.2.1.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > user`

**Title:** User

| Type | `string` |
| ---- | -------- |

**Description:** MySQL `username` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0_password"></a>2.1.1.2.1.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > password`

**Title:** Password

| Type | `string` |
| ---- | -------- |

**Description:** MySQL `password` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i0_database"></a>2.1.1.2.1.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MySQL > database`

**Title:** Database name

| Type | `string` |
| ---- | -------- |

**Description:** Name of the MySQL database to connect to

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1"></a>2.1.1.2.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL`

**Title:** PostgreSQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> PostgreSQL datastore properties </h4><p> A datastore corresponds to a **PostgreSQL database**.</p><p> Use this when `datastore.protocol` is `postgres`.</p>

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [host](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_host )         | No      | string | No         | -          | Host              |
| + [port](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_port )         | No      | string | No         | -          | Port              |
| + [user](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_user )         | No      | string | No         | -          | User              |
| + [password](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_password ) | No      | string | No         | -          | Password          |
| + [database](#datastores_pattern1_oneOf_i0_properties_anyOf_i1_database ) | No      | string | No         | -          | Database name     |

**Example:** 

```json
{
    "properties": {
        "host": "127.0.0.1",
        "port": "5432",
        "user": "john_doe",
        "password": "yourpassword",
        "database": "foobar"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1_host"></a>2.1.1.2.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > host`

**Title:** Host

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1_port"></a>2.1.1.2.2.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > port`

**Title:** Port

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1_user"></a>2.1.1.2.2.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > user`

**Title:** User

| Type | `string` |
| ---- | -------- |

**Description:** PostgreSQL `username` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1_password"></a>2.1.1.2.2.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > password`

**Title:** Password

| Type | `string` |
| ---- | -------- |

**Description:** PostgreSQL `password` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i1_database"></a>2.1.1.2.2.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > PostgreSQL > database`

**Title:** Database name

| Type | `string` |
| ---- | -------- |

**Description:** Name of the PostgreSQL database to connect to.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2"></a>2.1.1.2.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB`

**Title:** MongoDB

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> MongoDB datastore properties schema </h4><p> A datastore corresponds to a **MongoDB database**.</p><p> Use this when `datastore.protocol` is `mongodb`.</p>

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [host](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_host )         | No      | string | No         | -          | Host              |
| + [port](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_port )         | No      | string | No         | -          | Port              |
| + [user](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_user )         | No      | string | No         | -          | User              |
| + [password](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_password ) | No      | string | No         | -          | Password          |
| + [database](#datastores_pattern1_oneOf_i0_properties_anyOf_i2_database ) | No      | string | No         | -          | Database name     |

**Example:** 

```json
{
    "properties": {
        "host": "127.0.0.1",
        "port": "27017",
        "user": "john_doe",
        "password": "yourpassword",
        "database": "foobar"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2_host"></a>2.1.1.2.3.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > host`

**Title:** Host

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2_port"></a>2.1.1.2.3.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > port`

**Title:** Port

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2_user"></a>2.1.1.2.3.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > user`

**Title:** User

| Type | `string` |
| ---- | -------- |

**Description:** MongoDB `username` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2_password"></a>2.1.1.2.3.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > password`

**Title:** Password

| Type | `string` |
| ---- | -------- |

**Description:** MongoDB `password` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i2_database"></a>2.1.1.2.3.5. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > MongoDB > database`

**Title:** Database name

| Type | `string` |
| ---- | -------- |

**Description:** Name of the MongoDB database to connect to

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i3"></a>2.1.1.2.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch`

**Title:** Elasticsearch

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Elasticsearch datastore properties </h4><p> A datastore corresponds to an **Elasticsearch cluster**.</p><p> Use this when `datastore.protocol` is either one of `elasticsearch7` or `elasticsearch8`.</p>

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [host](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_host )         | No      | string | No         | -          | Host              |
| + [port](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_port )         | No      | string | No         | -          | Port              |
| + [user](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_user )         | No      | string | No         | -          | User              |
| + [password](#datastores_pattern1_oneOf_i0_properties_anyOf_i3_password ) | No      | string | No         | -          | Password          |

**Example:** 

```json
{
    "properties": {
        "host": "127.0.0.1",
        "port": "9200",
        "user": "john_doe",
        "password": "yourpassword"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i3_host"></a>2.1.1.2.4.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > host`

**Title:** Host

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i3_port"></a>2.1.1.2.4.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > port`

**Title:** Port

| Type | `string` |
| ---- | -------- |

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i3_user"></a>2.1.1.2.4.3. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > user`

**Title:** User

| Type | `string` |
| ---- | -------- |

**Description:** Elasticsearch `username` for connecting to the database.

##### <a name="datastores_pattern1_oneOf_i0_properties_anyOf_i3_password"></a>2.1.1.2.4.4. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Definition > properties > anyOf > Elasticsearch > password`

**Title:** Password

| Type | `string` |
| ---- | -------- |

**Description:** Elasticsearch `password` for connecting to the database.

#### <a name="datastores_pattern1_oneOf_i1"></a>2.1.2. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Reference`

**Title:** Datastore Reference

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Datastore Reference </h4><p> A datastore can be defined in a file separate from the manifest file.</p><p> You would generally want to define each datastore in a separate file. It is recommended to spread different parts of the manifest such as models and datastores across  different files in order to keep each config small and readable.</p> Use this schema when the datastore is defined in a separate file and you need to provide a  reference to that file in the manifest.</p> <p> Use the `ref` field in the manifest and provide absolute path to the file that actually contains the <a href="#tab-pane_datastores_pattern1_oneOf_i0"> datastore definition </a>.</p> In the example, the definition for `datastore_1` is present in a separate file and the `ref`erence to that file is added in the manifest.</p>

| Property                                    | Pattern | Type   | Deprecated | Definition | Title/Description                                            |
| ------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------ |
| + [ref](#datastores_pattern1_oneOf_i1_ref ) | No      | string | No         | -          | Absolute path to file that contains the datastore definition |

**Example:** 

```json
{
    "datastore_1": {
        "ref": "/abs/path/to/file.json"
    }
}
```

##### <a name="datastores_pattern1_oneOf_i1_ref"></a>2.1.2.1. Property `Dore Manifest schema > datastores > Datastore > oneOf > Datastore Reference > ref`

| Type | `string` |
| ---- | -------- |

**Description:** Absolute path to file that contains the datastore definition

**Example:** 

```json
"/abs/path/to/file.json"
```

## <a name="models"></a>3. [Required] Property `Dore Manifest schema > models`

**Title:** Model Container

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Model Container </h4><p>  All model definitions go here. </p><p>  You can think of a model as a MySQL table, an Elasticsearch index,  a collection in MongoDB, etc. </p><p> Each model can be defined as an object with key as the model's ID  (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and  value as the model definition. Please refer the  <a href="#models_pattern1"> Model </a> schema for reference.</p>

| Property                                        | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [^[A-Za-z]+[A-Za-z0-9_\-]](#models_pattern1 ) | Yes     | Combination | No         | -          | Model             |

**Example:** 

```json
{
    "models": {
        "model-1": "{ ** Model definition ** }",
        "model-2": "{ ** Model definition ** }"
    }
}
```

### <a name="models_pattern1"></a>3.1. [Optional] Pattern Property `Dore Manifest schema > models > Model`
> All properties whose name matches the regular expression
```^[A-Za-z]+[A-Za-z0-9_\-]``` ([Test](https://regex101.com/?regex=%5E%5BA-Za-z%5D%2B%5BA-Za-z0-9_%5C-%5D))
must respect the following conditions

**Title:** Model

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Model </h4><p> You can think of a model as *table* in MySQL, an *index* in Elasticsearch, a *collection* in MongoDB, and so on.</p><p> Each protocol has a different way of implementing the model abstraction. Please  refer to the protocol specific documentation for models to see how a particular protocol  uses the model abstraction.</p><h5> In place vs Referenced definition </h5><p> A model can either be defined in place or in a separate file. </p><ul> <li>  <p>    <b>In place</b>     <br>    If you are defining the model in place, use the    <a href="#tab-pane_models_pattern1_oneOf_i0"> Model Definition </a> schema for reference.   </p> </li> <li>  <p>   <b>Separate file</b>   <br>   When the model is defined in a separate file, use the    <a href="#tab-pane_models_pattern1_oneOf_i1"> Model Reference </a>   schema instead to provide a `ref`erence to the file which contains the model definition.  </p> </li></ul>

| One of(Option)                                |
| --------------------------------------------- |
| [Model Definition](#models_pattern1_oneOf_i0) |
| [Model Reference](#models_pattern1_oneOf_i1)  |

#### <a name="models_pattern1_oneOf_i0"></a>3.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition`

**Title:** Model Definition

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Model Definition </h4>A standard model corresponds to a table in SQL database, an index in Elasticsearch, a collection in MongoDB, etc. <br>

| Property                                                | Pattern | Type             | Deprecated | Definition | Title/Description   |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------- |
| - [persistence](#models_pattern1_oneOf_i0_persistence ) | No      | enum (of string) | No         | -          | Persistence Level   |
| - [records](#models_pattern1_oneOf_i0_records )         | No      | integer          | No         | -          | Records Count       |
| - [datastore](#models_pattern1_oneOf_i0_datastore )     | No      | string           | No         | -          | Datastore Reference |
| - [properties](#models_pattern1_oneOf_i0_properties )   | No      | Combination      | No         | -          | Model Properties    |
| + [attributes](#models_pattern1_oneOf_i0_attributes )   | No      | object           | No         | -          | Attribute Container |

**Example:** 

```json
{
    "model-1": {
        "persistence": "FULL",
        "records": 100,
        "datastore": "datastoreId",
        "properties": "{ ** Protocol specific model properties ** }",
        "attributes": "{ ** Attributes Definition ** }"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_persistence"></a>3.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > persistence`

**Title:** Persistence Level

| Type        | `enum (of string)` |
| ----------- | ------------------ |
| **Default** | `"FULL"`           |

**Description:** <h4> Persistence Level </h4><p> Dore allows you to specify various persistence levels for models </p><p>  This is particularly useful when you have nested attributes that need to be represented as a separate model in itself. In such scenarios, you would often want to only generate records for that model and not persist  it in the underlying database.</p><p> Consider the case of a `customer` model which has a `shippingAddress` attribute.  We would want to generate addresses for the customer and use those records  as values for the `shippingAddress` attribute. Since addresses are complex structures with multiple components, we would perhaps represent it as a separate model in the manifest so Dore can generate records  for it.</p><p> But, we wouldn't want to persist the `address` model itself in the datastore.  This would be the equivalent of having an `address` table with all addresses as  rows in the table. We just want to use the model so that its records can be used  for values in other attributes.</p><h5> Persistence Levels </h5><p> The Persistence levels supported by Dore along with its implications are given below: <ul>  <li><p> `FULL`: When this persistence level is used on a model, Dore creates a model for this in the underlying datastore and persists records generated for this model in the datastore. </p></li>  <li><p> `MEMORY_ONLY`: When this persistence level is used on a model, Dore persists the records generated for the model in the *cache  only* and does not create the model or persist records for the model in any datastore. </p></li>  <li><p> `NO_PERSIST`: When this persistence level is used on a model, Dore does NOT persist the model or the records generated for it in cache nor in any datastore. Each record is generated on the fly and discarded after being used.  </p></li> </ul></p>

Must be one of:
* "FULL"
* "MEMORY_ONLY"
* "NO_PERSIST"

**Example:** 

```json
{
    "persistence": "MEMORY_ONLY"
}
```

##### <a name="models_pattern1_oneOf_i0_records"></a>3.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > records`

**Title:** Records Count

| Type | `integer` |
| ---- | --------- |

**Description:** <h4> Records Count </h4><p>  We can use this field to specify the number of records to be generated for the  model.</p><p> *Note:* The actual number of records that Dore generates will depend on the value  provided here as well as the `scale_factor` provided during invocation.</p><p> For example, if a model has `records` as `10000`, and we provide a `scale_factor`  value of `0.1` when invoking Dore, the actual number of records generated by Dore will be `10000 * 0.1 = 1000`.</p>

**Example:** 

```json
{
    "records": 10000
}
```

##### <a name="models_pattern1_oneOf_i0_datastore"></a>3.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > datastore`

**Title:** Datastore Reference

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Datastore Reference </h4>ID of the datastore to which this model belongs. This is a required field in cases of models that have `FULL` persistence levels.

**Example:** 

```json
{
    "datastore": "datastoreId"
}
```

##### <a name="models_pattern1_oneOf_i0_properties"></a>3.1.1.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties`

**Title:** Model Properties

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Model Properties </h4><p> This config is used to specify protocol specific model properties such as table properties in SQL, index properties in Elasticsearch, collection properties in MongoDB, etc.</p><p> As protocol specific properties of a model are required only when there is a need to persist the model and it's records in any datastore, the `properties` field is a **required** field only when `persistence` on a model is set to `"FULL"` or is not explicitly mentioned in the manifest as the Dore assumes the default `persistence` as `"FULL"` if not specified.</p><p>  Since each protocol has different requirements for configuring  a model, this config varies from one protocol to the other.   Please refer to the protocol specific sections below to view which fields  are required for a particular protocol.</p>

| One of(Option)                                                 |
| -------------------------------------------------------------- |
| [MySQL](#models_pattern1_oneOf_i0_properties_oneOf_i0)         |
| [PostgreSQL](#models_pattern1_oneOf_i0_properties_oneOf_i1)    |
| [MongoDB](#models_pattern1_oneOf_i0_properties_oneOf_i2)       |
| [Elasticsearch](#models_pattern1_oneOf_i0_properties_oneOf_i3) |

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i0"></a>3.1.1.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MySQL`

**Title:** MySQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> MySQL model properties </h4><p>  A model corresponds to a table in a MySQL database.</p><p> Use this schema when the `datastore` id on the model refers to a datastore that uses the `mysql` protocol.</p>

| Property                                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [tableName](#models_pattern1_oneOf_i0_properties_oneOf_i0_tableName ) | No      | string | No         | -          | Table Name        |

**Example:** 

```json
{
    "properties": {
        "tableName": "some_table"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i0_tableName"></a>3.1.1.4.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MySQL > tableName`

**Title:** Table Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Table Name </h4><p> Name of the MySQL table that the model corresponds to. </p><p> While creating tables in MySQL for MySQL bound models in the manifest,  Dore infers the required columns and their data types from attribute  config for the model.</p>

**Examples:** 

```json
"some_table"
```

```json
"some_other_table"
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i1"></a>3.1.1.4.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL`

**Title:** PostgreSQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>PostgreSQL model properties</h4><p>  A model corresponds to a table in a PostgreSQL database.</p><p> Use this schema when the `datastore` id on the model refers to a datastore that uses the `postgres` protocol.</p>

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description      |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ---------------------- |
| + [tableName](#models_pattern1_oneOf_i0_properties_oneOf_i1_tableName )   | No      | string | No         | -          | Table Name             |
| + [schemaName](#models_pattern1_oneOf_i0_properties_oneOf_i1_schemaName ) | No      | string | No         | -          | PostgreSQL schema name |

**Example:** 

```json
{
    "properties": {
        "tableName": "some_table",
        "schemaName": "some_schema"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i1_tableName"></a>3.1.1.4.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL > tableName`

**Title:** Table Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Table Name </h4><p> Name of the PostgreSQL table that the model corresponds to. </p><p> While creating tables in PostgreSQL based on PostgreSQL bound models in the manifest, Dore infers the required columns and their data types from attribute config for the model. </p>

**Examples:** 

```json
"some_table"
```

```json
"some_other_table"
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i1_schemaName"></a>3.1.1.4.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > PostgreSQL > schemaName`

**Title:** PostgreSQL schema name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> PostgreSQL schema name </h4><p> Name of the PostgreSQL schema for the table that the model corresponds to. </p>

**Examples:** 

```json
"schema_name"
```

```json
"some_other_schema_name"
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i2"></a>3.1.1.4.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MongoDB`

**Title:** MongoDB

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>MongoDB model properties</h4><p>  A model corresponds to a <a href="https://www.mongodb.com/docs/manual/core/databases-and-collections/#collections"collection target="_blank"> collection </a> in a MongoDB database</p><p> Use this schema when the `datastore` id on the model refers to a datastore that uses the `mongodb` protocol.</p>

| Property                                                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [collectionName](#models_pattern1_oneOf_i0_properties_oneOf_i2_collectionName ) | No      | string | No         | -          | Collection Name   |

**Example:** 

```json
{
    "properties": {
        "collectionName": "some_collection"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i2_collectionName"></a>3.1.1.4.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > MongoDB > collectionName`

**Title:** Collection Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Collection Name </h4><p> Name of the MongoDB collection that the model corresponds to.<p><p> While creating collections in MongoDB for MongoDB bound models in the manifest, Dore infers the field names from attribute config for the model. </p>

**Examples:** 

```json
"some_collection"
```

```json
"some_other_collection"
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i3"></a>3.1.1.4.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > Elasticsearch`

**Title:** Elasticsearch

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>Elasticsearch model properties</h4><p>  A model corresponds to an index in elasticsearch.</p><p> Use this schema when the `datastore` id on the model refers to a datastore that uses the `elasticsearch7` or `elasticsearch8` protocol.</p>

| Property                                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [indexName](#models_pattern1_oneOf_i0_properties_oneOf_i3_indexName ) | No      | string | No         | -          | Index Name        |

**Example:** 

```json
{
    "properties": {
        "indexName": "index_name"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_properties_oneOf_i3_indexName"></a>3.1.1.4.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > properties > oneOf > Elasticsearch > indexName`

**Title:** Index Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Index Name </h4><p> Name of the Elasticsearch Index that the model corresponds to. </p><p> While creating indices in Elasticsearch based on Elasticsearch bound models in the manifest, Dore infers the fields and their data types from attribute config for the model.</p>

**Examples:** 

```json
"index_name"
```

```json
"other_name"
```

##### <a name="models_pattern1_oneOf_i0_attributes"></a>3.1.1.5. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes`

**Title:** Attribute Container

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Attribute Container </h4><p>  All attribute definitions for a model go here. </p><p> Each model will generally have a set of attributes associated with it.  You can think of an attribute as a *column* of a MySQL table (where the model  corresponds to the table), a *field* of an Elasticsearch index (where the model corresponds  to the index), a *field* of a MongoDB collection (where the model corresponds to the MongoDB  collection), and so on. </p><p> Please refer to the protocol specific attribute documentation for more information on how  a particular protocol implements the **attribute** abstraction.</p><p> Each attribute can be defined as an object with key as the attribute's ID  (accepted strings for ID are illustrated by the `Pattern Property` regex shown below) and  value as the attribute's definition. Please refer the **Attribute** definition schema for reference</p>

| Property                                                                     | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [^[A-Za-z]+[A-Za-z0-9_\-]](#models_pattern1_oneOf_i0_attributes_pattern1 ) | Yes     | Combination | No         | -          | Attribute         |

**Example:** 

```json
{
    "model-1": {
        "attributes": {
            "attribute-1": "{ ** Attribute definition ** }",
            "attribute-2": "{ ** Attribute definition ** }"
        }
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1"></a>3.1.1.5.1. Pattern Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute`
> All properties whose name matches the regular expression
```^[A-Za-z]+[A-Za-z0-9_\-]``` ([Test](https://regex101.com/?regex=%5E%5BA-Za-z%5D%2B%5BA-Za-z0-9_%5C-%5D))
must respect the following conditions

**Title:** Attribute

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4>Attribute</h4><p> Generally, models have attributes associated with them. You can think of an attribute as a *column* of a MySQL table (where the model corresponds to the table), a *field* of an Elasticsearch index (where the model corresponds to the index), a *field* of a MongoDB collection (where the model corresponds to the MongoDB collection), and so on. </p><p> An attribute can either be defined in place or in a separate file <p><ul>  <li>    <p><b>In place:</b> If you are defining the attribute in place, use the Attribute Definition    schema for reference </p>  </li>  <li>    <p><b>Separate file:</b> When the attribute is defined in a separate file, use the Attribute       Reference schema instead to provide a `ref`erence to the file which contains the attribute        definition.</p>  </li></ul>

| One of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [Attribute Definition](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0) |
| [Attribute Reference](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1)  |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0"></a>3.1.1.5.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition`

**Title:** Attribute Definition

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Attribute Definition </h4><p>  You can think of an attribute as a *column* of a MySQL table (where the model  corresponds to the table), a *field* of an Elasticsearch index (where the model  corresponds to the index), a *field* of a MongoDB collection (where the model corresponds  to the MongoDB collection), and so on. </p><p>  On a high level, we need to provide two types of information about an attribute to Dore in order for Dore to generate data:  <ul>  <li><p>    The second type of information we need to provide is *How should values for the   attribute be generated*?<br>    We use the `value` field of the attribute definition to specify   this information.  </p></li>  <li><p>    The first is *How should/is the attribute represented in the underlying datastore*?<br>   We use the `properties` field of the attribute definition to specify this information.  </p></li> </ul>

| Property                                                                           | Pattern | Type        | Deprecated | Definition | Title/Description    |
| ---------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | -------------------- |
| + [value](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value )           | No      | Combination | No         | -          | Value                |
| + [properties](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties ) | No      | Combination | No         | -          | Attribute Properties |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value"></a>3.1.1.5.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value`

**Title:** Value

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Attribute value schema </h4><p> This config is used specify how Dore should generate value for a particular attribute.</p><p> Dore uses the concept of an *Attribute Value Generator* to generate values for attributes. There are various attribute value generators that you can use to do things such as *use faker  to generate a date between a given range*, or *select from a list of values based on certain selection criteria*, etc.</p><p> Each section below illustrates one of the various attribute value generators supported by Dore and contains documentation on how to use a particular attribute value generator.</p>

| One of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [Faker](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0)     |
| [Selector](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1)  |
| [Ref](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2)       |
| [Composite](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0"></a>3.1.1.5.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Faker`

**Title:** Faker

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Faker based attribute value generator </h4><p> With Dore, you can leverage the capabilities that  <a href="https://faker.readthedocs.io/en/master/" target="_blank"> Python's Faker library </a> provides in order to generate values for attributes.</p><p> Python's faker library uses the concept of  <a href="https://faker.readthedocs.io/en/master/providers/baseprovider.html" target="_blank"> `providers` </a> which **provide** methods to the faker instance. These methods, when invoked, generate a value. For example, the <a href="https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html?highlight=uuid#faker.providers.misc.Provider" target="_blank"> `misc` provider </a> provides a method <a href="https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html?highlight=uuid#faker.providers.misc.Provider" target="_blank"> `uuid4`  </a>  that allows you to generate UUID4 strings. In a Python program, You can invoke this method  by calling `fake.uuid4()` to get a randomly generated UUID4 string.</p><p> In Dore manifest, Faker based attribute value configs follow a general structure which is  depicted in the first example in the `Examples` below. Parameters required for a faker  method can be provided by passing an object which contains the parameters as keys and the  parameter values as values. Ex: `{ "param_1": "val2", "param_2": "val2" }`. For specifying a  faker method should be invoked without any parameters, pass an empty object `{}`.</p>

| Property                                                                                | Pattern | Type   | Deprecated | Definition | Title/Description                                                                    |
| --------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------ |
| + [faker](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0_faker ) | No      | object | No         | -          | <p> All faker based configs should be present within the 'faker' root object in  ... |

**Examples:** 

```json
{
    "value": {
        "faker": {
            "faker_method_name": {
                "a_param": "val",
                "another_param": "val"
            }
        }
    }
}
```

```json
{
    "value": {
        "faker": {
            "pyint": {
                "min_value": 1,
                "max_value": 3
            }
        }
    }
}
```

```json
{
    "value": {
        "faker": {
            "uuid4": {}
        }
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i0_faker"></a>3.1.1.5.1.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Faker > faker`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <p> All faker based configs should be present within the `faker` root object in the  attribute `value` config.</p><p> This object will contain an object with key as the required Faker method's name and  value as parameters that we want to invoke the method with.</p>

**Examples:** 

```json
{
    "faker": {
        "pyint": {
            "min_value": 1,
            "max_value": 3
        }
    }
}
```

```json
{
    "faker": {
        "uuid": {}
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1"></a>3.1.1.5.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector`

**Title:** Selector

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Selector based attribute value generator </h4><p> Dore allows you to define a list of values from which a value is selected for an attribute during record generation.</p><p> Consider an example where you have an attribute representing the size of a T-shirt and you wanted  the value of this attribute to be one of the following values: `"S"`, `"L"` or `"XL"` picked at  random for each record. You can use the *Random Selector* for this. If, for example, you wanted  the T-shirt size value to be picked from the list above in a round robin fashion for each record,  you can use the *Round Robin Selector*</p><p> Each section in the `selector` field below illustrates one of the various selector based value  generators supported by Dore and contains documentation on how to use a particular selector.</p>

| Property                                                                                      | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [selector](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector ) | No      | Combination | No         | -          | -                 |

**Examples:** 

```json
{
    "selector": {
        "random": {
            "items": [
                "ML",
                "XL",
                "XXL"
            ]
        }
    }
}
```

```json
{
    "selector": {
        "roundRobin": {
            "items": [
                "M",
                "L",
                "XL",
                "XXL"
            ]
        }
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector"></a>3.1.1.5.1.1.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector`

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| One of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [Random Selector](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0)      |
| [Round Robin Selector](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0"></a>3.1.1.5.1.1.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector`

**Title:** Random Selector

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Random Selector </h4><p>  Selects values at random for an attribute from the list of values provided.</p><p>  Each value in the list is usually equally likely to be picked. </p></p>

| Property                                                                                                    | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [random](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random ) | No      | object | No         | -          | Random Selector   |

**Example:** 

```json
{
    "random": {
        "items": [
            "item 1",
            "item 2",
            "item 3"
        ]
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random"></a>3.1.1.5.1.1.1.2.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random`

**Title:** Random Selector

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Random Selector root object </h4><p> Use this object within the `selector` object to indicate that we want to use the random selector.</p>

| Property                                                                                                         | Pattern | Type  | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| + [items](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items ) | No      | array | No         | -          | Items             |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items"></a>3.1.1.5.1.1.1.2.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items`

**Title:** Items

| Type | `array` |
| ---- | ------- |

**Description:** <h4> Item List </h4><p> List of items to select from. </p><p> Any item can be a number, a string, or an arbitrarily complex JSON object. </p>

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                                           | Description |
| ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [items items](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items) | -           |

##### <a name="autogenerated_heading_2"></a>3.1.1.5.1.1.1.2.1.1.1.1.1. Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| One of(Option)                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- |
| [String](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i0) |
| [Number](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i1) |
| [Object](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i2) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i0"></a>3.1.1.5.1.1.1.2.1.1.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > String`

**Title:** String

| Type | `string` |
| ---- | -------- |

**Description:** An item can be a simple string.

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i1"></a>3.1.1.5.1.1.1.2.1.1.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > Number`

**Title:** Number

| Type | `number` |
| ---- | -------- |

**Description:** An item can be a number.

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i0_random_items_items_oneOf_i2"></a>3.1.1.5.1.1.1.2.1.1.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Random Selector > random > items > items items > oneOf > Object`

**Title:** Object

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** An item can be arbitrarily complex JSON object

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1"></a>3.1.1.5.1.1.1.2.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector`

**Title:** Round Robin Selector

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Round Robin Selector </h4><p> Selects a value in a round robin manner from the list of values provided.</p>

| Property                                                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description    |
| ------------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------- |
| + [roundRobin](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin ) | No      | object | No         | -          | Round Robin Selector |

**Example:** 

```json
{
    "roundRobin": {
        "items": [
            "item_1",
            "item_2",
            "item_3"
        ]
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin"></a>3.1.1.5.1.1.1.2.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin`

**Title:** Round Robin Selector

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Round Robin Selector root object </h4><p> Use this object within the `selector` object in the manifest to indicate that we want to  use the random selector.</p>

| Property                                                                                                             | Pattern | Type  | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| + [items](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items ) | No      | array | No         | -          | Items             |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items"></a>3.1.1.5.1.1.1.2.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items`

**Title:** Items

| Type | `array` |
| ---- | ------- |

**Description:** <h4> Item List </h4><p> List of items to select from. </p><p> An item can be a number, a string, or an arbitrarily complex JSON object. </p>

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                                               | Description |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [items items](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items) | -           |

##### <a name="autogenerated_heading_3"></a>3.1.1.5.1.1.1.2.1.2.1.1.1. Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| One of(Option)                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------- |
| [String](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i0) |
| [Number](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i1) |
| [Object](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i2) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i0"></a>3.1.1.5.1.1.1.2.1.2.1.1.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > String`

**Title:** String

| Type | `string` |
| ---- | -------- |

**Description:** An item can be a simple string.

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i1"></a>3.1.1.5.1.1.1.2.1.2.1.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > Number`

**Title:** Number

| Type | `number` |
| ---- | -------- |

**Description:** An item can be a number.

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i1_selector_oneOf_i1_roundRobin_items_items_oneOf_i2"></a>3.1.1.5.1.1.1.2.1.2.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Selector > selector > oneOf > Round Robin Selector > roundRobin > items > items items > oneOf > Object`

**Title:** Object

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** An item can be arbitrarily complex JSON object

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2"></a>3.1.1.5.1.1.1.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Ref`

**Title:** Ref

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Ref attribute value generator </h4><p>  Often times, we would want the value of an attribute to be based on the value of an attribute of  a different model.<p> A typical scenario where we might want do this is while generating data in a relational database with Foreign Key dependencies.</p><p> Consider an example of a schema where you are recording invoices generated by a business. An invoice generally has a customer associated with it.</p><p><p> On attempting to represent this scenario in a database schema, You would have a `customer` model  which would have some of the following attributes: <ul>  <li>    <p> `customerId`: a unique ID for the customer. </p>    <p>  This is a primary key for the customer model. </p>  </li>  <li> `name`: Customer's name.  <li> `address`: The customer's address. </ul></p> And you would have an `invoice` model which would have some of the following attributes: <ul>  <li> `invoiceId`: a unique ID for the invoice. </li>  <li> `date`: Date when the invoice was created. </li>  <li>    <p>`customerId`: ID of the customer to whom the invoice is addressed. </p>    <p> This is a foreign key which references the `customerId` of the customer model  </li> </ul></p><p> When we want to generate data for this schema with Dore, we can specify the value config  for `customerId` in the `invoice` model as a `ref` value and provide a reference to the  dependent attribute and model, which is the `customerId` attribute of the `customer` model in this case. Please refer the examples below on how to specify these references.</p><p> When we do this, Dore uses the `customer` model's `customerId` values as values for the  `customerId` attribute for the `invoice` model.</p><p> Before Dore starts generating records for any model, it analyzes the attribute and model  dependencies and creates an iteration order over the models based on topological sorting of their dependencies. By doing this, Dore ensures that records for a model which has other models dependent on it are generated before generating records for the dependent models.</p>

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description   |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------- |
| + [ref](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2_ref ) | No      | string | No         | -          | Attribute Reference |

**Examples:** 

```json
{
    "ref": "modelId.attributeId"
}
```

```json
{
    "ref": "customer.customerId"
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i2_ref"></a>3.1.1.5.1.1.1.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Ref > ref`

**Title:** Attribute Reference

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Attribute Reference </h4><p> Attribute references here take have the following syntax: `modelId.attributeId`. </p>

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3"></a>3.1.1.5.1.1.1.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite`

**Title:** Composite

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Composite attribute value generator </h4><p> The composite attribute value generator is similar to the `ref` attribute value generator in  the sense that you can have attributes of a model be dependent on other models. But, it is different in one major way: While you would use the  `ref` attribute value generator when you want values of an attribute of a particular model  be dependent on the values of another attribute of a different model, the `composite` attribute  value generator lets you assign the value of an attribute to be an *entire record* of the dependent model.</p><p> When an attribute uses a `composite` value generator, an entire record of the  dependent model would be used as the value for the attribute. In other words, the attribute will have an *object* as a value and the value is a record of the dependent model.</p><p> This is particularly useful in cases of NoSQL databases where we can have attributes that can be arbitrarily complex objects.</p><p> Consider an example where you have a `customer` model with the following attributes: <ul>  <li><p> `customerId`: unique ID for the customer. </p></li>  <li><p> `billingAddress`: Billing address for the customer. </p></li>  <li><p> `shippingAddress`: Shipping address for the customer. </ul></p> Addresses are generally complex in structure with many sub components. We can represent address as a separate model in the manifest, let Dore generate records for it, and use the generated records in their entirety as values for the `billingAddress` or `shippingAddress`.</p><p> We can create an `address` model with the following attributes: <ul>  <li><p>`house_number`</p></li>  <li><p>`residence_name`: The apartment / building / society name. </p></li>  <li><p>`street`: name of the street </p></li>  <li><p>`state`  <li><p>`country`</li></p>  <li><p>`pin_code`</li></p> </ul></p><p> And specify that the `billingAddress`/`shippingAddress` attribute of the `customer` model has a  `value` config of `composite` type and provide a reference to the address model's ID to it  (This is illustrated in the second example below).</p><p> The general structure of the `value` config for a `composite` attribute value generator is illustrated in the first example.</p>

| Property                                                                                        | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [composite](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite ) | No      | object | No         | -          | -                 |

**Examples:** 

```json
{
    "composite": {
        "ref": "modelId"
    }
}
```

```json
{
    "composite": {
        "ref": "address"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite"></a>3.1.1.5.1.1.1.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite > composite`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                                                                      | Pattern | Type   | Deprecated | Definition | Title/Description                                                                    |
| --------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------ |
| + [ref](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite_ref ) | No      | string | No         | -          | <h4> Model Reference </h4>. <p>  Use ID of the referenced model as values here.  ... |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_value_oneOf_i3_composite_ref"></a>3.1.1.5.1.1.1.4.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > value > oneOf > Composite > composite > ref`

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Model Reference </h4>. <p>  Use ID of the referenced model as values here. A record of the referenced model will be used as value for this attribute.</p>

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties"></a>3.1.1.5.1.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties`

**Title:** Attribute Properties

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Attribute Properties </h4><p> This config is used to specify protocol specific attribute properties such as *column name* and *data type* for a MySQL column, *field name* and *field  type* for an elasticsearch index, and so on.</p><p> Dore uses this config for creating models and running queries on them in the underlying datastore.<p><p> Since each protocol has different requirements for configuring an attribute, this config varies from one protocol to the other. Please refer to the protocol specific sections below to view which fields are required for a particular protocol.</p>

| Any of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [MySQL](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0)         |
| [PostgreSQL](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1)    |
| [MongoDB](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2)       |
| [Elasticsearch](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0"></a>3.1.1.5.1.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL`

**Title:** MySQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>MySQL attribute properties</h4><p>  An attribute corresponds to a column of a MySQL table.</p><p> Use this schema when the `datastore` id on the model to which this attribute belongs refers to a datastore that uses the `mysql` protocol.</p>

| Property                                                                                               | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [columnName](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnName ) | No      | string | No         | -          | Column Name       |
| + [columnType](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnType ) | No      | string | No         | -          | Column Type       |

**Examples:** 

```json
{
    "properties": {
        "columnName": "foo",
        "columnType": "DATETIME"
    }
}
```

```json
{
    "properties": {
        "columnName": "bar",
        "columnType": "DECIMAL(5,2)"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnName"></a>3.1.1.5.1.1.2.1.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL > columnName`

**Title:** Column Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4>Column Name</h4><p>  Name of the MySQL column that the attribute corresponds to.</p><p> While creating tables in MySQL for MySQL bound models in the manifest,  Dore infers the required column name from this field's value.</p>

**Examples:** 

```json
"column_one"
```

```json
"column_two"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i0_columnType"></a>3.1.1.5.1.1.2.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MySQL > columnType`

**Title:** Column Type

| Type | `string` |
| ---- | -------- |

**Description:** <h4>Column Type</h4><p> Data type of the MySQL column that the attribute corresponds to.</p><p> While creating tables in MySQL for MySQL bound models in the manifest,  Dore infers the required data type for a column from this field's value.</p><p> All <a target="_blank" href="https://dev.mysql.com/doc/refman/8.0/en/data-types.html">data types supported by MySQL</a> are supported here.</p>

**Examples:** 

```json
"DATETIME"
```

```json
"DECIMAL(5,2)"
```

```json
"VARCHAR(4)"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1"></a>3.1.1.5.1.1.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL`

**Title:** PostgreSQL

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>PostgreSQL attribute properties</h4><p> An attribute corresponds to a column of a PostgreSQL table</p><p> Use this schema when the `datastore` id on the model to which this attribute belongs refers to a datastore that uses the `postgres` protocol.</p>

| Property                                                                                               | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [columnName](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnName ) | No      | string | No         | -          | Column Name       |
| + [columnType](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnType ) | No      | string | No         | -          | Column Type       |

**Examples:** 

```json
{
    "properties": {
        "columnName": "foo",
        "columnType": "DATETIME"
    }
}
```

```json
{
    "properties": {
        "columnName": "bar",
        "columnType": "DECIMAL(5,2)"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnName"></a>3.1.1.5.1.1.2.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL > columnName`

**Title:** Column Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4>Column Name</h4><p>  Name of the PostgreSQL column that the attribute corresponds to.</p><p> While creating tables in PostgreSQL for PostgreSQL bound models in the manifest,  Dore infers the required column name from this field's value.</p>

**Examples:** 

```json
"column_one"
```

```json
"column_two"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i1_columnType"></a>3.1.1.5.1.1.2.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > PostgreSQL > columnType`

**Title:** Column Type

| Type | `string` |
| ---- | -------- |

**Description:** <h4>Column Type</h4><p> Data type of the PostgreSQL column that the attribute corresponds to.</p><p> While creating tables in PostgreSQL for PostgreSQL bound models in the manifest,  Dore infers the required data type for a column from this field's value.</p><p> All <a target="_blank" href="https://www.postgresql.org/docs/current/datatype.html"> data types supported by PostgreSQL</a> are supported here.</p>

**Examples:** 

```json
"DATETIME"
```

```json
"DECIMAL(5,2)"
```

```json
"CIDR"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2"></a>3.1.1.5.1.1.2.3. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MongoDB`

**Title:** MongoDB

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4>MongoDB attribute properties</h4><p> An attribute corresponds to a <a href="https://www.mongodb.com/docs/manual/core/document/#document-structure" target="_blank">  field of a MongoDB collection </a></p><p> Use this schema when the `datastore` id on the model to which this attribute belongs refers to a datastore that uses the `mongodb` protocol.</p>

| Property                                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [fieldName](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2_fieldName ) | No      | string | No         | -          | Field Name        |

**Example:** 

```json
{
    "properties": {
        "fieldName": "foo"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i2_fieldName"></a>3.1.1.5.1.1.2.3.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > MongoDB > fieldName`

**Title:** Field Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4>Field Name</h4><p> Name of the MongoDB field that the attribute corresponds to.</p><p> While creating collections in MongoDB for MongoDB bound models in the manifest, Dore infers the required field name from this field's value.</p>

**Examples:** 

```json
"field_one"
```

```json
"another_field"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3"></a>3.1.1.5.1.1.2.4. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch`

**Title:** Elasticsearch

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Elasticsearch attribute properties </h4><p> An attribute corresponds to a <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html#documents-indices" target="_blank"> field of an elasticsearch index </a>.</p><p> Use this schema when the `datastore` id on the model to which this attribute belongs refers to a datastore that uses the `elasticsearch7` or `elasticsearch8` protocol.</p>

| Property                                                                                             | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [fieldName](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldName ) | No      | string      | No         | -          | Field Name        |
| + [fieldType](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType ) | No      | Combination | No         | -          | Field Type        |

**Examples:** 

```json
{
    "properties": {
        "fieldName": "foo",
        "fieldType": "int"
    }
}
```

```json
{
    "properties": {
        "fieldName": "bar",
        "fieldType": {
            "time_frame": {
                "type": "date_range",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            }
        }
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldName"></a>3.1.1.5.1.1.2.4.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldName`

**Title:** Field Name

| Type | `string` |
| ---- | -------- |

**Description:** <h4> Field Name </h4><p> Name of the Elasticsearch field that the attribute corresponds to.</p>

**Examples:** 

```json
"foo"
```

```json
"bar"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType"></a>3.1.1.5.1.1.2.4.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType`

**Title:** Field Type

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** <h4> Field Type </h4><p> While creating indices in Eleasticsearch for elasticsearch bound models in the manifest, Dore creates an index and an<a href="https://www.elastic.co/guide/en/elasticsearch/reference/8.3/explicit-mapping.html#create-mapping" target="_blank"> index mapping </a> before generating and storing records for the model. Dore uses the `fieldType` value to assign the right data types for fields  when creating an index mapping in Elasticsearch.</p><p> You can use any  <a href="https://www.elastic.co/guide/en/elasticsearch/reference/8.3/mapping-types.html" target="_blank"> field data type that is supported by elasticsarch </a> here.</p>

| One of(Option)                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- |
| [Simple Data Types](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i0)  |
| [Complex Data Types](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i1) |

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i0"></a>3.1.1.5.1.1.2.4.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType > oneOf > Simple Data Types`

**Title:** Simple Data Types

| Type | `string` |
| ---- | -------- |

**Description:** Use this when field types can be represented as strings.

**Examples:** 

```json
"int"
```

```json
"keyword"
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i0_properties_anyOf_i3_fieldType_oneOf_i1"></a>3.1.1.5.1.1.2.4.2.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Definition > properties > anyOf > Elasticsearch > fieldType > oneOf > Complex Data Types`

**Title:** Complex Data Types

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Use this when field types need to be represented as objects.

**Example:** 

```json
{
    "type": "date_range",
    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
}
```

**Examples:** 

```json
{
    "fieldType": "int"
}
```

```json
{
    "fieldType": "keyword"
}
```

```json
{
    "fieldType": {
        "type": "date_range",
        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1"></a>3.1.1.5.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Reference`

**Title:** Attribute Reference

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Attribute Reference </h4><p> An attribute can be defined in a file separate from the manifest file.</p><p> You can, if you want, define each attribute in a separate file similar to how you can store each model and datastore in a separate file. We have no recommendations for or against this.  So, you might want to take a call to start splitting attributes across different files if you feel your model file is getting too large and difficult to read.</p> Use this schema when the attribute is defined in a separate file and you need to provide a  reference to that file in the manifest.</p> <p> Use the `ref` field in the manifest and provide absolute path to the file that actually contains the <a href="#tab-pane_datastores_pattern1_oneOf_i0">attribute definition </a>.</p> In the example, the definition for `attribute_1` is present in a separate file and the `ref`erence to that file is added in the manifest.</p>

| Property                                                             | Pattern | Type   | Deprecated | Definition | Title/Description                                            |
| -------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------ |
| + [ref](#models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1_ref ) | No      | string | No         | -          | Absolute path to file that contains the attribute definition |

**Example:** 

```json
{
    "attribute_1": {
        "ref": "/abs/path/to/file.json"
    }
}
```

##### <a name="models_pattern1_oneOf_i0_attributes_pattern1_oneOf_i1_ref"></a>3.1.1.5.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Definition > attributes > Attribute > oneOf > Attribute Reference > ref`

| Type | `string` |
| ---- | -------- |

**Description:** Absolute path to file that contains the attribute definition

**Example:** 

```json
"/abs/path/to/file.json"
```

**Example:** 

```json
{
    "attributes": {
        "attribute_1": {
            "ref": "/abs/path/to/file.json"
        },
        "attribute_2": {
            "properties": {
                "columnName": "foobar",
                "columnType": "DATE"
            },
            "value": {
                "faker": {
                    "date_between": {
                        "start_date": "-1M"
                    }
                }
            }
        }
    }
}
```

#### <a name="models_pattern1_oneOf_i1"></a>3.1.2. Property `Dore Manifest schema > models > Model > oneOf > Model Reference`

**Title:** Model Reference

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** <h4> Model Reference </h4><p> A model can be defined in a file separate from the manifest file.</p><p> You would generally want to define each model in a separate file. It is recommended to spread different parts of the manifest such as models and datastores across  different files in order to keep each config small and readable.</p> Use this schema when the model is defined in a separate file and you need to provide a  reference to that file in the manifest.</p> <p> Use the `ref` field in the manifest and provide absolute path to the file that actually contains the <a href="#tab-pane_models_pattern1_oneOf_i0"> model definition </a>.</p><p> In the example, the definition for `model_1` is present in a separate file and the  `ref`erence to that file is added in the manifest.</p>

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description                                            |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------ |
| + [ref](#models_pattern1_oneOf_i1_ref ) | No      | string | No         | -          | Absolute path to file that contains the model definition<br> |

**Example:** 

```json
{
    "model_1": {
        "ref": "/abs/path/to/file.json"
    }
}
```

##### <a name="models_pattern1_oneOf_i1_ref"></a>3.1.2.1. Property `Dore Manifest schema > models > Model > oneOf > Model Reference > ref`

| Type | `string` |
| ---- | -------- |

**Description:** Absolute path to file that contains the model definition<br>

**Example:** 

```json
"/abs/path/to/file.json"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2022-08-29 at 14:29:19 +0530
