from dataclasses import dataclass


@dataclass
class ProductListItemDTO:
    reference: str
    sku: str
