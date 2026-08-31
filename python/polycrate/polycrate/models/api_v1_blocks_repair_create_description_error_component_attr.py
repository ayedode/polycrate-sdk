from typing import Literal

ApiV1BlocksRepairCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_BLOCKS_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_blocks_repair_create_description_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateDescriptionErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
