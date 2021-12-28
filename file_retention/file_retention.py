#!/usr/bin/env python
import glob
import os
from os.path import expanduser
from datetime import date, timedelta
import yaml
from yaml.loader import SafeLoader
import click


@click.command()
@click.option('--retention','-r', default=15, help='Number of days')
@click.option('--extension','-e', default="*", help='Extension of files')
@click.option('--path','-p', help='Path')

def file_retention(retention, extension, path):
    """ Delete files based on predefined dates """
    space = "---------------------------------------------------------"
    today = date.today()
    days_ago = today - timedelta(days=retention)
    home = expanduser("~")
    output_files = os.path.join(home, "file_retention")
    click.echo(space)
    click.echo(f'Diretório criado: {output_files}')
    os.makedirs(output_files, exist_ok = True)

    def create_yaml(dictionary, date):
        """ cria o arquivo yaml esperando um dicionario e uma data"""
        full_path = os.path.join(output_files, f'{date}.yml')
        with open(full_path, 'w') as yaml_file:
            yaml.dump(dictionary, yaml_file, default_flow_style=False)
        click.echo(space)
        click.echo(f'Arquivo exportado: {full_path}')

    def get_files(fullpath):
        """ Pega os arquivos recursivamente esperando um diretório e uma extensão de arquivo"""
        values = [f for f in glob.glob(f"{fullpath}**/*.{extension}", recursive=True)]
        count = len(values)
        click.echo(space)
        click.echo(f'{count} arquivos encontrados!')
        return values

    def create_dict(date):
        """ Cria o dicionario com a data e a lista de arquivos encontrado na funcao get_files() """
        dicts = {}
        dicts["date"] = date
        dicts["arquivos"] = get_files(path)
        click.echo(space)
        click.echo(f'Dicionário criado!')
        return dicts

    def read_yaml(files, key):
        """ lê o arquivo yaml e filtra"""
        full_path = os.path.join(output_files, f'{files}.yml')
        with open(full_path, "r") as config:
            data = yaml.load(config, Loader=SafeLoader)
            data = data[key]
            click.echo(space)
            click.echo(f"Lendo o arquivo: {full_path}")
            return data

    def delete_yaml(files):
        

    def delete_files(date):
        """ delete os arquivos consultando o yaml ~/file_retention/yyyy-mm-dd.yml"""
        files = read_yaml(date, "arquivos")
        click.echo(space)
        click.echo(f"Os arquivos de {retention} dias atrás serão excluídos.")
        click.echo(space)
        for f in files:
            if os.path.exists(f):
                click.echo(f"Arquivo removido: {f}")
                os.remove(f"{f}")
            else:
                click.echo(f"O Arquivo {f} não existe mais") 
        click.echo(space)

    create_yaml(create_dict(today), today)
    delete_files(days_ago)

file_retention()