from typing import Literal

ApiV1BlockRolloutsUpdateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollouts_update_last_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateLastStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
