from typing import Literal

ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponentAttr = Literal["loopback_project_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponentAttr
] = {
    "loopback_project_id",
}


def check_api_v1_organizations_discover_create_loopback_project_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
