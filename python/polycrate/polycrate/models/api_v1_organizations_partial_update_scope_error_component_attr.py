from typing import Literal

ApiV1OrganizationsPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_organizations_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
