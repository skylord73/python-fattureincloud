# Acquisti
from fattureincloud import mixins
from fattureincloud.base import Manager, RESTObject



ACQUISTO_NUOVO_ATTRS = (
    (
        'nome',
    ),
    (
  'tipo',
  'id_fornitore',
  'piva',
  'cf',
  'autocompila_anagrafica',
  'salva_anagrafica',
  'data',
  'descrizione',
  'categoria',
  'importo_netto',
  'importo_iva',
  'valuta',
  'valuta_cambio',
  'ritenuta_acconto',
  'ritenuta_previdenziale',
  'deducibilita_tasse',
  'detraibilita_iva',
  'ammortamento',
  'centro_costo',
  'numero_fattura',
  'lista_pagamenti',
  'lista_articoli'
  ),
)

ACQUISTO_MODIFICA_ATTRS = (
    tuple(),
    (
      'id',
      'id_fornitore',
      'nome',
      'piva',
      'cf',
      'autocompila_anagrafica',
      'salva_anagrafica',
      'data',
      'descrizione',
      'categoria',
      'importo_netto',
      'importo_iva',
      'valuta',
      'valuta_cambio',
      'ritenuta_acconto',
      'ritenuta_previdenziale',
      'deducibilita_tasse',
      'detraibilita_iva',
      'ammortamento',
      'centro_costo',
      'numero_fattura',
      'lista_pagamenti',
      'lista_articoli'
    ),
)


class Acquisti(mixins.DettagliMixin, mixins.EliminaMixin, mixins.ModificaMixin, RESTObject):
    """
    Acquisti
    """
    _modifica_attrs = ACQUISTO_MODIFICA_ATTRS

    LANGUAGE_IT = 'it'
    LANGUAGE_EN = 'en'
    LANGUAGE_DE = 'de'


class AcquistiManager(mixins.ListaMixin, mixins.CRUDMixin, mixins.InfoMixin, Manager):
    _path = 'acquisti'
    _obj_cls = Acquisti
    _nuovo_attrs = ACQUISTO_NUOVO_ATTRS
    _modifica_attrs = ACQUISTO_MODIFICA_ATTRS
    _dettagli_obj_key = 'dettagli_documento'