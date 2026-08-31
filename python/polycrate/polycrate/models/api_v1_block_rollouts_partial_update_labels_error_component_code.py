from typing import Literal

ApiV1BlockRolloutsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
