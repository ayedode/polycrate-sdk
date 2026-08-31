from typing import Literal

ApiV1RegionsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_REGIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_regions_create_scope_error_component_attr(value: str) -> ApiV1RegionsCreateScopeErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
