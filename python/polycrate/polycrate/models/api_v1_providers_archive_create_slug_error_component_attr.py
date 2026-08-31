from typing import Literal

ApiV1ProvidersArchiveCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_providers_archive_create_slug_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateSlugErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
