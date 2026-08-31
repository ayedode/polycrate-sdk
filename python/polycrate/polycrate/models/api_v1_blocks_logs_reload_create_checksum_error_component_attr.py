from typing import Literal

ApiV1BlocksLogsReloadCreateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateChecksumErrorComponentAttr
] = {
    "checksum",
}


def check_api_v1_blocks_logs_reload_create_checksum_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
