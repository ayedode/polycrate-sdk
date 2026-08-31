from typing import Literal

ApiV1DowntimesArchiveCreateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreateSeverityErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_downtimes_archive_create_severity_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreateSeverityErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
