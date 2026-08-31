from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.content_kind_enum import ContentKindEnum, check_content_kind_enum
from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.message_status_enum import MessageStatusEnum, check_message_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageRequest")


@_attrs_define
class MessageRequest:
    """Full serializer for Message detail views and CRUD operations.
    Following S3 pattern with comprehensive fields and validation.

        Attributes:
            name (str):
            meta (Any): Message metadata as JSON object
            config (Any): Message configuration as JSON object
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            status (MessageStatusEnum | Unset): * `pending` - Pending
                * `requested` - Requested
                * `delivered` - Delivered
                * `error` - Error
                * `deleted` - Deleted
            content (str | Unset): The actual message content
            content_kind (ContentKindEnum | Unset): * `text` - Text
                * `markdown` - Markdown
                * `html` - HTML
                * `json` - JSON
                * `yaml` - YAML
            provider_id (None | str | Unset):
    """

    name: str
    meta: Any
    config: Any
    kind: ConversationKindEnum | Unset = UNSET
    status: MessageStatusEnum | Unset = UNSET
    content: str | Unset = UNSET
    content_kind: ContentKindEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        meta = self.meta

        config = self.config

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        content = self.content

        content_kind: str | Unset = UNSET
        if not isinstance(self.content_kind, Unset):
            content_kind = self.content_kind

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "meta": meta,
                "config": config,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if content is not UNSET:
            field_dict["content"] = content
        if content_kind is not UNSET:
            field_dict["content_kind"] = content_kind
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("meta", (None, str(self.meta).encode(), "text/plain")))

        files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.content_kind, Unset):
            files.append(("content_kind", (None, str(self.content_kind).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        meta = d.pop("meta")

        config = d.pop("config")

        _kind = d.pop("kind", UNSET)
        kind: ConversationKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_conversation_kind_enum(_kind)

        _status = d.pop("status", UNSET)
        status: MessageStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_message_status_enum(_status)

        content = d.pop("content", UNSET)

        _content_kind = d.pop("content_kind", UNSET)
        content_kind: ContentKindEnum | Unset
        if isinstance(_content_kind, Unset):
            content_kind = UNSET
        else:
            content_kind = check_content_kind_enum(_content_kind)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        message_request = cls(
            name=name,
            meta=meta,
            config=config,
            kind=kind,
            status=status,
            content=content,
            content_kind=content_kind,
            provider_id=provider_id,
        )

        message_request.additional_properties = d
        return message_request

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
