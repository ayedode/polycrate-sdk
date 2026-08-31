from typing import Literal

ApiV1CertificatesCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_certificates_create_namespace_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateNamespaceErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
