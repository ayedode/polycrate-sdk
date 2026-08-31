from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_object_item import S3ObjectItem


T = TypeVar("T", bound="S3ObjectListResponse")


@_attrs_define
class S3ObjectListResponse:
    """
    Attributes:
        objects (list[S3ObjectItem]):
        current_prefix (str):
        continuation_token (None | str):
        next_continuation_token (None | str):
        is_truncated (bool):
        total_count (int):
    """

    objects: list[S3ObjectItem]
    current_prefix: str
    continuation_token: None | str
    next_continuation_token: None | str
    is_truncated: bool
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        current_prefix = self.current_prefix

        continuation_token: None | str
        continuation_token = self.continuation_token

        next_continuation_token: None | str
        next_continuation_token = self.next_continuation_token

        is_truncated = self.is_truncated

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objects": objects,
                "current_prefix": current_prefix,
                "continuation_token": continuation_token,
                "next_continuation_token": next_continuation_token,
                "is_truncated": is_truncated,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_object_item import S3ObjectItem

        d = dict(src_dict)
        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = S3ObjectItem.from_dict(objects_item_data)

            objects.append(objects_item)

        current_prefix = d.pop("current_prefix")

        def _parse_continuation_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token"))

        def _parse_next_continuation_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_continuation_token = _parse_next_continuation_token(d.pop("next_continuation_token"))

        is_truncated = d.pop("is_truncated")

        total_count = d.pop("total_count")

        s3_object_list_response = cls(
            objects=objects,
            current_prefix=current_prefix,
            continuation_token=continuation_token,
            next_continuation_token=next_continuation_token,
            is_truncated=is_truncated,
            total_count=total_count,
        )

        s3_object_list_response.additional_properties = d
        return s3_object_list_response

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
