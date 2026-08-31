from typing import Literal

ApiV1CertificatesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_certificates_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
