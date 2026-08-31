from typing import Literal

ApiV1CertificatesSyncCreateCertDataErrorComponentAttr = Literal["cert_data"]

API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesSyncCreateCertDataErrorComponentAttr
] = {
    "cert_data",
}


def check_api_v1_certificates_sync_create_cert_data_error_component_attr(
    value: str,
) -> ApiV1CertificatesSyncCreateCertDataErrorComponentAttr:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_CERT_DATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
