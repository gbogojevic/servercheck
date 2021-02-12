# servercheck

A simple CLI tool that can either take a JSON file with servers and ports to check or a list of host/port combinations to make requests to

# Usage

$ servercheck -s IP1:port -s IP2:port -s IP3:port
{'IP1:port', 'IP2:port', 'IP3:port'}

OR

$ servercheck -f servers.json
{'IP1:port', 'IP1:port2', 'IP2:port'}