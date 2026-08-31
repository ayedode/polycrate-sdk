from typing import Literal

ApiV1BlocksListVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_blocks_list_version_error_component_attr(value: str) -> ApiV1BlocksListVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
