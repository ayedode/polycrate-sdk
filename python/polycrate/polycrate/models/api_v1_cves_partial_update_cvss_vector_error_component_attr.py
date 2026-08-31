from typing import Literal

ApiV1CvesPartialUpdateCvssVectorErrorComponentAttr = Literal["cvss_vector"]

API_V1_CVES_PARTIAL_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdateCvssVectorErrorComponentAttr
] = {
    "cvss_vector",
}


def check_api_v1_cves_partial_update_cvss_vector_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateCvssVectorErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
