from typing import Literal

ApiV1CvesArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_CVES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_cves_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
