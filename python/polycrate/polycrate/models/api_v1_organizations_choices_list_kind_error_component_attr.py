from typing import Literal

ApiV1OrganizationsChoicesListKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_organizations_choices_list_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
