from typing import Literal

ApiV1RegionsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_REGIONS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_regions_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
