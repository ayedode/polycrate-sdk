from typing import Literal

ApiV1CertificatesUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_certificates_update_namespace_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateNamespaceErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
