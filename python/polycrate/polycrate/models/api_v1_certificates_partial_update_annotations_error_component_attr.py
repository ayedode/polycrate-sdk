from typing import Literal

ApiV1CertificatesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_certificates_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
