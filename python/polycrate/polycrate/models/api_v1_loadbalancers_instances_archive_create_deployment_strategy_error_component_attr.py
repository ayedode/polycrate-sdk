from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponentAttr = Literal["deployment_strategy"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEPLOYMENT_STRATEGY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponentAttr
] = {
    "deployment_strategy",
}


def check_api_v1_loadbalancers_instances_archive_create_deployment_strategy_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateDeploymentStrategyErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEPLOYMENT_STRATEGY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_DEPLOYMENT_STRATEGY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
