from dtos.product import ProductListItemDTO


def convert_products_dtos_to_message(products: list[ProductListItemDTO]) -> str:
    return "\n".join(
        (
            "Список всех доступных продуктов: ",
            "\n".join(
                (
                    f"{index + 1}. Товар: '{product.reference}', артикул: '{product.sku}'"
                    for index, product in enumerate(products)
                )
            ),
        ),
    )
