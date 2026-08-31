from typing import Literal

ApiV1AlertsArchiveCreateExternalUrlErrorComponentAttr = Literal["external_url"]

API_V1_ALERTS_ARCHIVE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateExternalUrlErrorComponentAttr
] = {
    "external_url",
}


def check_api_v1_alerts_archive_create_external_url_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateExternalUrlErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
