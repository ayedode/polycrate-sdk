from typing import Literal

ApiV1IncidentsListAffectedOrganizationErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsListAffectedOrganizationErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_incidents_list_affected_organization_error_component_code(
    value: str,
) -> ApiV1IncidentsListAffectedOrganizationErrorComponentCode:
    if value in API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
