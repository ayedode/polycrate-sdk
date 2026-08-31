from typing import Literal

ApiV1BlocksCreateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_blocks_create_version_error_component_attr(value: str) -> ApiV1BlocksCreateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
