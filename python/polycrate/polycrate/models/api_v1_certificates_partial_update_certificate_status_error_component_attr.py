from typing import Literal

ApiV1CertificatesPartialUpdateCertificateStatusErrorComponentAttr = Literal["certificate_status"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateCertificateStatusErrorComponentAttr
] = {
    "certificate_status",
}


def check_api_v1_certificates_partial_update_certificate_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateCertificateStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_CERTIFICATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
