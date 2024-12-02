from dtos.product import ProductListItemDTO


def convert_product_response_to_chat_dto(product_data: dict) -> ProductListItemDTO:
    return ProductListItemDTO(
        reference=product_data["reference"],
        sku=product_data["sku"],
    )
    