from typing import Literal

ApiV1S3ClustersUpdateSloWindowDaysErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1S3_CLUSTERS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1s3_clusters_update_slo_window_days_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateSloWindowDaysErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
