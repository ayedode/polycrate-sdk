from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_kubernetes_controlplanes_archive_create_actual_availability_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
