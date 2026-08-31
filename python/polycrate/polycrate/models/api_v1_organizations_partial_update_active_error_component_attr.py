from typing import Literal

ApiV1OrganizationsPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_organizations_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
