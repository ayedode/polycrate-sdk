from typing import Literal

ApiV1BlocksPartialUpdateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateActionsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_partial_update_actions_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
