from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentAttr = Literal["metrics_data"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentAttr
] = {
    "metrics_data",
}


def check_api_v1_loadbalancers_instances_archive_create_metrics_data_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateMetricsDataErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_METRICS_DATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
