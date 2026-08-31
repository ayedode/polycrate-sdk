from typing import Literal

ApiV1BlocksRepairCreateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateActionsErrorComponentAttr
] = {
    "actions",
}


def check_api_v1_blocks_repair_create_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
