from typing import Literal

ApiV1AlertcategoriesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertcategories_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
