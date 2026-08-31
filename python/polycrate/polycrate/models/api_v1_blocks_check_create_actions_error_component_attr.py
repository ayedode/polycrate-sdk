from typing import Literal

ApiV1BlocksCheckCreateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_CHECK_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateActionsErrorComponentAttr] = {
    "actions",
}


def check_api_v1_blocks_check_create_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
