from typing import Literal

ApiV1OrganizationsListKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_organizations_list_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
