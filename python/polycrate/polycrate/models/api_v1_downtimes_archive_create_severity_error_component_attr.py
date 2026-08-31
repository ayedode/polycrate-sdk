from typing import Literal

ApiV1DowntimesArchiveCreateSeverityErrorComponentAttr = Literal["severity"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateSeverityErrorComponentAttr
] = {
    "severity",
}


def check_api_v1_downtimes_archive_create_severity_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateSeverityErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
