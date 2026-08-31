from typing import Literal

ApiV1ProvidersIconUploadCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_providers_icon_upload_create_slug_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateSlugErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
