from dtos.batch import BatchListItemDTO


def convert_batch_data_to_batch_dto(batch_data: dict) -> BatchListItemDTO:
    return BatchListItemDTO(
        reference=batch_data["reference"],
        sku=batch_data["sku"],
    )


def convert_batch_dto_to_batch_data(batch: BatchListItemDTO) -> dict:
    return {"reference": batch.reference, "sku": batch.sku}
