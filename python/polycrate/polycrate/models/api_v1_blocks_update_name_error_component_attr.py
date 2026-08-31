from typing import Literal

ApiV1BlocksUpdateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_blocks_update_name_error_component_attr(value: str) -> ApiV1BlocksUpdateNameErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
