from typing import Literal

ApiV1IncidentsCreateAffectedVolumeIdsErrorComponentAttr = Literal["affected_volume_ids"]

API_V1_INCIDENTS_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateAffectedVolumeIdsErrorComponentAttr
] = {
    "affected_volume_ids",
}


def check_api_v1_incidents_create_affected_volume_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateAffectedVolumeIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
