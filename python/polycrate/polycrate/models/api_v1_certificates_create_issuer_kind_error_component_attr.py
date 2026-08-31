from typing import Literal

ApiV1CertificatesCreateIssuerKindErrorComponentAttr = Literal["issuer_kind"]

API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateIssuerKindErrorComponentAttr
] = {
    "issuer_kind",
}


def check_api_v1_certificates_create_issuer_kind_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateIssuerKindErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
