from typing import Literal

ApiV1IncidentsListAffectedPopsErrorComponentAttr = Literal["affected_pops"]

API_V1_INCIDENTS_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsListAffectedPopsErrorComponentAttr
] = {
    "affected_pops",
}


def check_api_v1_incidents_list_affected_pops_error_component_attr(
    value: str,
) -> ApiV1IncidentsListAffectedPopsErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_AFFECTED_POPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
