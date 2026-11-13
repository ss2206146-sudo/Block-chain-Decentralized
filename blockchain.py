import hashlib
import json
from datetime import datetime, timezone


class ValidationResult(tuple):
    def __new__(cls, is_valid, errors):
        return super().__new__(cls, (is_valid, errors))

    def __bool__(self):
        return bool(self[0])


class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        encoded = json.dumps(data, sort_keys=True, default=str).encode()
        return hashlib.sha256(encoded).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash,
        }


class Blockchain:
    def __init__(self):
        self.chain = [Block(0, {"type": "GENESIS"}, "0")]

    def add_block(self, transactions):
        previous = self.chain[-1]
        block = Block(len(self.chain), transactions, previous.hash)
        self.chain.append(block)
        return block

    def is_valid(self):
        errors = []

        if not self.chain:
            return ValidationResult(False, ["Blockchain is empty."])

        genesis = self.chain[0]
        if genesis.index != 0:
            errors.append(f"Block {genesis.index}: genesis block index is invalid.")

        if genesis.previous_hash != "0":
            errors.append("Genesis block previous hash is invalid.")

        if genesis.hash != genesis.calculate_hash():
            errors.append("Genesis block hash mismatch.")

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.index != i:
                errors.append(f"Block {current.index}: index does not match chain position.")

            if current.hash != current.calculate_hash():
                errors.append(f"Block {current.index}: hash mismatch.")

            if current.previous_hash != previous.hash:
                errors.append(
                    f"Block {current.index}: previous hash does not match Block {previous.index}."
                )

        return ValidationResult(len(errors) == 0, errors)

    def to_dict(self):
        return [block.to_dict() for block in self.chain]
