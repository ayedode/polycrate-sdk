from typing import Literal

ApiV1PopsDiscoverCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POPS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_pops_discover_create_description_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateDescriptionErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
