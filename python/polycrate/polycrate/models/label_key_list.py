from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_keys_enum import LabelKeysEnum, check_label_keys_enum

T = TypeVar("T", bound="LabelKeyList")


@_attrs_define
class LabelKeyList:
    """
    Attributes:
        label_keys (list[LabelKeysEnum]):
    """

    label_keys: list[LabelKeysEnum]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_keys = []
        for label_keys_item_data in self.label_keys:
            label_keys_item: str = label_keys_item_data
            label_keys.append(label_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label_keys": label_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label_keys = []
        _label_keys = d.pop("label_keys")
        for label_keys_item_data in _label_keys:
            label_keys_item = check_label_keys_enum(label_keys_item_data)

            label_keys.append(label_keys_item)

        label_key_list = cls(
            label_keys=label_keys,
        )

        label_key_list.additional_properties = d
        return label_key_list

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
