from typing import Literal

ApiV1BlockRolloutsCreateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlockRolloutsCreateStateErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollouts_create_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
