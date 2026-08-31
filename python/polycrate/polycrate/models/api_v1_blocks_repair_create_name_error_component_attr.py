from typing import Literal

ApiV1BlocksRepairCreateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCKS_REPAIR_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksRepairCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_blocks_repair_create_name_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateNameErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
