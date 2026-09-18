from typing import Literal

ApiV1IncidentsListAffectedOrganizationErrorComponentAttr = Literal["affected_organization"]

API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsListAffectedOrganizationErrorComponentAttr
] = {
    "affected_organization",
}


def check_api_v1_incidents_list_affected_organization_error_component_attr(
    value: str,
) -> ApiV1IncidentsListAffectedOrganizationErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_AFFECTED_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
