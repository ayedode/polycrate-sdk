from typing import Literal

ApiV1OrganizationsUpdateHarborProjectIdErrorComponentAttr = Literal["harbor_project_id"]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateHarborProjectIdErrorComponentAttr
] = {
    "harbor_project_id",
}


def check_api_v1_organizations_update_harbor_project_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateHarborProjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
