from typing import Literal

ApiV1BackupsBackupsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_backups_backups_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
