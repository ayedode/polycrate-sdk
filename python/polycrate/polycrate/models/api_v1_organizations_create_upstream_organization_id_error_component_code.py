from typing import Literal

ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_create_upstream_organization_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
