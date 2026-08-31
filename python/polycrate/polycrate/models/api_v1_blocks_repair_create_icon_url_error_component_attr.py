from typing import Literal

ApiV1BlocksRepairCreateIconUrlErrorComponentAttr = Literal["icon_url"]

API_V1_BLOCKS_REPAIR_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateIconUrlErrorComponentAttr
] = {
    "icon_url",
}


def check_api_v1_blocks_repair_create_icon_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateIconUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
