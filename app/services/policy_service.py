import os
import uuid
from web3 import Web3
from eth_account import Account
from services.web3_service import contract, w3

PRIVATE_KEY = os.getenv("PRIVATE_KEY", "")
OWNER = Account.from_key(PRIVATE_KEY).address if PRIVATE_KEY else None


def create_policy(agent, token, total_budget, per_tx_limit, valid_from, valid_until, purpose):
    policy_id = str(uuid.uuid4())[:8].upper()

    if contract and w3 and PRIVATE_KEY and OWNER:
        try:
            agent_addr = Web3.to_checksum_address(agent) if agent.startswith("0x") else agent
            # Non-address token symbols (ETH, USDC) use zero address
            zero = "0x0000000000000000000000000000000000000000"
            token_addr = Web3.to_checksum_address(token) if token.startswith("0x") else Web3.to_checksum_address(zero)
            purpose_hash = w3.keccak(text=purpose)

            tx = contract.functions.createPolicy(
                agent_addr,
                token_addr,
                total_budget,
                per_tx_limit,
                valid_from,
                valid_until,
                purpose_hash,
                True
            ).build_transaction({
                "from":     OWNER,
                "nonce":    w3.eth.get_transaction_count(OWNER),
                "gas":      300_000,
                "gasPrice": w3.eth.gas_price,
            })

            signed  = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
            tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
            w3.eth.wait_for_transaction_receipt(tx_hash, timeout=60)

            print(f"[policy_service] On-chain policy tx: {tx_hash.hex()}")
            return policy_id, f"0x{tx_hash.hex()}"

        except Exception as e:
            print(f"[policy_service] Web3 call failed, using demo mode: {e}")

    return policy_id, "demo_tx_hash"
