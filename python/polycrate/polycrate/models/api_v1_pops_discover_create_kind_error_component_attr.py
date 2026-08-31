from typing import Literal

ApiV1PopsDiscoverCreateKindErrorComponentAttr = Literal["kind"]

API_V1_POPS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsDiscoverCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pops_discover_create_kind_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateKindErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
