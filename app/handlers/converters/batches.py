from dtos.batch import BatchListItemDTO


def convert_batches_dtos_to_message(batches: list[BatchListItemDTO]) -> str:
    return "\n".join(
        (
            "Список всех доступных продуктов: ",
            "\n".join(
                (
                    fr"{index + 1}\. Товар: `{batch.reference}`, артикул: `{batch.sku}`"
                    for index, batch in enumerate(batches)
                )
            ),
        ),
    )


def convert_batch_dtos_to_message(batch: BatchListItemDTO) -> str:
    return f"Товар: {batch.reference}, артикул: {batch.sku}"
