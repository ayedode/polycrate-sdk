from typing import Literal

ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentAttr = Literal["batch_identifier"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentAttr
] = {
    "batch_identifier",
}


def check_api_v1_block_rollouts_archive_create_batch_identifier_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
