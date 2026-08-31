from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostStatementLineItemUsageRow")


@_attrs_define
class CostStatementLineItemUsageRow:
    """Read-only usage breakdown under a line item. Spec: polycrate spec inspect 174.

    Attributes:
        id (int):
        source_kind (str):
        payload (Any):
        sort_order (int):
        source_object_id (None | UUID):
    """

    id: int
    source_kind: str
    payload: Any
    sort_order: int
    source_object_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source_kind = self.source_kind

        payload = self.payload

        sort_order = self.sort_order

        source_object_id: None | str
        if isinstance(self.source_object_id, UUID):
            source_object_id = str(self.source_object_id)
        else:
            source_object_id = self.source_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source_kind": source_kind,
                "payload": payload,
                "sort_order": sort_order,
                "source_object_id": source_object_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        source_kind = d.pop("source_kind")

        payload = d.pop("payload")

        sort_order = d.pop("sort_order")

        def _parse_source_object_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_object_id_type_0 = UUID(data)

                return source_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        source_object_id = _parse_source_object_id(d.pop("source_object_id"))

        cost_statement_line_item_usage_row = cls(
            id=id,
            source_kind=source_kind,
            payload=payload,
            sort_order=sort_order,
            source_object_id=source_object_id,
        )

        cost_statement_line_item_usage_row.additional_properties = d
        return cost_statement_line_item_usage_row

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
