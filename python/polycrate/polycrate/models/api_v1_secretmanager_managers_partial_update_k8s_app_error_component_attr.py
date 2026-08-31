from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_secretmanager_managers_partial_update_k8s_app_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
