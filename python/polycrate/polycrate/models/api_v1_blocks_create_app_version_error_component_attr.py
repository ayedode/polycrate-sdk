from typing import Literal

ApiV1BlocksCreateAppVersionErrorComponentAttr = Literal["app_version"]

API_V1_BLOCKS_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateAppVersionErrorComponentAttr] = {
    "app_version",
}


def check_api_v1_blocks_create_app_version_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateAppVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
