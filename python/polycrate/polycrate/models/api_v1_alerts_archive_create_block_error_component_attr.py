from typing import Literal

ApiV1AlertsArchiveCreateBlockErrorComponentAttr = Literal["block"]

API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsArchiveCreateBlockErrorComponentAttr] = {
    "block",
}


def check_api_v1_alerts_archive_create_block_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateBlockErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
