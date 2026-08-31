from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationUpdateRequest")


@_attrs_define
class ConversationUpdateRequest:
    """Serializer for Conversation updates.
    Following S3 pattern with restricted update fields.

        Attributes:
            status (ConversationStatusEnum | Unset): * `closed` - Closed
                * `waiting_for_operator` - Waiting for Operator
                * `waiting_for_user` - Waiting for User
                * `deleted` - Deleted
            provider_id (None | str | Unset):
            meta (Any | Unset): Conversation metadata as JSON object
            config (Any | Unset): Conversation configuration as JSON object
    """

    status: ConversationStatusEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        meta = self.meta

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        if not isinstance(self.meta, Unset):
            files.append(("meta", (None, str(self.meta).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ConversationStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_conversation_status_enum(_status)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        conversation_update_request = cls(
            status=status,
            provider_id=provider_id,
            meta=meta,
            config=config,
        )

        conversation_update_request.additional_properties = d
        return conversation_update_request

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
