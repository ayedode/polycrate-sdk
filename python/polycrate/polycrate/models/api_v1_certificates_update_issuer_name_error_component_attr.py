from typing import Literal

ApiV1CertificatesUpdateIssuerNameErrorComponentAttr = Literal["issuer_name"]

API_V1_CERTIFICATES_UPDATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateIssuerNameErrorComponentAttr
] = {
    "issuer_name",
}


def check_api_v1_certificates_update_issuer_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateIssuerNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_ISSUER_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
