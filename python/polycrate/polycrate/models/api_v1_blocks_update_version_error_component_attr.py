from typing import Literal

ApiV1BlocksUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_blocks_update_version_error_component_attr(value: str) -> ApiV1BlocksUpdateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
