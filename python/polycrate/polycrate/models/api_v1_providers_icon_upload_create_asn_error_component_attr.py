from typing import Literal

ApiV1ProvidersIconUploadCreateAsnErrorComponentAttr = Literal["asn"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateAsnErrorComponentAttr
] = {
    "asn",
}


def check_api_v1_providers_icon_upload_create_asn_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateAsnErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
