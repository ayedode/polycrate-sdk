from typing import Literal

ApiV1BlocksUpdateIconUrlErrorComponentAttr = Literal["icon_url"]

API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateIconUrlErrorComponentAttr] = {
    "icon_url",
}


def check_api_v1_blocks_update_icon_url_error_component_attr(value: str) -> ApiV1BlocksUpdateIconUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
