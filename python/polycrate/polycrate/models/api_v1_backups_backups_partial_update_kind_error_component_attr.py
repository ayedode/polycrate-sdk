from typing import Literal

ApiV1BackupsBackupsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_backups_backups_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
