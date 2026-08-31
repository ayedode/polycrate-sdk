from typing import Literal

ApiV1CertificatesPartialUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
