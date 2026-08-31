from typing import Literal

ApiV1CertificatesUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_certificates_update_metadata_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateMetadataErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
