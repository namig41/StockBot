from dataclasses import dataclass


@dataclass
class BatchListItemDTO:
    reference: str
    sku: str
