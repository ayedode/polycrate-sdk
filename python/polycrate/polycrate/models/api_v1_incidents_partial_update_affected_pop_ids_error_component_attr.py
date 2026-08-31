from typing import Literal

ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponentAttr = Literal["affected_pop_ids"]

API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponentAttr
] = {
    "affected_pop_ids",
}


def check_api_v1_incidents_partial_update_affected_pop_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_POP_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
