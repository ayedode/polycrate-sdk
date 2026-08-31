from typing import Literal

ApiV1CertificatesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_certificates_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
