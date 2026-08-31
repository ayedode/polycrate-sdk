from typing import Literal

ApiV1BlocksPartialUpdateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateActionsErrorComponentAttr
] = {
    "actions",
}


def check_api_v1_blocks_partial_update_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
