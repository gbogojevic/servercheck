import click
import json
import sys


@click.command()
@click.option("--server", "-s", default=None, multiple=True, help="IP:port mapping")
@click.option("--filename", "-f", default=None, help="Path to input json file")
def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("must provide a JSON file or servers")

    # Create a set of servers IP:PORT to prevent duplicates
    servers = set()

    # If --filename or -f opiton is used then attempt to open file before
    # making requests

    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: unable to open or read JSON file")
            sys.exit(1)

    if server:
        for s in server:
            servers.add(s)

    print(servers)


if __name__ == "__main__":
    cli()