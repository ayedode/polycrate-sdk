from typing import Literal

ApiV1BlocksUpdateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateActionsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_update_actions_error_component_code(value: str) -> ApiV1BlocksUpdateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
