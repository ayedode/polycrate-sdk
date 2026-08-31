from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentAttr = Literal["enable_grpc"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentAttr
] = {
    "enable_grpc",
}


def check_api_v1_loadbalancers_instances_archive_create_enable_grpc_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
