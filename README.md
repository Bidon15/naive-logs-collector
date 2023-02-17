Motivation
---

While testground is still in progress with out-of-the-box metrics and logs collection, this is the scripts to just have
at least some info on test pods' logs

### What are these scripts doing

1. `main.py` -> calling `kubectl exec` to gather metrics.json from app validators
2. stdin accepts run_id from test-plan

### Artifacts

`<number>-<group-id>.log` format in root
