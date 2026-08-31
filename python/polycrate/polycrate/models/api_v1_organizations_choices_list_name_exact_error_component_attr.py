from typing import Literal

ApiV1OrganizationsChoicesListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_ORGANIZATIONS_CHOICES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_organizations_choices_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListNameExactErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
