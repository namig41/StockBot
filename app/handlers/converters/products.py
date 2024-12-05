from dtos.batch import BatchListItemDTO


def convert_products_dtos_to_message(products: list[BatchListItemDTO]) -> str:
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
