from typing import Literal

ApiV1AlertsArchiveCreatePodErrorComponentAttr = Literal["pod"]

API_V1_ALERTS_ARCHIVE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsArchiveCreatePodErrorComponentAttr] = {
    "pod",
}


def check_api_v1_alerts_archive_create_pod_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreatePodErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
