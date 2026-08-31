from typing import Literal

ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponentAttr = Literal["cached_endpoint_down_count"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponentAttr
] = {
    "cached_endpoint_down_count",
}


def check_api_v1_organizations_update_cached_endpoint_down_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_ENDPOINT_DOWN_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
