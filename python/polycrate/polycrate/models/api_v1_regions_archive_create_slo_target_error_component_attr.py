from typing import Literal

ApiV1RegionsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_REGIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_regions_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
