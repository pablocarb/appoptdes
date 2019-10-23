#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
synbioParts (c) University of Manchester 2019

synbioParts is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

Created on Fri Oct 18 13:38:19 2019

@author:  Pablo Carbonell, SYNBIOCHEM
@description: Routines to create standard collections of synbio parts.
 - Option 1: import the parts from other collection
 - Option 2: define new parts
"""
import os
import sbol
from doebase.synbioParts import _ReadParts as ReadParts
import pandas as pd

def _UploadDoc(doc,registry='https://synbiohub.org'):
    """ A tabular csv file containing columns: Name, Type, Part is read 
    and each part in added to the SBOL doc.
    Part type should is overriden by the ontology definition in the registry """
    namespace = "http://synbiochem.co.uk"
    sbol.setHomespace( namespace  )
    repo = sbol.PartShop(registry)
    repo.login(os.getenv('IBISBA_SYNBIOHUB_USERNAME'),os.getenv('IBISBA_SYNBIOHUB_PASSWORD'))
    doc.displayId = 'E_coli_Parts'
    doc.name = 'A collection of genetic parts for engineering E. coli'
    doc.description = 'Standard regulatory genetic parts for building E. coli combinatorial libraries in the Galaxy-SynbioCAD. The collection contains a selection of commonly-used origins of replication, resistance cassettes, and inducible promoters.'
    repo.submit(doc)

parts = pd.read_csv('test/RefParts.csv')
doc = ReadParts(parts)
_UploadDoc(doc)
