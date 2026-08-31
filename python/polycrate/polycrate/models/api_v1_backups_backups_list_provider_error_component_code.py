from typing import Literal

ApiV1BackupsBackupsListProviderErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsListProviderErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backups_list_provider_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsListProviderErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
