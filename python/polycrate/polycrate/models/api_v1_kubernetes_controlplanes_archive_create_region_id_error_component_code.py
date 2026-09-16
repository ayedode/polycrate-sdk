from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateRegionIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateRegionIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_kubernetes_controlplanes_archive_create_region_id_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateRegionIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_REGION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
