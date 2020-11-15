# Python SDK for FattureInCloud API

Python API per accedere al software di FattureInCloud.ii

*Leggilo in altre lingue : [English](README.md)*

## Instalazione


```bash
pip install fattureincloud
```

## Utilizzo

Inizializza la classe con i tuoi **api_uid** e **api_key**, che puoi trovare nel menu API della tua applicazione

```python
fic = FattureInCloud(api_uid,api_key)
```

Una volta instanzato l'oggetto FattureInCloud hai accesso ai seguenti oggetti:

* **anagrafica**
* prodotto (TBD)
* **documento**
* **acquisto**
* corrispettiv (TBD)
* magazzino (TBD)
* mail (TBD)
* info (TBD)

Per ogni oggetto sono disponibili una serie di richieste come documentato nella guida alle API di [Fatture in Cloud](https://api.fattureincloud.it/v1/documentation/dist/)

## Esempio

```python
>>> from fattureincloud import FattureInCloud

>>> fic = FattureInCloud(api_uid,api_key)
>>> fatt_list = fic.documento.fatture.lista(2020)
```

restituisce la lista di fatture relative all'anno 2020
una volta ottenuto l'**id** della fattura desiderata puoi chiederne i dettagli:

```python
>>> id =fatt_list[0]['id']
>>> fatt_dettagli = fic.documento.fatture.dettagli(id)
```

una volta ottenuto l'oggetto fattura puoi chiederne i vslori dei campi utilizzando un metodo con il niome del campo:

```python
>>> fatt_dettagli.name
'nome cognome'

```
oppure ottenere la lista di tutti i campi:

```python
>>> fatt_dettagli.fields()
dict_keys(['id', 'tipo', 'anno_competenza', 'id_cliente', 'nome', 'indirizzo_via', ...])

```

puoi invece ottenere l'elenco degli acquisti:

```python
>>> acq_list = fic.acquisti.lista(2020)
>>> id =acq_list[0]['id']
>>> acq_dettagli = fic.acquisti.dettagli(id)

```


