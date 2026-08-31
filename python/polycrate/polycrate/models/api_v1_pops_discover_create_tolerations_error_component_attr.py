from typing import Literal

ApiV1PopsDiscoverCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POPS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pops_discover_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateTolerationsErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
