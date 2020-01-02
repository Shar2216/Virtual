from dataclasses import dataclass
from typing import List

from src.types.full_block import FullBlock
from src.types.header_block import HeaderBlock
from src.types.peer_info import PeerInfo
from src.types.proof_of_time import ProofOfTime
from src.types.sized_bytes import bytes32
from src.types.transaction import Transaction
from src.util.cbor_message import cbor_message
from src.util.ints import uint32, uint64


"""
Protocol between full nodes.
"""


@dataclass(frozen=True)
@cbor_message
class NewTip:
    height: uint32
    weight: uint64
    header_hash: bytes32


@dataclass(frozen=True)
@cbor_message
class TransactionId:
    transaction_id: bytes32


@dataclass(frozen=True)
@cbor_message
class RequestTransaction:
    transaction_id: bytes32


@dataclass(frozen=True)
@cbor_message
class NewTransaction:
    transaction: Transaction


@dataclass(frozen=True)
@cbor_message
class NewProofOfTime:
    proof: ProofOfTime


@dataclass(frozen=True)
@cbor_message
class UnfinishedBlock:
    block: FullBlock


@dataclass(frozen=True)
@cbor_message
class RequestBlock:
    header_hash: bytes32


@dataclass(frozen=True)
@cbor_message
class Block:
    block: FullBlock


@dataclass(frozen=True)
@cbor_message
class RequestPeers:
    """
    Return full list of peers
    """


@dataclass(frozen=True)
@cbor_message
class Peers:
    peer_list: List[PeerInfo]


@dataclass(frozen=True)
@cbor_message
class RequestAllHeaderHashes:
    tip_header_hash: bytes32


@dataclass(frozen=True)
@cbor_message
class AllHeaderHashes:
    header_hashes: List[bytes32]


@dataclass(frozen=True)
@cbor_message
class RequestHeaderBlock:
    height: uint32
    header_hash: bytes32


@dataclass(frozen=True)
@cbor_message
class RespondHeaderBlock:
    header_block: HeaderBlock
