from typing import Literal

ApiV1BlocksCreateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateAutoRolloutErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_create_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksCreateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
