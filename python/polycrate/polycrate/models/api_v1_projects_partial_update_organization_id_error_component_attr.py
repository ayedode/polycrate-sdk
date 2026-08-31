from typing import Literal

ApiV1ProjectsPartialUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_PROJECTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_projects_partial_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
