from typing import Literal

ApiV1BackupsBackupsCreateExpirationErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_CREATE_EXPIRATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateExpirationErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_create_expiration_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateExpirationErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_EXPIRATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_EXPIRATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
