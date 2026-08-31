from typing import Literal

ApiV1OrganizationsUpdateHarborGroupIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateHarborGroupIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_update_harbor_group_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateHarborGroupIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
