from typing import Literal

ApiV1BlocksUpdateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateAutoRolloutErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_update_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
