from typing import Literal

ApiV1BlocksPartialUpdateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateAutoRolloutErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_partial_update_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
