from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_archive_create_metrics_data_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
