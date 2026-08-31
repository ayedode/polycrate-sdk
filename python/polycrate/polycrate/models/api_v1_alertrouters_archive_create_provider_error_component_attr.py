from typing import Literal

ApiV1AlertroutersArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertrouters_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
