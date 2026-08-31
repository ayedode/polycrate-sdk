from typing import Literal

ApiV1PopsListAffectedIncidentsErrorComponentAttr = Literal["affected_incidents"]

API_V1_POPS_LIST_AFFECTED_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsListAffectedIncidentsErrorComponentAttr
] = {
    "affected_incidents",
}


def check_api_v1_pops_list_affected_incidents_error_component_attr(
    value: str,
) -> ApiV1PopsListAffectedIncidentsErrorComponentAttr:
    if value in API_V1_POPS_LIST_AFFECTED_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_AFFECTED_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
