from typing import Literal

ApiV1CertificatesPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_certificates_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
