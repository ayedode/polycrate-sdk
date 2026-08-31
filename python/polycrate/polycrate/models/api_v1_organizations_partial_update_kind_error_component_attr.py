from typing import Literal

ApiV1OrganizationsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_organizations_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
