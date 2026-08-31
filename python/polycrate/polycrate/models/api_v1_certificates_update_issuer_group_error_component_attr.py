from typing import Literal

ApiV1CertificatesUpdateIssuerGroupErrorComponentAttr = Literal["issuer_group"]

API_V1_CERTIFICATES_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateIssuerGroupErrorComponentAttr
] = {
    "issuer_group",
}


def check_api_v1_certificates_update_issuer_group_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateIssuerGroupErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
