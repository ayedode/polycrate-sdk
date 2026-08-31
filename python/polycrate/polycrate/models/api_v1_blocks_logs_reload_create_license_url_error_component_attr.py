from typing import Literal

ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponentAttr
] = {
    "license_url",
}


def check_api_v1_blocks_logs_reload_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
