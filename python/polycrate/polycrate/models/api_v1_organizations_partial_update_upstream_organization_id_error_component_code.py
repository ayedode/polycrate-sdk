from typing import Literal

ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_partial_update_upstream_organization_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
