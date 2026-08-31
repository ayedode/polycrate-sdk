from typing import Literal

ApiV1BlocksCheckCreateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_CHECK_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_blocks_check_create_version_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
