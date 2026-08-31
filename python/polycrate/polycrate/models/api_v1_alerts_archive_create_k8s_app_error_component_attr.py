from typing import Literal

ApiV1AlertsArchiveCreateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_ALERTS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_alerts_archive_create_k8s_app_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateK8SAppErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
