from typing import Literal

ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_partial_update_upstream_system_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_SYSTEM_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
