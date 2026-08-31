from typing import Literal

ApiV1AlertsArchiveCreateStatusErrorComponentAttr = Literal["status"]

API_V1_ALERTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_alerts_archive_create_status_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateStatusErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
