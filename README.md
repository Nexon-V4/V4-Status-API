# V4-Status-API
An python implementation for check statuses of V4 services

# Usage

This project only supports `python>=3.6`

Install dependencies:

```
pip install -r requirements.txt
```

Execution:

```python
status = lookup_status()
print(status)
print(status['IsMaintenance'])
print(status['IsGameMaintenance'])
print(status['IsLoginMaintenance'])

# outputs
"""
{'IsMaintenance': False, 'IsGameMaintenance': False, 'IsLoginMaintenance': False}
False
False
False
"""
```
