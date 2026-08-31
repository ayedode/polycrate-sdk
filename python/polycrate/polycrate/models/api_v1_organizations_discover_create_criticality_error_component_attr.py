from typing import Literal

ApiV1OrganizationsDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_organizations_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
