from typing import Literal

ApiV1CertificatesCreateIssuerNameErrorComponentAttr = Literal["issuer_name"]

API_V1_CERTIFICATES_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateIssuerNameErrorComponentAttr
] = {
    "issuer_name",
}


def check_api_v1_certificates_create_issuer_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateIssuerNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
