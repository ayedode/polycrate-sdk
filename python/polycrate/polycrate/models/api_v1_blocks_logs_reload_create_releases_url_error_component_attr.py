from typing import Literal

ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponentAttr = Literal["releases_url"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponentAttr
] = {
    "releases_url",
}


def check_api_v1_blocks_logs_reload_create_releases_url_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateReleasesUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
