#! /bin/bash

tr ";" "\t" < /tmp/atendimentos_desafio_stone.csv | mongoimport --host mongodb:27017 -d stone -c initialCalls --type tsv --headerline --mode insert
tr ";" "\t" < /tmp/estoque_bases_desafio_stone.csv | mongoimport --host mongodb:27017 -d stone -c initialStock --type tsv --headerline --mode insert
