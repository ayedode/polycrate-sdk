from typing import Literal

ApiV1OrganizationsCreateUpstreamSystemIdErrorComponentAttr = Literal["upstream_system_id"]

API_V1_ORGANIZATIONS_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateUpstreamSystemIdErrorComponentAttr
] = {
    "upstream_system_id",
}


def check_api_v1_organizations_create_upstream_system_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateUpstreamSystemIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
