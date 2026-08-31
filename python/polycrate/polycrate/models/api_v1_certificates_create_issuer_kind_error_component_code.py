from typing import Literal

ApiV1CertificatesCreateIssuerKindErrorComponentCode = Literal["invalid_choice"]

API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateIssuerKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_certificates_create_issuer_kind_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateIssuerKindErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
