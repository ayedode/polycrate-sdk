from typing import Literal

ApiV1ContactgroupsCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_CONTACTGROUPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_contactgroups_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
