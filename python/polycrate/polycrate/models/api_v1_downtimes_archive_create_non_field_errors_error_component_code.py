from typing import Literal

ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
