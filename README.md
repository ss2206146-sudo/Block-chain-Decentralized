# Blockchain Banking System

Academic/demo project using Python Flask, SQLite and a custom blockchain.

## Features
- User registration and login
- Password hashing
- Simulated bank balance
- Deposit
- Withdrawal
- Account-to-account transfer
- Transaction history
- Blockchain explorer
- Blockchain integrity verification
- REST API for blockchain data

## Run

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create a virtual environment:

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:

pip install -r requirements.txt

5. Start:

python app.py

6. Open:
http://127.0.0.1:5000

The SQLite database `bank.db` is created automatically.

## Demo

Register two accounts. Deposit simulated money into account 1, then transfer some amount to account 2. Open Blockchain to see the blocks and Verify Blockchain to check integrity.

This is an educational simulation. It does not connect to real banks, cards, UPI, cryptocurrency networks or real money.
