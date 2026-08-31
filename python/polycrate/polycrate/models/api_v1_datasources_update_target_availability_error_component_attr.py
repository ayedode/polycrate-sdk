from typing import Literal

ApiV1DatasourcesUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DATASOURCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_datasources_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
