from typing import Literal

ApiV1CvesUpdateCvssVectorErrorComponentAttr = Literal["cvss_vector"]

API_V1_CVES_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateCvssVectorErrorComponentAttr] = {
    "cvss_vector",
}


def check_api_v1_cves_update_cvss_vector_error_component_attr(
    value: str,
) -> ApiV1CvesUpdateCvssVectorErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
