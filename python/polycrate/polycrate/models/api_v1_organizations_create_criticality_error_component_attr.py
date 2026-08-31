from typing import Literal

ApiV1OrganizationsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ORGANIZATIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_organizations_create_criticality_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCriticalityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
