from typing import Literal

ApiV1AlertroutersArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_alertrouters_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
