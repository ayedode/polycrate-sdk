from typing import Literal

ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentAttr = Literal["icon_content_type"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentAttr
] = {
    "icon_content_type",
}


def check_api_v1_providers_icon_upload_create_icon_content_type_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateIconContentTypeErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ICON_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
