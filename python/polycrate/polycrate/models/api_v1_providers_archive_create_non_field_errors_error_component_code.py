from typing import Literal

ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
