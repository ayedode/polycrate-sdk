from typing import Literal

ApiV1BlockRolloutsUpdateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollouts_update_status_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateStatusErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
