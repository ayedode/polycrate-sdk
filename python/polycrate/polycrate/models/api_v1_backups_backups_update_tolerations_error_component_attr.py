from typing import Literal

ApiV1BackupsBackupsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_backups_backups_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
