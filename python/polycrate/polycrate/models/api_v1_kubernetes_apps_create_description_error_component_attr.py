from typing import Literal

ApiV1KubernetesAppsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_kubernetes_apps_create_description_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateDescriptionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
