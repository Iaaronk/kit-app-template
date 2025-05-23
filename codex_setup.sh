#!/usr/bin/env bash
set -eux

# 1. Install vendored wheels if present
if ls third_party/wheels/*.whl 1>/dev/null 2>&1; then
  pip install third_party/wheels/*.whl
fi

# 2. Add ./stubs directory to PYTHONPATH so imports succeed
export PYTHONPATH="$PWD/stubs:$PYTHONPATH"
