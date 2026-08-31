from typing import Literal

ApiV1OrganizationsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_organizations_create_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
