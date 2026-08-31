from typing import Literal

ApiV1CvesCreateModifiedAtErrorComponentAttr = Literal["modified_at"]

API_V1_CVES_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateModifiedAtErrorComponentAttr] = {
    "modified_at",
}


def check_api_v1_cves_create_modified_at_error_component_attr(
    value: str,
) -> ApiV1CvesCreateModifiedAtErrorComponentAttr:
    if value in API_V1_CVES_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
