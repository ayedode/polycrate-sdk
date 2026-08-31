from typing import Literal

ApiV1AlertcategoriesArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alertcategories_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateProviderErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
