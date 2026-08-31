from typing import Literal

ApiV1BackupsBackupsPartialUpdateExpirationErrorComponentAttr = Literal["expiration"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateExpirationErrorComponentAttr
] = {
    "expiration",
}


def check_api_v1_backups_backups_partial_update_expiration_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateExpirationErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
