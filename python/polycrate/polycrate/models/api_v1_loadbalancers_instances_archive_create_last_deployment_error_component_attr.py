from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponentAttr = Literal["last_deployment"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_LAST_DEPLOYMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponentAttr
] = {
    "last_deployment",
}


def check_api_v1_loadbalancers_instances_archive_create_last_deployment_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateLastDeploymentErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_LAST_DEPLOYMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_LAST_DEPLOYMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
