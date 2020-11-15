# Python SDK for FattureInCloud API

Python API to access data in FattureInCloud.it software

*Read this in other languages : [Italiano](../../README.it.md)*

## Installation


```bash
pip install fattureincloud
```

## Usage

Initialize the class with your **api_uid** and **api_key**, you can find in the API menu of your App

```python
fic = FattureInCloud(api_uid,api_key)
```

You can now access to the following abjects:

* **anagrafica**
* prodotto (TBD)
* **documento**
* **acquisto**
* corrispettiv (TBD)
* magazzino (TBD)
* mail (TBD)
* info (TBD)

For every objects you have a set of requests as documented in [Fatture in Cloud](https://api.fattureincloud.it/v1/documentation/dist/) API reference

## Example

```python
>>> from fattureincloud import FattureInCloud

>>> fic = FattureInCloud(api_uid,api_key)
>>> fatt_list = fic.documento.fatture.lista(2020)
```

returns a list of your invoices for year 2020 
you can now get your invoce **id** of the first invoice to ask for details:

```python
>>> id =fatt_list[0]['id']
>>> fatt_dettagli = fic.documento.fatture.dettagli(id)
```

you can now inqury the invoice fields using simple methods:

```python
>>> fatt_dettagli.name
'name of the invoice customer'

```
or get a dictionary with the list of fields:

```python
>>> fatt_dettagli.fields()
dict_keys(['id', 'tipo', 'anno_competenza', 'id_cliente', 'nome', 'indirizzo_via', ...])

```

you can get the purchase invoices:

```python
>>> acq_list = fic.acquisti.lista(2020)
>>> id =acq_list[0]['id']
>>> acq_dettagli = fic.acquisti.dettagli(id)

```


