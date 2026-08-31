from typing import Literal

ApiV1OrganizationsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_organizations_update_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
