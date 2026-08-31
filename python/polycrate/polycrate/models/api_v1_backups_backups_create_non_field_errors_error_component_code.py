from typing import Literal

ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
