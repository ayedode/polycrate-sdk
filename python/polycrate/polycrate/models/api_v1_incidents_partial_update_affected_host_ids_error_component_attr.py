from typing import Literal

ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponentAttr = Literal["affected_host_ids"]

API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponentAttr
] = {
    "affected_host_ids",
}


def check_api_v1_incidents_partial_update_affected_host_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
