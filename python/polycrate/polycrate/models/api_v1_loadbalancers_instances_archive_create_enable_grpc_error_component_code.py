from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_archive_create_enable_grpc_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateEnableGrpcErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_ENABLE_GRPC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
