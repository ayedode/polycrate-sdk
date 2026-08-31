from typing import Literal

ApiV1EndpointsDiscoverCreateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_ENDPOINTS_DISCOVER_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_endpoints_discover_create_k8s_app_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateK8SAppErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
