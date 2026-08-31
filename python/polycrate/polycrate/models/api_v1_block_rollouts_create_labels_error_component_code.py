from typing import Literal

ApiV1BlockRolloutsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_create_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
