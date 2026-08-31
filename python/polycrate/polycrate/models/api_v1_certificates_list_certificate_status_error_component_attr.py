from typing import Literal

ApiV1CertificatesListCertificateStatusErrorComponentAttr = Literal["certificate_status"]

API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesListCertificateStatusErrorComponentAttr
] = {
    "certificate_status",
}


def check_api_v1_certificates_list_certificate_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesListCertificateStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
