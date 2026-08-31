from typing import Literal

ApiV1BackupsBackupsListProviderErrorComponentAttr = Literal["provider"]

API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_backups_backups_list_provider_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListProviderErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
