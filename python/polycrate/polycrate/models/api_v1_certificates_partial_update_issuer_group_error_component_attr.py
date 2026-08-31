from typing import Literal

ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentAttr = Literal["issuer_group"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentAttr
] = {
    "issuer_group",
}


def check_api_v1_certificates_partial_update_issuer_group_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
