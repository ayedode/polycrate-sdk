from typing import Literal

ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponentAttr = Literal["batch_identifier"]

API_V1_BLOCK_ROLLOUTS_UPDATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponentAttr
] = {
    "batch_identifier",
}


def check_api_v1_block_rollouts_update_batch_identifier_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateBatchIdentifierErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_BATCH_IDENTIFIER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
