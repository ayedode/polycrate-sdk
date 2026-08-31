from typing import Literal

ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DATASOURCES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_datasources_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
