from typing import Literal

ApiV1CertificatesUpdateCertManagerStatusErrorComponentAttr = Literal["cert_manager_status"]

API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateCertManagerStatusErrorComponentAttr
] = {
    "cert_manager_status",
}


def check_api_v1_certificates_update_cert_manager_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateCertManagerStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CERT_MANAGER_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
