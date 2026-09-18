from typing import Literal

ApiV1OrganizationsListSlugErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1OrganizationsListSlugErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_organizations_list_slug_error_component_code(
    value: str,
) -> ApiV1OrganizationsListSlugErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_SLUG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
