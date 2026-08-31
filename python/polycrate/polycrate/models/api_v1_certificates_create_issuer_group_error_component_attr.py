from typing import Literal

ApiV1CertificatesCreateIssuerGroupErrorComponentAttr = Literal["issuer_group"]

API_V1_CERTIFICATES_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateIssuerGroupErrorComponentAttr
] = {
    "issuer_group",
}


def check_api_v1_certificates_create_issuer_group_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateIssuerGroupErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
