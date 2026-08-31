from typing import Literal

ApiV1CvesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CVES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_cves_create_kind_error_component_attr(value: str) -> ApiV1CvesCreateKindErrorComponentAttr:
    if value in API_V1_CVES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
