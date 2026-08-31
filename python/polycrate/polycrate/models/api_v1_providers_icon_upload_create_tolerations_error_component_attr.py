from typing import Literal

ApiV1ProvidersIconUploadCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_providers_icon_upload_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
