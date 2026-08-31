from typing import Literal

ApiV1CertificatesArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_certificates_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
