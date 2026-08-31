from typing import Literal

ApiV1IncidentsCreateAffectedHostIdsErrorComponentAttr = Literal["affected_host_ids"]

API_V1_INCIDENTS_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateAffectedHostIdsErrorComponentAttr
] = {
    "affected_host_ids",
}


def check_api_v1_incidents_create_affected_host_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateAffectedHostIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_AFFECTED_HOST_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
