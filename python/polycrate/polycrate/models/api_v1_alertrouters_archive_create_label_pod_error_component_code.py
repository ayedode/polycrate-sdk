from typing import Literal

ApiV1AlertroutersArchiveCreateLabelPodErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelPodErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_archive_create_label_pod_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelPodErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_POD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
