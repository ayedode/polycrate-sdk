from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3ObjectItem")


@_attrs_define
class S3ObjectItem:
    """
    Attributes:
        key (str):
        size (int | None): Dateigröße in Bytes, null bei Prefixes
        last_modified (datetime.datetime | None):
        is_prefix (bool): True = Ordner/Prefix, False = Datei
        display_name (str): Dateiname ohne Pfad-Prefix
    """

    key: str
    size: int | None
    last_modified: datetime.datetime | None
    is_prefix: bool
    display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        size: int | None
        size = self.size

        last_modified: None | str
        if isinstance(self.last_modified, datetime.datetime):
            last_modified = self.last_modified.isoformat()
        else:
            last_modified = self.last_modified

        is_prefix = self.is_prefix

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "size": size,
                "last_modified": last_modified,
                "is_prefix": is_prefix,
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size = _parse_size(d.pop("size"))

        def _parse_last_modified(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_type_0 = datetime.datetime.fromisoformat(data)

                return last_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_modified = _parse_last_modified(d.pop("last_modified"))

        is_prefix = d.pop("is_prefix")

        display_name = d.pop("display_name")

        s3_object_item = cls(
            key=key,
            size=size,
            last_modified=last_modified,
            is_prefix=is_prefix,
            display_name=display_name,
        )

        s3_object_item.additional_properties = d
        return s3_object_item

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
