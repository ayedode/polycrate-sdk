from typing import Literal

ApiV1CertificatesListK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_CERTIFICATES_LIST_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CertificatesListK8SAppErrorComponentAttr] = {
    "k8s_app",
}


def check_api_v1_certificates_list_k8s_app_error_component_attr(
    value: str,
) -> ApiV1CertificatesListK8SAppErrorComponentAttr:
    if value in API_V1_CERTIFICATES_LIST_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
