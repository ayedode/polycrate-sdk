from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_component_attr import (
    ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr,
    check_api_v1_datasources_rescan_notes_create_last_sync_error_component_attr,
)
from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_component_code import (
    ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentCode,
    check_api_v1_datasources_rescan_notes_create_last_sync_error_component_code,
)

T = TypeVar("T", bound="ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent")


@_attrs_define
class ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent:
    """
    Attributes:
        attr (ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr): * `last_sync` - last_sync
        code (ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentCode): * `date` - date
            * `invalid` - invalid
            * `make_aware` - make_aware
            * `overflow` - overflow
        detail (str):
    """

    attr: ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentAttr
    code: ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr: str = self.attr

        code: str = self.code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = check_api_v1_datasources_rescan_notes_create_last_sync_error_component_attr(d.pop("attr"))

        code = check_api_v1_datasources_rescan_notes_create_last_sync_error_component_code(d.pop("code"))

        detail = d.pop("detail")

        api_v1_datasources_rescan_notes_create_last_sync_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        api_v1_datasources_rescan_notes_create_last_sync_error_component.additional_properties = d
        return api_v1_datasources_rescan_notes_create_last_sync_error_component

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
