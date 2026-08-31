from typing import Literal

ApiV1OrganizationsUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_organizations_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
