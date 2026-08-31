from typing import Literal

ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_archive_create_loadbalancer_instance_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
