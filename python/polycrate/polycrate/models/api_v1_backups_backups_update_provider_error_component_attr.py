from typing import Literal

ApiV1BackupsBackupsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_backups_backups_update_provider_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateProviderErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
