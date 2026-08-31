from typing import Literal

ApiV1BlocksUpdateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateActionsErrorComponentAttr] = {
    "actions",
}


def check_api_v1_blocks_update_actions_error_component_attr(value: str) -> ApiV1BlocksUpdateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
