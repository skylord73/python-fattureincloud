# Python SDK for FattureInCloud API

## Installation


```bash
pip install fattureincloud
```

## Usage

Initialize the class with your **api_uid** and **api_key**, you can find in the API menu of your APP

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

For every objects you have a set of request as documented in [Fatture in Cloud](https://api.fattureincloud.it/v1/documentation/dist/) API reference

## Example

```python
>>> from fattureincloud import FattureInCloud

>>> fic = FattureInCloud(api_uid,api_key)
>>> fatt_dict = fic.documento.fatture.lista(2020)
```

returns a dictionary of your invoices for year 2020 

```python
>>> fatt_list = fatt_dict['lista_documenti]
```

you can now get your invoce **id** af the first invoice to ask for details:

```python
>>> id =fatt_list[0]['id']
>>> fatt_dettagli = fic.documento.fatture.dettagli(id)
```

you can now inqury the invoice fileds using simple methods:

```python
>>> fatt_dettagli.name
'name of the invoice customer'

```


