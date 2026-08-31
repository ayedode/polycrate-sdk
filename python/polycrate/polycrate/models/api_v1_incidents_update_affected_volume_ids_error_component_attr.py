from typing import Literal

ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponentAttr = Literal["affected_volume_ids"]

API_V1_INCIDENTS_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponentAttr
] = {
    "affected_volume_ids",
}


def check_api_v1_incidents_update_affected_volume_ids_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_AFFECTED_VOLUME_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
