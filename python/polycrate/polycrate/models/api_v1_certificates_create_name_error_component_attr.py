from typing import Literal

ApiV1CertificatesCreateNameErrorComponentAttr = Literal["name"]

API_V1_CERTIFICATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CertificatesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_certificates_create_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
