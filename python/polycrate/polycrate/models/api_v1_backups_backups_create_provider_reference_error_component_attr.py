from typing import Literal

ApiV1BackupsBackupsCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BACKUPS_BACKUPS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_backups_backups_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
