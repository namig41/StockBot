from dtos.batch import BatchListItemDTO


def convert_batch_response_to_chat_dto(batch_data: dict) -> BatchListItemDTO:
    return BatchListItemDTO(
        reference=batch_data["reference"],
        sku=batch_data["sku"],
    )
