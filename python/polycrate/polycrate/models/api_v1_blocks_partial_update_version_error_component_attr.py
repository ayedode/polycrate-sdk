from typing import Literal

ApiV1BlocksPartialUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_blocks_partial_update_version_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
