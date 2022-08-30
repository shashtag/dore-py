# What is Dore?

Dore is a schema based fake data generation tool.

# Why is it called Dore?

No particular reason. I just wanted to share my thoughts on how we should have spelt *door*. 

# What can you do with it?

Dore allows you to define the details of your target data in a config file, known as the **Manifest**, and Dore
takes care of generating this data for you. <br>

With Dore, you can:
* Generate fake data for **multiple models across multiple protocols with complex schema dependencies with just a 
  single command**. <br>
  For example, you can set up your entire database with data for all tables with FK/PK integrity constraints in a single 
  command.
  
  
* Generate fake data with **dependencies between models regardless of the protocol**. <br> 
  For example, you can have a column in a MySQL table be dependent/have a FK relationship on a field in an 
  Elasticsearch index.
  

* Support for generating data for attributes that are **nested to arbitrary depth**. **Nested attributes can in turn be 
  dependent** or have their values derived from attributes of models in other protocols. <br>
  For example, you can have a MongoDB 
  collection which has a field that derives its value from a row of a PostgreSQL table or another MongoDB collection's 
  doc.

## Getting Started

### Installation

##### Optional: Create a virtual env and activate it.

```shell
python3 -m venv venv && source venv/bin/activate
```

#### Install Dore

```shell
pip install dore
```
### Usage

```shell
dore --manifest /path/to/manifest.json --var1=val1 --var2=val2 ...
```


## Useful Links

* [GitHub](https://github.com/bkn-dore/dore-py)
* [Tutorial](https://github.com/bkn-dore/dore-py/tree/master/tutorial)
* [Examples](https://github.com/bkn-dore/dore-py/tree/master/examples)
* [Manifest Docs](https://bkn-dore.github.io)

## CLI Options
`Dore` command supports the following cli args. Required options are specified with `**` next to them. 

Details for each supported cli arg is mentioned in [further sections](#More on CLI options)

| Option                       | Description                                                  | Values        |
| -----------------------------|--------------------------------------------------------------|---------------|              
| `--manifest`**               | Absolute path to [manifest](#manifest) file                  | /path/to/file |
| `--seed`                     | [Seed Options](#seed)                                        | Integer       |
| `--scale`                    | Scale Factor                                                 | Number        |
| `--cache`                    | [Cache Options](#caching)                                    | redis / local |
| `--drop-conflicting-models`  | [Conflict handling options](#handling-conflicts)             | -             |
| `--var1=val1`, `--var2=val2` | Provide values for [Manifest variables](#Manifest Variables) | -             |

# Terminology

You will come across these terms quite frequently in Dore's documentation:

* **Protocol**: A protocol is an implementation of a system. For example, `mysql`, `mongodb`, `elasticsearch8` are 
  all protocols.
  
  
* **Datastore**: A datastore usually represents a particular database, whether that's a database running within 
  a locally installed MySQL server, a remote Elasticsearch cluster that is running on your company's servers, or
  a remote MongoDB database hosted by a cloud provider.
  

* **Model**: A model represents a set of structured data, called records. Models usually represent a Table in
  SQL databases, a Collection in MongoDB, an Index in Elasticsearch, etc.
  

* **Attributes**: Models consist of a set of attributes. Attributes usually correspond to columns of a table in SQL 
  databases, fields of a collection in MongoDB, etc.
  

* **Manifest**: The manifest is a config you provide to Dore which contains details of the data that needs
   to be generated. <br>
  On a high level, the manifest has details about protocols, datastores, models, attributes. etc.
  
Let's drive these concepts home with a few examples:
* A MySQL database `foo_db` has a table `bar_tbl` which has columns `a`, `b`, and `c`.
    * Here, `mysql` is the **protocol**.
    * `foo_db` is a **datastore**.
    * `bar_tbl` is a **model**.
    * The model has **attributes** `a`, `b`, and `c`.
  
    
* A MongoDB database `foo_db` has a collection `bar_collection` which has docs with fields `a`, `b`, and `c`.
    * Here, `mongodb` is the **protocol**.
    * `foo_db` is a **datastore**.
    * `bar_collection` is a **model**.
    * The model has **attributes** `a`, `b`, and `c`.
  
  
### Supported Protocols

Currently, Dore supports the following protocols.

| NoSQL Protocols | SQL Protocols    |
| ----------------|------------------|
| Elasticsearch   | MySQL            |
| MongoDB         | PostgreSQL       |
  
# Tutorial

If this is the first time you're using Dore, we recommend you check our [tutorial](./tutorial) out to get familiar with
it. 

In the tutorial, we go through a hands on exercise where we use Dore to generate data for a popular (and relatively 
non trivial) database schema from scratch!

## Examples

There are examples present in [examples](./examples) directory of this repo with instructions
on how to execute them. These can help you get started on creating your first manifest or can serve as a reference 
in case you're stuck.

# More on CLI options

### Manifest

The manifest is the core config that contains specifications about the target data.

A detailed documentation for the *Manifest* is available here:
* https://Dore-datagen.github.io/

### Caching
In order to generate records for models that are dependent on other models, the dependent model's records are loaded 
into cache to avoid repeated db calls (which can be quite slow). By default, Dore uses a local python dictionary based 
cache. But, you can make Dore work with other caches as well.

#### Caching with Redis
Run Dore with redis cache by using `--cache redis` argument while invoking Dore:
```shell
(dore-venv)$ dore \
  ...
  --cache redis \
  --redis-host <redis-host> \
  --redis-port <redis-port> \
  ...
```

#### CLI Options for Redis caching

| Options           | Description                              | Values                |
| ----------------- | ---------------------------------------- | --------------------- |
| --redis-host      | Host URL for the redis cluster           | `"127.0.0.1"`, ...    |
| --redis-port      | Port on which redis server is listening  | `6379`, ...           |

<br>


### Handling Conflicts
Dore tries to create models and datastores based on what has been specified in the Manifest. Being mindful of how
Dore handles name conflicts is important.

**!! WARNING !!**<br> 
**BE CAREFUL WHILE USING THIS AS IT DELETES MODELS FROM DATASTORE**

Dore's default behavior to fail on encountering model name conflicts can be altered by using the 
`--drop-conflicting-models` option.

When this option is used, Dore **DROPS / DELETES** conflicting models in the 
datastore and re-creates them.

```shell
(dore-venv)$ dore ... --drop-conflicting-models ...
```
<br>


### Seed
At its core, Dore creates datastores, models, and generates data for models based on the manifest provided. 

Each record of a model is a set of values for attributes of the model. The value generated for an attribute
is based on the specified generator type and quite a few of the generators have randomness associated with them 
(ex: `faker`, `randomSelector`, etc). Each Dore run results into different records being generated for the same
model due to this inherent randomness.

In order to reproduce the outcomes/records of a previous run, you can specify the `--seed` arg while invoking
Dore. The seed value for each run is usually present in the output logs of a Dore run.

For example, if you invoked Dore, you would see something like the below in output logs:

```shell
# First invocation (without --seed flag)

(dore-venv)$ dore ...

# --- Logs ---

# Get seed value from output logs
# ... other logs ...
[2022-08-08 10:04:58,164] [INFO] [config.Dore_config]: executing with seed [-4140708867]
# ... other logs ...
```

You can then invoke Dore with above seed value in any subsequent runs and reproduce the same records/outcomes as the one above.

```shell
# Second, Third, Nth invocation with --seed flag produces same results as first invocation.

(dore-venv)$ dore ... --seed -4140708867 ...
```
