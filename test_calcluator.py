
name: Python CI Pipeline

on:
  push:
    branches:
      - main

  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v5

      - name: Set Up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Build Application
        run: |
          python -m py_compile calculator.py

      - name: Run Automated Tests
        run: |
          python -m pytest -v

