from typing import Literal

ApiV1RegionsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_regions_create_kind_error_component_attr(value: str) -> ApiV1RegionsCreateKindErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
