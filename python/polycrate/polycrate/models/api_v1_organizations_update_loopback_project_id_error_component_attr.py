from typing import Literal

ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponentAttr = Literal["loopback_project_id"]

API_V1_ORGANIZATIONS_UPDATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponentAttr
] = {
    "loopback_project_id",
}


def check_api_v1_organizations_update_loopback_project_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
