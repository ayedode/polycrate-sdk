from typing import Literal

ApiV1CertificatesPartialUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_certificates_partial_update_namespace_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateNamespaceErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
