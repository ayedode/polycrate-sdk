from typing import Literal

ApiV1OrganizationsCreateCachedLbCountErrorComponentAttr = Literal["cached_lb_count"]

API_V1_ORGANIZATIONS_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedLbCountErrorComponentAttr
] = {
    "cached_lb_count",
}


def check_api_v1_organizations_create_cached_lb_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedLbCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
